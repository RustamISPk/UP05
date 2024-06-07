from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QWidget, QMainWindow, QApplication, QPushButton, QLabel


class MainRegime(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.TableLayout = None
        self.TableWidget = None
        self.TaskLabel = None
        self.centralwidget = None
        self.number = None
        self.BackButton = None
        self.TableLabel_v = None
        self.TableButton = None
        self.TableLabel_h = None
        self.width = QApplication.desktop().width()
        self.height = QApplication.desktop().height()
        self.setupUi(self, mainwindow)

    def setupUi(self, MainWindow, mainwindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.width, self.height)
        self.number = mainwindow.number
        self.gameplay(mainwindow)

    def rows_cols_number(self, number, mainwindow):
        mainwindow.rows = len(mainwindow.ColsAndRowsName[str(number)][1]) + 1
        mainwindow.cols = len(mainwindow.ColsAndRowsName[str(number)][0]) + 1

    def gameplay(self, mainwindow):
        if self.number < len(mainwindow.variants):
            self.rows_cols_number(self.number, mainwindow)

            gamefield = []
            for i in range(mainwindow.rows - 1):
                col_list = []
                for j in range(mainwindow.cols - 1):
                    col_list.append(' ')
                gamefield.append(col_list)

            self.centralwidget = QWidget()
            self.centralwidget.setObjectName("centralwidget")

            self.BackButton = QPushButton(self.centralwidget)
            self.BackButton.setText('Назад')
            self.BackButton.setGeometry(0, 0, 100, 50)
            self.BackButton.clicked.connect(lambda: mainwindow.back())

            self.TaskLabel = QLabel(self.centralwidget)
            self.TaskLabel.setGeometry(QtCore.QRect(int((self.width - 1000) / 2), 40, 1000, 200))
            self.TaskLabel.setObjectName("listView")
            self.TaskLabel.setText(str(mainwindow.variants[str(self.number)]))
            self.TaskLabel.setAlignment(Qt.AlignJustify)
            self.TaskLabel.setStyleSheet("font: 12pt Times New Roman")
            self.TaskLabel.setTextFormat(Qt.RichText)
            self.TaskLabel.setWordWrap(True)

            self.TableWidget = QWidget(self.centralwidget)
            self.TableWidget.setGeometry(
                QtCore.QRect(int((self.width - 87 * mainwindow.cols) / 2), 300, 87 * mainwindow.cols, 87 * mainwindow.rows))
            self.TableWidget.setObjectName("gridLayoutWidget")

            self.TableLayout = QGridLayout(self.TableWidget)
            self.TableLayout.setContentsMargins(0, 0, 0, 0)
            self.TableLayout.setObjectName("gridLayout")

            for i in range(mainwindow.rows):
                for j in range(mainwindow.cols):
                    self.TableButton = QPushButton()
                    self.TableButton.setStyleSheet('background-color: yellow')
                    self.TableButton.setMinimumSize(75, 75)
                    self.TableButton.setMaximumSize(75, 75)
                    self.TableButton.setObjectName(f'{i}')
                    self.TableButton.setAccessibleName(f'{j}')
                    self.TableButton.clicked.connect(
                        lambda cheked, button=self.TableButton: self.add_value(button, gamefield, mainwindow))

                    self.TableLabel_h = QLabel()
                    self.TableLabel_h.setMinimumSize(75, 30)
                    self.TableLabel_h.setMaximumSize(75, 30)
                    self.TableLabel_h.setObjectName(f'{i}{j}')
                    self.TableLabel_h.setStyleSheet('border: 1px solid #000')
                    self.TableLabel_h.setAlignment(Qt.AlignCenter)

                    self.TableLabel_v = QLabel()
                    self.TableLabel_v.setMinimumSize(75, 30)
                    self.TableLabel_v.setMaximumSize(75, 30)
                    self.TableLabel_v.setObjectName(f'{i}{j}')
                    self.TableLabel_v.setStyleSheet('border: 1px solid #000')
                    self.TableLabel_v.setAlignment(Qt.AlignCenter)

                    if i == 0 and j != 0:
                        self.TableLabel_h.setText(mainwindow.ColsAndRowsName[str(self.number)][0][j - 1])
                        self.TableLayout.addWidget(self.TableLabel_h, i, j, 1, 1)
                    else:
                        if j == 0 and i != 0:
                            self.TableLabel_v.setText(mainwindow.ColsAndRowsName[str(self.number)][1][i - 1])
                            self.TableLayout.addWidget(self.TableLabel_v, i, j, 1, 1)
                        elif i != 0 and j != 0:
                            self.TableLayout.addWidget(self.TableButton, i, j, 1, 1)

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
        for a in range(mainwindow.rows - 1):
            for b in range(mainwindow.cols - 1):
                if lists[a][b] == ' ':
                    count += 1
        if count == 0:
            mainwindow.answer_check = True
        else:
            mainwindow.answer_check = False
        if mainwindow.answer_check == True and lists == mainwindow.answer[str(self.number)]:
            self.number += 1
            self.TaskLabel.clear()
            self.TaskLabel.setText(str(mainwindow.variants[str(self.number)]))
            return self.gameplay(mainwindow)