from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QStackedWidget, QVBoxLayout
from qt_material import apply_stylesheet
import json
from AddTask import AddTask
from ChoiseWindow import ChoiseWindow
from MainMenu import MainMenu
from MainRegime import MainRegime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Widget = None
        self.window4 = None
        self.window3 = None
        self.window2 = None
        self.window1 = None
        self.ColsAndRowsName = None
        self.answer = None
        self.variants = None
        self.stack = None
        self.flag = False
        self.number = 1
        self.boolz = False
        self.rows, self.cols = 0, 0
        self.UIinit()

    def UIinit(self):
        self.Widget = QWidget()
        self.stack = QStackedWidget()

        self.setWindowTitle("Помощник решения логических задач")

        with open('variants.json', 'r', encoding='utf-8') as fh:
            self.variants = json.load(fh)

        with open('answers.json', 'r', encoding='utf-8') as fh:
            self.answer = json.load(fh)

        with open('ColsAndRowsName.json', 'r', encoding='utf-8') as fh:
            self.ColsAndRowsName = json.load(fh)

        self.window1 = MainMenu(self)
        self.window2 = MainRegime(self)
        self.window3 = ChoiseWindow(self)
        self.window4 = AddTask(self)

        self.stack.addWidget(self.window1)
        self.stack.addWidget(self.window2)
        self.stack.addWidget(self.window3)
        self.stack.addWidget(self.window4)
        self.stack.setCurrentWidget(self.window1)

        self.setCentralWidget(self.Widget)
        self.layout = QVBoxLayout(self.Widget)
        self.layout.addWidget(self.stack)

    def back(self):
        self.stack.setCurrentWidget(self.window1)
        self.window3.TaskEdit.clear()

    def First(self):
        self.number = 1
        self.window2.deleteLater()
        self.window2 = MainRegime(self)
        self.stack.addWidget(self.window2)
        self.stack.setCurrentWidget(self.window2)

    def Choice(self):
        self.stack.setCurrentWidget(self.window3)
        self.window3.amounttask.setText(f'Количество задач: {len(self.variants) - 1}')

    def AddTask(self):
        self.window4.TaskText.append(f'Задание №{len(self.variants)}.')
        self.stack.setCurrentWidget(self.window4)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(1920, 1080)
    apply_stylesheet(app, theme='dark_purple.xml')
    window.showMaximized()
    sys.exit(app.exec_())
