from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QGridLayout, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit
from MainRegime import MainRegime


class ChoiseWindow(QMainWindow):

    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(725, 10, 470, 101))
        self.amounttask = QLabel(self.centralwidget)
        self.amounttask.setGeometry(QtCore.QRect(1600, 10, 300, 50))
        self.amounttask.setText(f'Количество задач: {len(mainwindow.variants) - 1}')
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText('Введите номер задачи в поле')
        self.label.setStyleSheet("font: 20pt Times New Roman")
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(460, 100, 1000, 50))
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
        mainwindow.number = int(self.TaskEdit.text())
        if mainwindow.number < len(mainwindow.variants):
            mainwindow.window2.deleteLater()
            mainwindow.window2 = MainRegime(mainwindow)
            mainwindow.stack.addWidget(mainwindow.window2)
            mainwindow.stack.setCurrentWidget(mainwindow.window2)
            self.TaskEdit.clear()
