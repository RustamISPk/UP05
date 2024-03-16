from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMetaObject
from PyQt5.QtWidgets import QGridLayout, QWidget, QListView, QMenuBar, QStatusBar, QMainWindow, QApplication, \
    QPushButton, QListWidget

rows = 4
cols = 4
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
            }
answer = {1: [['-', '-', '-', '+'],
              ['-', '+', '-', '-'],
              ['+', '-', '-', '-'],
              ['-', '-', '+', '-']],
          2: [['+', '-', '-', '-'],
              ['-', '+', '-', '-'],
              ['+', '-', '-', '-'],
              ['-', '-', '+', '-']]
          }

boolz = False


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.number = 1
        self.gameplay()

    def gameplay(self):

        gamefield = [[' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ']]

        #result = False



        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(180, 10, 901, 281))
        self.listView.setObjectName("listView")
        self.listView.addItem(str(variants[self.number]))

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(420, 350, 250, 250))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        for i in range(rows):
            for j in range(cols):
                self.pushButton = QPushButton()
                self.pushButton.setStyleSheet('background-color: yellow')
                self.pushButton.setMinimumSize(50, 50)
                self.pushButton.setMaximumSize(50, 50)
                self.pushButton.setText(f'[ ]')
                self.pushButton.setObjectName(f'{i}')
                self.pushButton.setAccessibleName(f'{j}')
                self.pushButton.clicked.connect(
                    lambda cheked, button=self.pushButton: self.add_value(button, gamefield))
                self.gridLayout.addWidget(self.pushButton, i, j, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)



    def add_value(self, button, lists):
        global boolz
        i = int(button.objectName())
        j = int(button.accessibleName())

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
        for i in range(rows):
             for j in range(cols):
                 if lists[i][j] == ' ':
                     count += 1
        if count == 0:
            boolz = True
            #print(boolz)
        else:
            boolz = False
            #print(boolz)
        if boolz == True and lists == answer[self.number]:
            result = True
            self.number += 1
            #print('OK')
            self.listView.clear()
            self.listView.addItem(str(variants[self.number]))
            return self.gameplay()
            # return lists, boolz

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())