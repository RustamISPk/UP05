from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QGridLayout, QWidget, QMainWindow, QApplication, QPushButton, QListWidget, QLabel, \
    QStackedWidget, QVBoxLayout, QTextEdit, QLineEdit
from qt_material import apply_stylesheet
import json

rows, cols = 0, 0

with open('variants.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    variants = json.load(fh)  # загружаем из файла данные в словарь data

with open('answers.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    answer = json.load(fh)  # загружаем из файла данные в словарь data

with open('ColsAndRowsName.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    ColsAndRowsName = json.load(fh)  # загружаем из файла данные в словарь data

boolz = False
number = 1


class AddTask(QMainWindow):

    def __init__(self, mainwindow):
        super().__init__()
        self.TaskCols = None
        self.TaskRows = None
        self.TaskText = None
        self.boolz = None
        self.table = None
        self.table_elements = None
        self.new_answer = None
        self.secondwidget = None
        self.cols = None
        self.rows = None
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        self.mainwidget = QStackedWidget()
        self.setCentralWidget(self.mainwidget)

        self.firstwidget = QWidget()
        self.firstwidget.setObjectName("centralwidget")

        self.Instruction = QLabel(self.firstwidget)
        self.Instruction.setGeometry(QtCore.QRect(1530, 0, 381, 291))
        self.Instruction.setObjectName("label")
        self.Instruction.setText("Instruction")

        self.TaskText = QTextEdit(self.firstwidget)
        self.TaskText.setGeometry(QtCore.QRect(730, 260, 511, 191))
        self.TaskText.setObjectName("TaskText")

        self.TaskRowsText = QLabel(self.firstwidget)
        self.TaskRowsText.setGeometry(QtCore.QRect(730, 470, 200, 35))
        self.TaskRowsText.setObjectName("TaskRowsText")
        self.TaskRowsText.setText('Введите количество строк')

        self.TaskRows = QLineEdit(self.firstwidget)
        self.TaskRows.setGeometry(QtCore.QRect(950, 470, 100, 35))
        self.TaskRows.setObjectName("TaskRows")
        self.TaskRows.setValidator(QIntValidator(1, 99, self))

        self.TaskColsText = QLabel(self.firstwidget)
        self.TaskColsText.setGeometry(QtCore.QRect(730, 510, 200, 35))
        self.TaskColsText.setObjectName("TaskColsText")
        self.TaskColsText.setText('Введите количество колон')

        self.TaskCols = QLineEdit(self.firstwidget)
        self.TaskCols.setGeometry(QtCore.QRect(950, 510, 100, 35))
        self.TaskCols.setObjectName("TaskCols")
        self.TaskCols.setValidator(QIntValidator(1, 99, self))

        self.NextButton = QPushButton(self.firstwidget)
        self.NextButton.setGeometry(QtCore.QRect(730, 560, 511, 70))
        self.NextButton.setText('Сгенерировать таблицу\n для ввода ответа')
        self.NextButton.clicked.connect(lambda: self.tableGen())

        self.BackButton = QPushButton(self.firstwidget)
        self.BackButton.setGeometry(QtCore.QRect(1630, 340, 201, 41))
        self.BackButton.setObjectName("pushButton")
        self.BackButton.setText('Назад')
        self.BackButton.clicked.connect(lambda: mainwindow.back())

        self.secondwidget = QWidget()

        self.mainwidget.addWidget(self.firstwidget)
        self.mainwidget.setCurrentWidget(self.firstwidget)

    def tableGen(self):
        if self.TaskText.toPlainText() and self.TaskRows.text() and int(self.TaskRows.text()) != 0 and self.TaskCols.text() and int(self.TaskCols.text()) != 0 :
            self.backbutton = QPushButton(self.secondwidget)
            self.backbutton.setGeometry(QtCore.QRect(1630, 400, 201, 41))
            self.backbutton.setText('Назад')
            self.backbutton.clicked.connect(lambda: self.back())
            self.table = [[], []]
            NewTaskText = self.TaskText.setPlainText
            self.rows = int(self.TaskRows.text()) + 1
            self.cols = int(self.TaskCols.text()) + 1
            self.table_elements = [[], []]

            self.new_answer = []
            for i in range(self.rows - 1):
                col_new_answer = []
                for j in range(self.cols - 1):
                    col_new_answer.append(' ')
                self.new_answer.append(col_new_answer)

            if self.rows > 0 and self.cols > 0 and NewTaskText != ' ':

                self.gridLayoutWidget = QWidget(self.secondwidget)
                self.gridLayoutWidget.setGeometry(
                    QtCore.QRect(int((1920 - 87 * self.cols) / 2), 300, 87 * self.cols, 87 * self.rows))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")

                self.gridLayout = QGridLayout(self.gridLayoutWidget)
                self.gridLayout.setContentsMargins(0, 0, 0, 0)
                self.gridLayout.setObjectName("gridLayout")

                self.SaveButton = QPushButton(self.secondwidget)
                self.SaveButton.setGeometry(QtCore.QRect(1630, 340, 201, 41))
                self.SaveButton.setText("Сохранить задачу")
                self.SaveButton.clicked.connect(self.saveTask)

                for i in range(self.rows):
                    for j in range(self.cols):
                        self.listView = QLabel(self.secondwidget)
                        self.listView.setText(self.TaskText.toPlainText())
                        self.listView.setGeometry(QtCore.QRect(int((1920 - 1000) / 2), 40, 1000, 200))
                        self.listView.setObjectName("listView")

                        self.pushButton = QPushButton()
                        self.pushButton.setStyleSheet('background-color: yellow')
                        self.pushButton.setMinimumSize(75, 75)
                        self.pushButton.setMaximumSize(75, 75)
                        self.pushButton.setText(f'{i}_{j}')
                        self.pushButton.setObjectName(f'{i}')
                        self.pushButton.setAccessibleName(f'{j}')
                        self.pushButton.clicked.connect(
                            lambda cheked, button=self.pushButton: self.newAnswer(button))

                        self.cell_h = QLineEdit()
                        self.cell_h.setMinimumSize(75, 30)
                        self.cell_h.setMaximumSize(75, 30)
                        self.cell_h.setObjectName(f'{i}{j}')
                        self.cell_h.setStyleSheet('border: 1px solid #000')
                        self.cell_h.setText('')

                        self.cell_v = QLineEdit()
                        self.cell_v.setMinimumSize(75, 30)
                        self.cell_v.setMaximumSize(75, 30)
                        self.cell_v.setObjectName(f'{i}')
                        self.cell_v.setStyleSheet('border: 1px solid #000')
                        self.cell_v.setText('')

                        if i == 0 and j != 0:
                            self.table[0].append(self.cell_h)
                            self.gridLayout.addWidget(self.cell_h, i, j, 1, 1)
                        else:
                            if j == 0 and i != 0:
                                self.table[1].append(self.cell_v)
                                self.gridLayout.addWidget(self.cell_v, i, j, 1, 1)
                            elif i != 0 and j != 0:
                                self.gridLayout.addWidget(self.pushButton, i, j, 1, 1)
                self.mainwidget.addWidget(self.secondwidget)
                self.mainwidget.setCurrentWidget(self.secondwidget)

    def newAnswer(self, button):

        i = int(button.objectName()) - 1
        j = int(button.accessibleName()) - 1
        if self.new_answer[i][j] == ' ':
            self.new_answer[i][j] = '+'
            button.setStyleSheet('background-color: lime')
        elif self.new_answer[i][j] == '-':
            self.new_answer[i][j] = '+'
            button.setStyleSheet('background-color: lime')
        elif self.new_answer[i][j] == '+':
            self.new_answer[i][j] = '-'
            button.setStyleSheet('background-color: red')
        button.setText(f'{self.new_answer[i][j]}')

        count = 0

        for a in range(self.rows - 1):
            for b in range(self.cols - 1):
                if self.new_answer[a][b] == ' ':
                    count += 1

        if count == 0:
            self.boolz = True
        else:
            self.boolz = False

    def saveTask(self):
        global variants, answer, ColsAndRowsName
        cellhcheck = False
        cellvcheck = False

        for self.cell_h in self.table[0]:
            if self.cell_h.text() != '':
                cellhcheck = True
            else:
                cellhcheck = False
                break

        for self.cell_v in self.table[1]:
            if self.cell_v.text() != '':
                cellvcheck = True
            else:
                cellvcheck = False
                break

        if cellvcheck == True and cellhcheck == True and self.boolz == True:
            for self.cell_h in self.table[0]:
                if len(self.table_elements[0]) < self.rows and self.cell_h.text() != '':
                    self.table_elements[0].append(self.cell_h.text())
            for self.cell_v in self.table[1]:
                if len(self.table_elements[1]) < self.cols and self.cell_v.text() != '':
                    self.table_elements[1].append(self.cell_v.text())

            variants[str(len(variants))] = self.TaskText.toPlainText()
            variants[str(len(variants) + 1)] = " "

            answer[str(len(answer))] = self.new_answer
            answer[str(len(answer) + 1)] = " "

            ColsAndRowsName[str(len(ColsAndRowsName))] = self.table_elements
            ColsAndRowsName[str(len(ColsAndRowsName) + 1)] = " "

            with open('ColsAndRowsName.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(ColsAndRowsName, ensure_ascii=False))

            with open('variants.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(variants, ensure_ascii=False))

            with open('answers.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(answer, ensure_ascii=False))

            with open('variants.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                variants = json.load(fh)  # загружаем из файла данные в словарь data

            with open('answers.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                answer = json.load(fh)  # загружаем из файла данные в словарь data

            with open('ColsAndRowsName.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                ColsAndRowsName = json.load(fh)  # загружаем из файла данные в словарь data

            self.mainwidget.setCurrentWidget(self.firstwidget)
            self.secondwidget.deleteLater()
            self.secondwidget = QWidget()
            self.mainwidget.addWidget(self.secondwidget)
            self.TaskCols.clear()
            self.TaskRows.clear()
            self.TaskText.clear()

    def back(self):
        self.mainwidget.setCurrentWidget(self.firstwidget)
        self.secondwidget.deleteLater()
        self.secondwidget = QWidget()
        self.mainwidget.addWidget(self.secondwidget)
        self.TaskCols.clear()
        self.TaskRows.clear()
        self.TaskText.clear()


class ChoiseWindow(QMainWindow):

    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 10, 470, 101))
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText('Введите номер задачи в поле')
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(390, 100, 1000, 50))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.MenuButton = QPushButton(self.gridLayoutWidget)
        self.MenuButton.setObjectName("MenuButton")
        self.MenuButton.setMinimumSize(150, 50)
        self.MenuButton.setMaximumSize(150, 50)
        self.MenuButton.setText('Назад')
        self.MenuButton.clicked.connect(lambda: mainwindow.back())
        self.gridLayout.addWidget(self.MenuButton, 0, 0, 1, 1)

        self.TaskEdit = QLineEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.TaskEdit.setFont(font)
        self.TaskEdit.setValidator(QIntValidator(1, 999, self))
        self.gridLayout.addWidget(self.TaskEdit, 0, 1, 1, 1)

        self.GameButton = QPushButton(self.gridLayoutWidget)
        self.GameButton.setObjectName("GameButton")
        self.GameButton.setMinimumSize(150, 50)
        self.GameButton.setMaximumSize(150, 50)
        self.GameButton.setText('Продолжить')
        self.GameButton.clicked.connect(lambda: self.TaskNumber(mainwindow))
        self.gridLayout.addWidget(self.GameButton, 0, 2, 1, 1)

        self.setCentralWidget(self.centralwidget)

    def TaskNumber(self, mainwindow):
        global number
        number = int(self.TaskEdit.text())
        if number < len(variants):
            mainwindow.window2.deleteLater()
            mainwindow.window2 = Ui_MainWindow(mainwindow)
            mainwindow.stack.addWidget(mainwindow.window2)
            mainwindow.stack.setCurrentWidget(mainwindow.window2)
            self.TaskEdit.clear()


class MainMenu(QMainWindow):
    global variants, answer, ColsAndRowsName

    def __init__(self, mainwindow):
        super().__init__()
        self.initUI(mainwindow)

    def initUI(self, mainwindow):
        label = QLabel(self)
        label.setGeometry(QRect(691, 40, 538, 111))
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        label.setFont(font)
        label.setObjectName("label")
        verticalLayoutWidget = QWidget(self)
        verticalLayoutWidget.setGeometry(QRect(880, 260, 160, 250))
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        verticalLayout = QVBoxLayout(verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        FirstTask = QPushButton(verticalLayoutWidget)
        FirstTask.setObjectName("FirstTask")
        FirstTask.clicked.connect(lambda: mainwindow.First())
        verticalLayout.addWidget(FirstTask)
        FirstTask.setMinimumSize(150, 75)
        FirstTask.setMaximumSize(150, 75)
        ChooseTask = QPushButton(verticalLayoutWidget)
        ChooseTask.setObjectName("ChooseTask")
        ChooseTask.clicked.connect(lambda: mainwindow.Choice())
        verticalLayout.addWidget(ChooseTask)
        ChooseTask.setMinimumSize(150, 75)
        ChooseTask.setMaximumSize(150, 75)
        NewTask = QPushButton(verticalLayoutWidget)
        NewTask.setObjectName("NewTask")
        verticalLayout.addWidget(NewTask)
        NewTask.setMinimumSize(150, 75)
        NewTask.setMaximumSize(150, 75)
        NewTask.clicked.connect(lambda: mainwindow.AddTask())
        label.setText("Помощник решения логических задач")
        FirstTask.setText("Начать с первой задачи")
        ChooseTask.setText("Выбрать задачу")
        NewTask.setText("Добавить задачу")


class Ui_MainWindow(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.gridLayout = None
        self.gridLayoutWidget = None
        self.listView = None
        self.centralwidget = None
        self.number = None
        self.BackButton = None
        self.cell_v = None
        self.pushButton = None
        self.cell_h = None
        self.width = QApplication.desktop().width()
        self.height = QApplication.desktop().height()
        self.setupUi(self, mainwindow)

    def setupUi(self, MainWindow, mainwindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.width, self.height)
        self.number = number
        self.gameplay(mainwindow)

    def rows_cols_number(self, number):
        global rows, cols
        rows = len(ColsAndRowsName[str(number)][1]) + 1
        cols = len(ColsAndRowsName[str(number)][0]) + 1

    def gameplay(self, mainwindow):
        if self.number < len(variants):
            self.rows_cols_number(self.number)

            gamefield = []
            for i in range(rows - 1):
                col_list = []
                for j in range(cols - 1):
                    col_list.append(' ')
                gamefield.append(col_list)

            self.centralwidget = QWidget()
            self.centralwidget.setObjectName("centralwidget")

            self.BackButton = QPushButton(self.centralwidget)
            self.BackButton.setStyleSheet('background-color: blue')
            self.BackButton.setText('Назад')
            self.BackButton.setGeometry(0, 0, 100, 50)
            self.BackButton.clicked.connect(lambda: mainwindow.back())

            self.listView = QListWidget(self.centralwidget)
            self.listView.setGeometry(QtCore.QRect(int((self.width - 1000) / 2), 40, 1000, 200))
            self.listView.setObjectName("listView")
            self.listView.addItem(str(variants[str(self.number)]))

            self.gridLayoutWidget = QWidget(self.centralwidget)
            self.gridLayoutWidget.setGeometry(
                QtCore.QRect(int((self.width - 87 * cols) / 2), 300, 87 * cols, 87 * rows))
            self.gridLayoutWidget.setObjectName("gridLayoutWidget")

            self.gridLayout = QGridLayout(self.gridLayoutWidget)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setObjectName("gridLayout")

            for i in range(rows):
                for j in range(cols):
                    self.pushButton = QPushButton()
                    self.pushButton.setStyleSheet('background-color: yellow')
                    self.pushButton.setMinimumSize(75, 75)
                    self.pushButton.setMaximumSize(75, 75)
                    self.pushButton.setText(f'{i}_{j}')
                    self.pushButton.setObjectName(f'{i}')
                    self.pushButton.setAccessibleName(f'{j}')
                    self.pushButton.clicked.connect(
                        lambda cheked, button=self.pushButton: self.add_value(button, gamefield, mainwindow))

                    self.cell_h = QLabel()
                    self.cell_h.setMinimumSize(75, 30)
                    self.cell_h.setMaximumSize(75, 30)
                    self.cell_h.setObjectName(f'{i}{j}')
                    self.cell_h.setStyleSheet('border: 1px solid #000')

                    self.cell_v = QLabel()
                    self.cell_v.setMinimumSize(75, 30)
                    self.cell_v.setMaximumSize(75, 30)
                    self.cell_v.setObjectName(f'{i}{j}')
                    self.cell_v.setStyleSheet('border: 1px solid #000')

                    if i == 0 and j != 0:
                        self.cell_h.setText(ColsAndRowsName[str(self.number)][0][j - 1])
                        self.gridLayout.addWidget(self.cell_h, i, j, 1, 1)
                    else:
                        if j == 0 and i != 0:
                            self.cell_v.setText(ColsAndRowsName[str(self.number)][1][i - 1])
                            self.gridLayout.addWidget(self.cell_v, i, j, 1, 1)
                        elif i != 0 and j != 0:
                            self.gridLayout.addWidget(self.pushButton, i, j, 1, 1)

            self.setCentralWidget(self.centralwidget)
        else:
            mainwindow.stack.setCurrentIndex(0)

    def add_value(self, button, lists, mainwindow):
        global boolz
        i = int(button.objectName()) - 1
        j = int(button.accessibleName()) - 1

        if lists[i][j] == ' ':
            lists[i][j] = '+'
            button.setStyleSheet('background-color: lime')
        elif lists[i][j] == '-':
            lists[i][j] = '+'
            button.setStyleSheet('background-color: lime')
        elif lists[i][j] == '+':
            lists[i][j] = '-'
            button.setStyleSheet('background-color: red')
        button.setText(f'{lists[i][j]}')
        count = 0
        for a in range(rows - 1):
            for b in range(cols - 1):
                if lists[a][b] == ' ':
                    count += 1
        if count == 0:
            boolz = True
        else:
            boolz = False
        if boolz == True and lists == answer[str(self.number)]:
            self.number += 1
            self.listView.clear()
            self.listView.addItem(str(variants[str(self.number)]))
            return self.gameplay(mainwindow)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stack = None
        self.flag = False
        self.UIinit()

    def UIinit(self):
        self.Widget = QWidget()
        self.stack = QStackedWidget()

        self.window1 = MainMenu(self)
        self.window2 = Ui_MainWindow(self)
        self.window3 = ChoiseWindow(self)
        self.window4 = AddTask(self)

        self.stack.addWidget(self.window1)
        self.stack.addWidget(self.window2)
        self.stack.addWidget(self.window3)
        self.stack.addWidget(self.window4)
        self.stack.setCurrentWidget(self.window1)

        self.setCentralWidget(self.Widget)
        self.layout = QVBoxLayout(self.Widget)
        self.layout.addWidget(self.stack)

    def back(self):
        self.stack.setCurrentWidget(self.window1)

    def First(self):
        global number
        number = 1
        self.window2.deleteLater()
        self.window2 = Ui_MainWindow(self)
        self.stack.addWidget(self.window2)
        self.stack.setCurrentWidget(self.window2)

    def Choice(self):
        self.stack.setCurrentWidget(self.window3)

    def AddTask(self):
        self.stack.setCurrentWidget(self.window4)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(1920, 1080)
    apply_stylesheet(app, theme='dark_purple.xml')
    window.showMaximized()
    sys.exit(app.exec_())
