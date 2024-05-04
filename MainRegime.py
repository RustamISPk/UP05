from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QWidget, QMainWindow, QApplication, QPushButton, QLabel


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
        self.number = mainwindow.number
        self.gameplay(mainwindow)

    def rows_cols_number(self, number, mainwindow):
        global rows, cols
        rows = len(mainwindow.ColsAndRowsName[str(number)][1]) + 1
        cols = len(mainwindow.ColsAndRowsName[str(number)][0]) + 1

    def gameplay(self, mainwindow):
        if self.number < len(mainwindow.variants):
            self.rows_cols_number(self.number, mainwindow)

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

            self.listView = QLabel(self.centralwidget)
            self.listView.setGeometry(QtCore.QRect(int((self.width - 1000) / 2), 40, 1000, 200))
            self.listView.setObjectName("listView")
            self.listView.setText(str(mainwindow.variants[str(self.number)]))
            self.listView.setAlignment(Qt.AlignJustify)
            self.listView.setStyleSheet("font: 12pt Times New Roman")
            self.listView.setTextFormat(Qt.RichText)
            self.listView.setWordWrap(True)

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
                    # self.cell_h.setStyleSheet('font: 12pt Times New Roman')
                    self.cell_h.setAlignment(Qt.AlignCenter)

                    self.cell_v = QLabel()
                    self.cell_v.setMinimumSize(75, 30)
                    self.cell_v.setMaximumSize(75, 30)
                    self.cell_v.setObjectName(f'{i}{j}')
                    self.cell_v.setStyleSheet('border: 1px solid #000')
                    self.cell_v.setAlignment(Qt.AlignCenter)

                    if i == 0 and j != 0:
                        self.cell_h.setText(mainwindow.ColsAndRowsName[str(self.number)][0][j - 1])
                        self.gridLayout.addWidget(self.cell_h, i, j, 1, 1)
                    else:
                        if j == 0 and i != 0:
                            self.cell_v.setText(mainwindow.ColsAndRowsName[str(self.number)][1][i - 1])
                            self.gridLayout.addWidget(self.cell_v, i, j, 1, 1)
                        elif i != 0 and j != 0:
                            self.gridLayout.addWidget(self.pushButton, i, j, 1, 1)

            self.setCentralWidget(self.centralwidget)
        else:
            mainwindow.stack.setCurrentIndex(0)

    def add_value(self, button, lists, mainwindow):
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
            mainwindow.boolz = True
        else:
            mainwindow.boolz = False
        if mainwindow.boolz == True and lists == mainwindow.answer[str(self.number)]:
            self.number += 1
            self.listView.clear()
            self.listView.setText(str(mainwindow.variants[str(self.number)]))
            return self.gameplay(mainwindow)