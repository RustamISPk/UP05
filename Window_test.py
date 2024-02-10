from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMetaObject
from PyQt5.QtWidgets import QGridLayout, QWidget, QListView, QMenuBar, QStatusBar, QMainWindow, QApplication, \
    QPushButton

rows = 4
cols = 4

answer = {1: [['-', '-', '-', '+'],
              ['-', '+', '-', '-'],
              ['+', '-', '-', '-'],
              ['-', '-', '+', '-']],
          2: [['+', '-', '-', '-'],
              ['-', '+', '-', '-'],
              ['+', '-', '-', '-'],
              ['-', '-', '+', '-']]
          }

gamefield = [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(180, 10, 901, 281))
        self.listView.setObjectName("listView")

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
                self.pushButton.clicked.connect(lambda cheked, button=self.pushButton: self.add_value(button, gamefield))
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

    def add_value(self, button, list):
        i = int(button.objectName())
        j = int(button.accessibleName())
        if list[i][j] == '-':
            list[i][j] = '+'
            button.setStyleSheet('background-color: green')
        elif list[i][j] == '+':
            list[i][j] = '-'
            button.setStyleSheet('background-color: red')
        button.setText(f'{list[i][j]}')

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
