from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QGridLayout, QWidget, QMainWindow, QPushButton, QLabel, \
    QStackedWidget, QTextEdit, QLineEdit
from PyQt5.QtGui import QTextCursor
import json


class AddTask(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.TaskCols = None
        self.TaskRows = None
        self.TaskText = None
        self.boolz = None
        self.table = None
        self.table_elements = None
        self.new_answer = None
        self.secondwidget = None
        self.cols = None
        self.rows = None
        self.password = 'Admin'
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        self.mainwidget = QStackedWidget()
        self.setCentralWidget(self.mainwidget)

        self.firstwidget = QWidget()
        self.firstwidget.setObjectName("centralwidget")

        self.PasswordLable = QLineEdit(self.firstwidget)
        self.PasswordLable.setGeometry(QtCore.QRect(0, 85, 200, 75))
        self.PasswordLable.setEchoMode(QLineEdit.Password)
        self.PasswordButton = QPushButton(self.firstwidget)
        self.PasswordButton.setGeometry(QtCore.QRect(0, 0, 200, 75))
        self.PasswordButton.setText('Введите пароль')
        self.PasswordButton.clicked.connect(lambda: self.inputPassword())

        self.Instruction = QLabel(self.firstwidget)
        self.Instruction.setGeometry(QtCore.QRect(1300, 0, 500, 300))
        self.Instruction.setObjectName("label")
        self.Instruction.setText("Режим добавления задачи предназначен\n"
                                 "только для учителей. Введите пароль,\nчтобы продолжить добавление.\n"
                                 "При добавлении новой задачи, размер таблицы\n"
                                 "не должен превышать размер 7х14."
                                 "\nПеред тем как сгенерировать таблицу,\nубедитесь, "
                                 "что поля для текста задачи\nи размеров таблицы заполнены\n"
                                 "")
        self.Instruction.setTextFormat(Qt.RichText)
        self.Instruction.setWordWrap(True)
        self.Instruction.setAlignment(Qt.AlignJustify)
        self.Instruction.setStyleSheet("font: 15pt Times New Roman")

        self.TaskText = QTextEdit(self.firstwidget)
        self.TaskText.setGeometry(QtCore.QRect(730, 260, 511, 191))
        self.TaskText.setObjectName("TaskText")
        self.TaskText.setEnabled(False)

        self.TaskRowsText = QLabel(self.firstwidget)
        self.TaskRowsText.setGeometry(QtCore.QRect(730, 470, 200, 35))
        self.TaskRowsText.setObjectName("TaskRowsText")
        self.TaskRowsText.setText('Введите количество строк')
        self.TaskRowsText.setStyleSheet('font: 10pt Times New Roman')

        self.TaskRows = QLineEdit(self.firstwidget)
        self.TaskRows.setGeometry(QtCore.QRect(950, 470, 100, 35))
        self.TaskRows.setObjectName("TaskRows")
        self.TaskRows.setValidator(QIntValidator(1, 7, self))
        self.TaskRows.setEnabled(False)

        self.TaskColsText = QLabel(self.firstwidget)
        self.TaskColsText.setGeometry(QtCore.QRect(730, 510, 200, 35))
        self.TaskColsText.setObjectName("TaskColsText")
        self.TaskColsText.setText('Введите количество колон')
        self.TaskColsText.setStyleSheet('font: 10pt Times New Roman')

        self.TaskCols = QLineEdit(self.firstwidget)
        self.TaskCols.setGeometry(QtCore.QRect(950, 510, 100, 35))
        self.TaskCols.setObjectName("TaskCols")
        self.TaskCols.setValidator(QIntValidator(1, 14, self))
        self.TaskCols.setEnabled(False)

        self.NextButton = QPushButton(self.firstwidget)
        self.NextButton.setGeometry(QtCore.QRect(730, 560, 511, 70))
        self.NextButton.setText('Сгенерировать таблицу\n для ввода ответа')
        self.NextButton.clicked.connect(lambda: self.tableGen(mainwindow))
        self.NextButton.setEnabled(False)

        self.BackButton = QPushButton(self.firstwidget)
        self.BackButton.setGeometry(QtCore.QRect(1630, 340, 201, 41))
        self.BackButton.setObjectName("pushButton")
        self.BackButton.setText('Назад')
        self.BackButton.clicked.connect(lambda: self.backToMainwindow(mainwindow))

        self.secondwidget = QWidget()

        self.mainwidget.addWidget(self.firstwidget)
        self.mainwidget.setCurrentWidget(self.firstwidget)

    def backToMainwindow(self, mainwindow):
        mainwindow.back()
        self.TaskText.setEnabled(False)
        self.TaskRows.setEnabled(False)
        self.TaskCols.setEnabled(False)
        self.NextButton.setEnabled(False)
        self.PasswordLable.show()
        self.PasswordButton.show()
        self.PasswordLable.clear()
        self.TaskText.clear()
        self.TaskCols.clear()
        self.TaskRows.clear()

    def inputPassword(self):
        userword = self.PasswordLable.text()
        if userword == self.password:
            self.TaskText.setEnabled(True)
            self.TaskRows.setEnabled(True)
            self.TaskCols.setEnabled(True)
            self.NextButton.setEnabled(True)
            self.PasswordLable.hide()
            self.PasswordButton.hide()

    def tableGen(self, mainwindow):
        if self.TaskText.toPlainText() and self.TaskText.toPlainText() != f'Задание №{len(mainwindow.variants)}.' and self.TaskRows.text() and int(
                self.TaskRows.text()) != 0 and self.TaskCols.text() and int(self.TaskCols.text()) != 0 \
                and int(self.TaskRows.text()) <= 7 and int(self.TaskCols.text()) <= 14 and len(
            self.TaskText.toPlainText()) <= 600:

            text = self.TaskText.toPlainText()
            check = text.find(f'Задание №{len(mainwindow.variants)}.')

            if check == -1:
                cursor = QTextCursor(self.TaskText.document())
                cursor.setPosition(0)
                self.TaskText.setTextCursor(cursor)
                self.TaskText.insertPlainText(f'Задание №{len(mainwindow.variants)}.')

            self.secondInstruction = QLabel(self.secondwidget)
            self.secondInstruction.setGeometry(1500, 100, 400, 100)
            self.secondInstruction.setText("Введите правильный ответ в таблицу\n"
                                           "и подпишите названия строк и колон")
            self.secondInstruction.setTextFormat(Qt.RichText)
            self.secondInstruction.setWordWrap(True)
            self.secondInstruction.setAlignment(Qt.AlignJustify)
            self.secondInstruction.setStyleSheet("font: 15pt Times New Roman")

            self.backbutton = QPushButton(self.secondwidget)
            self.backbutton.setGeometry(QtCore.QRect(1630, 400, 201, 41))
            self.backbutton.setText('Назад')
            self.backbutton.clicked.connect(lambda: self.back(mainwindow))

            self.table = [[], []]
            NewTaskText = self.TaskText.setPlainText
            self.rows = int(self.TaskRows.text()) + 1
            self.cols = int(self.TaskCols.text()) + 1
            self.table_elements = [[], []]

            self.new_answer = []
            for i in range(self.rows - 1):
                col_new_answer = []
                for j in range(self.cols - 1):
                    col_new_answer.append(' ')
                self.new_answer.append(col_new_answer)

            if self.rows > 0 and self.cols > 0 and NewTaskText != ' ':

                self.TableWidget = QWidget(self.secondwidget)
                self.TableWidget.setGeometry(
                    QtCore.QRect(int((1920 - 87 * self.cols) / 2), 300, 87 * self.cols, 87 * self.rows))
                self.TableWidget.setObjectName("gridLayoutWidget")

                self.TableLayout = QGridLayout(self.TableWidget)
                self.TableLayout.setContentsMargins(0, 0, 0, 0)
                self.TableLayout.setObjectName("gridLayout")

                self.SaveButton = QPushButton(self.secondwidget)
                self.SaveButton.setGeometry(QtCore.QRect(1630, 340, 201, 41))
                self.SaveButton.setText("Сохранить задание")
                self.SaveButton.clicked.connect(lambda: self.saveTask(mainwindow))

                self.TaskTextLabel = QLabel(self.secondwidget)
                self.TaskTextLabel.setText(self.TaskText.toPlainText())
                self.TaskTextLabel.setGeometry(QtCore.QRect(int((1920 - 1000) / 2), 40, 1000, 200))
                self.TaskTextLabel.setTextFormat(Qt.RichText)
                self.TaskTextLabel.setWordWrap(True)
                self.TaskTextLabel.setAlignment(Qt.AlignJustify)
                self.TaskTextLabel.setStyleSheet("font: 15pt Times New Roman")

                for i in range(self.rows):
                    for j in range(self.cols):

                        self.TableButton = QPushButton()
                        self.TableButton.setStyleSheet('background-color: yellow')
                        self.TableButton.setMinimumSize(75, 75)
                        self.TableButton.setMaximumSize(75, 75)
                        self.TableButton.setObjectName(f'{i}')
                        self.TableButton.setAccessibleName(f'{j}')
                        self.TableButton.clicked.connect(
                            lambda cheked, button=self.TableButton: self.newAnswer(button))

                        self.RowName = QLineEdit()
                        self.RowName.setMinimumSize(75, 30)
                        self.RowName.setMaximumSize(75, 30)
                        self.RowName.setObjectName(f'{i}{j}')
                        self.RowName.setStyleSheet('border: 1px solid #000')
                        self.RowName.setText('')

                        self.ColName = QLineEdit()
                        self.ColName.setMinimumSize(75, 30)
                        self.ColName.setMaximumSize(75, 30)
                        self.ColName.setObjectName(f'{i}')
                        self.ColName.setStyleSheet('border: 1px solid #000')
                        self.ColName.setText('')

                        if i == 0 and j != 0:
                            self.table[0].append(self.RowName)
                            self.TableLayout.addWidget(self.RowName, i, j, 1, 1)
                        else:
                            if j == 0 and i != 0:
                                self.table[1].append(self.ColName)
                                self.TableLayout.addWidget(self.ColName, i, j, 1, 1)
                            elif i != 0 and j != 0:
                                self.TableLayout.addWidget(self.TableButton, i, j, 1, 1)
                self.mainwidget.addWidget(self.secondwidget)
                self.mainwidget.setCurrentWidget(self.secondwidget)

    def newAnswer(self, button):

        i = int(button.objectName()) - 1
        j = int(button.accessibleName()) - 1
        if self.new_answer[i][j] == ' ':
            self.new_answer[i][j] = '+'
            button.setStyleSheet('background-color: lime')
        elif self.new_answer[i][j] == '-':
            self.new_answer[i][j] = '+'
            button.setStyleSheet('background-color: lime')
        elif self.new_answer[i][j] == '+':
            self.new_answer[i][j] = '-'
            button.setStyleSheet('background-color: red')
        button.setText(f'{self.new_answer[i][j]}')

        count = 0

        for a in range(self.rows - 1):
            for b in range(self.cols - 1):
                if self.new_answer[a][b] == ' ':
                    count += 1

        if count == 0:
            self.boolz = True
        else:
            self.boolz = False

    def saveTask(self, mainwindow):
        cellhcheck = False
        cellvcheck = False

        for self.RowName in self.table[0]:
            if self.RowName.text() != '':
                cellhcheck = True
            else:
                cellhcheck = False
                break

        for self.ColName in self.table[1]:
            if self.ColName.text() != '':
                cellvcheck = True
            else:
                cellvcheck = False
                break

        if cellvcheck == True and cellhcheck == True and self.boolz == True:
            for self.RowName in self.table[0]:
                if len(self.table_elements[0]) < self.rows and self.RowName.text() != '':
                    self.table_elements[0].append(self.RowName.text())
            for self.ColName in self.table[1]:
                if len(self.table_elements[1]) < self.cols and self.ColName.text() != '':
                    self.table_elements[1].append(self.ColName.text())

            mainwindow.variants[str(len(mainwindow.variants))] = self.TaskText.toPlainText()
            mainwindow.variants[str(len(mainwindow.variants) + 1)] = " "

            mainwindow.answer[str(len(mainwindow.answer))] = self.new_answer
            mainwindow.answer[str(len(mainwindow.answer) + 1)] = " "

            mainwindow.ColsAndRowsName[str(len(mainwindow.ColsAndRowsName))] = self.table_elements
            mainwindow.ColsAndRowsName[str(len(mainwindow.ColsAndRowsName) + 1)] = " "

            with open('ColsAndRowsName.json', 'w', encoding='utf-8') as fh:
                fh.write(json.dumps(mainwindow.ColsAndRowsName, ensure_ascii=False))

            with open('variants.json', 'w', encoding='utf-8') as fh:
                fh.write(json.dumps(mainwindow.variants, ensure_ascii=False))

            with open('answers.json', 'w', encoding='utf-8') as fh:
                fh.write(json.dumps(mainwindow.answer, ensure_ascii=False))

            with open('variants.json', 'r', encoding='utf-8') as fh:
                mainwindow.variants = json.load(fh)

            with open('answers.json', 'r', encoding='utf-8') as fh:
                mainwindow.answer = json.load(fh)

            with open('ColsAndRowsName.json', 'r', encoding='utf-8') as fh:
                mainwindow.ColsAndRowsName = json.load(fh)

            self.mainwidget.setCurrentWidget(self.firstwidget)
            self.secondwidget.deleteLater()
            self.secondwidget = QWidget()
            self.mainwidget.addWidget(self.secondwidget)
            self.TaskCols.clear()
            self.TaskRows.clear()
            self.TaskText.clear()
            self.TaskText.append(f'Задание №{len(mainwindow.variants)}.')

    def back(self, mainwindow):
        self.mainwidget.setCurrentWidget(self.firstwidget)
        self.secondwidget.deleteLater()
        self.secondwidget = QWidget()
        self.mainwidget.addWidget(self.secondwidget)
        self.TaskCols.clear()
        self.TaskRows.clear()
        self.TaskText.clear()
        self.TaskText.append(f'Задание №{len(mainwindow.variants)}.')
