from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMetaObject, QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QWidget, QListView, QMenuBar, QStatusBar, QMainWindow, QApplication, \
    QPushButton, QListWidget, QLabel, QStackedWidget, QVBoxLayout, QTextEdit
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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


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

        self.TaskEdit = QTextEdit(self.gridLayoutWidget)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.TaskEdit.setFont(font)
        self.TaskEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.TaskEdit.setObjectName("TaskEdit")
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
        number = int(self.TaskEdit.toPlainText())
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stack = None
        self.flag = False
        self.UIinit()

    def UIinit(self):
        self.Widget = QWidget()
        self.stack = QStackedWidget()
        self.window2 = Ui_MainWindow(self)
        self.window1 = MainMenu(self)
        self.window3 = ChoiseWindow(self)
        self.stack.addWidget(self.window1)
        self.stack.addWidget(self.window2)
        self.stack.addWidget(self.window3)
        self.stack.setCurrentWidget(self.window1)

        self.setCentralWidget(self.Widget)
        self.layout = QVBoxLayout(self.Widget)
        self.layout.addWidget(self.stack)

    def back(self):
        self.stack.setCurrentWidget(self.window1)
        self.flag = True

    def First(self):
        global number
        number = 1
        self.window2.deleteLater()
        self.window2 = Ui_MainWindow(self)
        self.stack.addWidget(self.window2)
        self.stack.setCurrentWidget(self.window2)

    def Choice(self):
        self.stack.setCurrentWidget(self.window3)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(1920, 1080)
    window.showMaximized()
    sys.exit(app.exec_())
