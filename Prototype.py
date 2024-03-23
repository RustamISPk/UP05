from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMetaObject
from PyQt5.QtWidgets import QGridLayout, QWidget, QListView, QMenuBar, QStatusBar, QMainWindow, QApplication, \
    QPushButton, QListWidget, QLabel, QStackedWidget, QVBoxLayout, QHBoxLayout

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


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Помощник решения логических задач")
        self.cell_v = None
        self.pushButton = None
        self.cell_h = None
        self.width = QApplication.desktop().width()
        self.height = QApplication.desktop().height()
        self.setObjectName("MainWindow")
        self.resize(self.width, self.height)
        self.number = 1
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.centrallayout = QVBoxLayout(self.centralwidget)
        self.clearfild()
        self.gameplay()

    def clearfild(self):
        print(self.centrallayout.count())
        index = self.centrallayout.count()
        while index > 0:
            item = self.centrallayout.itemAt(index)
            self.centrallayout.removeItem(item)

    def menu(self):
        self.clearfild()
        print('menu')

    def rows_cols_number(self, number):
        global rows, cols
        rows = len(ColsAndRowsName[number][1]) + 1
        cols = len(ColsAndRowsName[number][0]) + 1

    def gameplay(self):
        self.rows_cols_number(self.number)

        gamefield = []
        for i in range(rows - 1):
            col_list = []
            for j in range(cols - 1):
                col_list.append(' ')
            gamefield.append(col_list)

        self.taskLayout = QHBoxLayout()
        self.listView = QLabel()
        # self.listView.setGeometry(QtCore.QRect(int((self.width - 1000) / 2), 40, 1000, 200))
        self.listView.move(int((self.width - 1000) / 2), 0)
        self.listView.setMaximumSize(1000, 200)
        self.listView.setStyleSheet('background: #fff')
        self.listView.setObjectName("listView")
        self.listView.setText(str(variants[self.number]))
        self.taskLayout.addWidget(self.listView)
        self.btn = QPushButton()
        self.btn.setText('menu')
        self.btn.setMinimumSize(100, 50)
        self.btn.clicked.connect(lambda: self.menu())
        self.taskLayout.addWidget(self.btn)
        self.centrallayout.addLayout(self.taskLayout)

        self.solutionLayout = QHBoxLayout()
        self.gridLayoutWidget = QWidget()
        # self.gridLayoutWidget.setGeometry(QtCore.QRect(int((self.width - 87 * cols) / 2), 300, 87 * cols, 87 * rows))
        self.gridLayoutWidget.setMaximumSize(87 * cols, 87 * rows)
        self.gridLayoutWidget.move(int((self.width - 87 * cols) / 2), 300)
        self.gridLayoutWidget.setStyleSheet('background: #fff')
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.solutionLayout.addWidget(self.gridLayoutWidget)
        self.centrallayout.addLayout(self.solutionLayout)

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
                    lambda cheked, button=self.pushButton: self.add_value(button, gamefield))

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

        self.setCentralWidget(self.centralwidget)
        # self.menubar = QMenuBar()
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        # self.menubar.setObjectName("menubar")
        # self.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar()
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)

        # self.retranslateUi()
        # QMetaObject.connectSlotsByName()

    def add_value(self, button, lists):
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
            return self.gameplay()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
