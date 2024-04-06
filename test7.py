import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QGridLayout



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Привет")
        self.setGeometry(0, 0, 1920, 1080)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.widget = CustomWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.central_widget.setLayout(layout)


class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.gridLayoutWidget = QWidget()
        self.gridLayoutWidget.setGeometry(500, 300, 800, 800)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        for i in range(4):
            for j in range(4):
                self.pushButton = QPushButton()
                self.pushButton.setStyleSheet('background-color: yellow')
                self.pushButton.setMinimumSize(75, 75)
                self.pushButton.setMaximumSize(75, 75)
                self.pushButton.setText(f'{i}_{j}')
                self.pushButton.setObjectName(f'{i}')
                self.pushButton.setAccessibleName(f'{j}')
                self.gridLayout.addWidget(self.pushButton)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
