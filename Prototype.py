from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMetaObject, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QWidget, QListView, QMenuBar, QStatusBar, QMainWindow, QApplication, \
    QPushButton, QListWidget, QLabel, QStackedWidget, QVBoxLayout

rows, cols = 0, 0
variants = {1: 'Задание №1. В одном дворе живут четыре друга.\n'
               'Вадим и шофёр старше Сергея;\n'
               'Николая и слесарь занимаются боксом;\n'
               'электрик - младший из друзей;\n'
               'по вечерам Антон и токарь играют в домино против Сергея и электрика.\n'
               'Определите профессию каждого из друзей',
            2: 'Задание №2. В одном дворе живут четыре друга.\n'
               'Вадим и шофёр старше Сергея;\n'
               'Николая и слесарь занимаются боксом;\n'
               'электрик - младший из друзей;\n'
               'по вечерам Антон и токарь играют в домино против Сергея и электрика.\n'
               'Определите профессию каждого из друзей',
            3: 'Задание №3. В одном дворе живут четыре друга.\n'
               'Вадим и шофёр старше Сергея;\n'
               'Николая и слесарь занимаются боксом;\n'
               'электрик - младший из друзей;\n'
               'по вечерам Антон и токарь играют в домино против Сергея и электрика.\n'
               'Определите профессию каждого из друзей',
            }
answer = {1: [['-', '-', '-', '+'],
              ['-', '+', '-', '-'],
              ['+', '-', '-', '-'],
              ['-', '-', '+', '-']],
          2: [['+', '-', '-'],
              ['-', '+', '-'],
              ['+', '-', '-'],
              ['+', '-', '-'],
              ['-', '-', '+']],
          3: [['+', '-', '-', '-', '-'],
              ['-', '+', '-', '-', '-'],
              ['-', '-', '+', '-', '-']]
          }

ColsAndRowsName = {1: [['Вадим', 'Сергей', 'Николай', 'Антон'],
                       ['Шофер', 'Слесарь', 'Токарь', 'Электрик']],
                   2: [['Андрей', 'Сергей', 'Николай'],
                       ['Шофер', 'Слесарь', 'Токарь', 'Электрик', 'Повар']],
                   3: [['Шофер', 'Слесарь', 'Токарь', 'Электрик', 'Повар'],
                       ['Андрей', 'Сергей', 'Николай']]
                   }

boolz = False
number = 1


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
        verticalLayoutWidget.setGeometry(QRect(930, 260, 160, 100))
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        verticalLayout = QVBoxLayout(verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        FirstTask = QPushButton(verticalLayoutWidget)
        FirstTask.setObjectName("FirstTask")
        FirstTask.clicked.connect(lambda: mainwindow.First())
        verticalLayout.addWidget(FirstTask)
        ChooseTask = QPushButton(verticalLayoutWidget)
        ChooseTask.setObjectName("ChooseTask")
        verticalLayout.addWidget(ChooseTask)
        NewTask = QPushButton(verticalLayoutWidget)
        NewTask.setObjectName("NewTask")
        verticalLayout.addWidget(NewTask)
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
        rows = len(ColsAndRowsName[number][1]) + 1
        cols = len(ColsAndRowsName[number][0]) + 1

    def gameplay(self, mainwindow):
        if self.number <= len(variants):
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
            self.listView.addItem(str(variants[self.number]))

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
                        self.cell_h.setText(ColsAndRowsName[self.number][0][j - 1])
                        self.gridLayout.addWidget(self.cell_h, i, j, 1, 1)
                    else:
                        if j == 0 and i != 0:
                            self.cell_v.setText(ColsAndRowsName[self.number][1][i - 1])
                            self.gridLayout.addWidget(self.cell_v, i, j, 1, 1)
                        elif i != 0 and j != 0:
                            self.gridLayout.addWidget(self.pushButton, i, j, 1, 1)

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
        if boolz == True and lists == answer[self.number]:
            self.number += 1
            self.listView.clear()
            self.listView.addItem(str(variants[self.number]))
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
        window1 = MainMenu(self)
        self.stack.addWidget(window1)
        self.stack.addWidget(self.window2)
        self.stack.setCurrentIndex(0)

        self.setCentralWidget(self.Widget)
        self.layout = QVBoxLayout(self.Widget)
        self.layout.addWidget(self.stack)

    def back(self):
        self.stack.setCurrentIndex(0)
        self.flag = True

    def First(self):
        self.flag = False
        self.window2.deleteLater()
        self.window2 = Ui_MainWindow(self)
        self.stack.addWidget(self.window2)
        self.stack.setCurrentIndex(1)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
