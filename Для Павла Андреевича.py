from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMetaObject, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QWidget, QListView, QMenuBar, QStatusBar, QMainWindow, QApplication, \
    QPushButton, QListWidget, QLabel, QVBoxLayout, QStackedWidget

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

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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


class MainRegime(QWidget):
    def __init__(self):
        super().__init__()
        self.listView = None
        self.cell_v = None
        self.pushButton = None
        self.cell_h = None
        self.width = QApplication.desktop().width()
        self.height = QApplication.desktop().height()
        self.number = 1
        self.setupUi(self)

    def setupUi(self, MainRegime):
        MainRegime.resize(self.width, self.height)

        self.gameplay(self.number)

    def gameplay(self, number):
        self.rows_cols_number(number)

        gamefield = []
        for i in range(rows - 1):
            col_list = []
            for j in range(cols - 1):
                col_list.append(' ')
            gamefield.append(col_list)

        centralwidget = QWidget(self)
        centralwidget.setObjectName("centralwidget")
        listView = QLabel(self)
        listView.setGeometry(QtCore.QRect(int((self.width-1000)/2), 40, 1000, 200))
        listView.setObjectName("listView")
        listView.setText(str(variants[number]))

        gridLayoutWidget = QWidget(self)
        gridLayoutWidget.setGeometry(QtCore.QRect(int((self.width-87*cols)/2), 300, 87*cols, 87*rows))
        gridLayoutWidget.setObjectName("gridLayoutWidget")

        gridLayout = QGridLayout(gridLayoutWidget)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setObjectName("gridLayout")

        for i in range(rows):
            for j in range(cols):
                if (i != 0 and j != 0):
                    self.pushButton = QPushButton()
                    self.pushButton.setStyleSheet('background-color: yellow')
                    self.pushButton.setMinimumSize(75, 75)
                    self.pushButton.setMaximumSize(75, 75)
                    self.pushButton.setText(f'{i}_{j}')
                    self.pushButton.setObjectName(f'{i}')
                    self.pushButton.setAccessibleName(f'{j}')
                    self.pushButton.clicked.connect(
                        lambda cheked, button=self.pushButton: self.add_value(button, gamefield, listView, number))
                    gridLayout.addWidget(self.pushButton, i, j, 1, 1)
                if i == 0 and j != 0:
                    cell_h = QLabel(self)
                    cell_h.setMinimumSize(75, 30)
                    cell_h.setMaximumSize(75, 30)
                    cell_h.setObjectName(f'{i}{j}')
                    cell_h.setStyleSheet('border: 1px solid #000')
                    cell_h.setText(ColsAndRowsName[number][0][j - 1])
                    gridLayout.addWidget(cell_h, i, j, 1, 1)

                if j == 0 and i != 0:
                    cell_v = QLabel()
                    cell_v.setMinimumSize(75, 30)
                    cell_v.setMaximumSize(75, 30)
                    cell_v.setObjectName(f'{i}{j}')
                    cell_v.setStyleSheet('border: 1px solid #000')
                    cell_v.setText(ColsAndRowsName[number][1][i - 1])
                    gridLayout.addWidget(cell_v, i, j, 1, 1)

                # if i == 0 and j != 0:
                #     cell_h.setText(ColsAndRowsName[self.number][0][j - 1])
                #     gridLayout.addWidget(cell_h, i, j, 1, 1)
                # else:
                #     if j == 0 and i != 0:
                #         cell_v.setText(ColsAndRowsName[self.number][1][i - 1])
                #         gridLayout.addWidget(cell_v, i, j, 1, 1)
                    # elif i != 0 and j != 0:
                    #     gridLayout.addWidget(pushButton, i, j, 1, 1)

    def add_value(self, button, lists, listView, number):
        global boolz, answer, variants
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
        if boolz == True and lists == answer[number]:
            number += 1
            listView.clear()
            listView.setText(str(variants[number]))
            return self.gameplay(number)

    def rows_cols_number(self, number):
        global rows, cols
        rows = len(ColsAndRowsName[number][1]) + 1
        cols = len(ColsAndRowsName[number][0]) + 1

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cell_v = None
        self.pushButton = None
        self.cell_h = None
        self.width = QApplication.desktop().width()
        self.height = QApplication.desktop().height()
        mainwidget = MainRegime()
        Win = QStackedWidget()
        Win.addWidget(mainwidget)
        Win.setCurrentIndex(0)
        self.setCentralWidget(Win)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.width, self.height)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())