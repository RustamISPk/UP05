from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout


class MainMenu(QMainWindow):

    def __init__(self, mainwindow):
        super().__init__()
        self.initUI(mainwindow)

    def initUI(self, mainwindow):
        label = QLabel(self)
        label.setGeometry(QRect(691, 40, 538, 111))
        label.setAlignment(Qt.AlignCenter)
        label.setText("Помощник решения логических задач")
        label.setStyleSheet("font: 20pt Times New Roman")
        verticalLayoutWidget = QWidget(self)
        verticalLayoutWidget.setGeometry(QRect(880, 260, 160, 250))
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        verticalLayout = QVBoxLayout(verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        verticalLayout.setAlignment(Qt.AlignCenter)
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
        FirstTask.setText(f"Начать с первой\nзадачи")
        ChooseTask.setText("Выбрать\nзадачу")
        NewTask.setText("Добавить\nзадачу")