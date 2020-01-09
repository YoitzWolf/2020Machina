from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class ErrorDialogue(QtWidgets.QDialog):

    def __init__(self, parent, err):
        super(ErrorDialogue, self).__init__(parent)
        self.label = QtWidgets.QLabel()
        self.setWindowTitle("ERROR")
        self.setWindowIcon(QtGui.QIcon("visual/images/No.svg"))
        self.setFixedHeight(150)
        self.lay = QtWidgets.QHBoxLayout()
        self.label.setText(err)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.lay.addWidget(self.label)
        self.setLayout(self.lay)
        self.setStyleSheet(
            "background-color: #FFF; font-family:Roboto; font-weight: bold; font-size: 12pt;")


class HelpDialogue(QtWidgets.QDialog):

    def __init__(self, parent):
        super(HelpDialogue, self).__init__(parent)
        self.label = QtWidgets.QLabel()
        self.setWindowTitle("Help View")
        self.setWindowIcon(QtGui.QIcon("visual/images/Ok.svg"))
        self.resize(720, 320)
        self.lay = QtWidgets.QVBoxLayout()
        self.label.setText(
            '''
                Welocome to Simple SQLite!\n
                Вы можете конкретнее прочитать об устройстве приложения в Documentation.docx\n
                Самый простой редактор БД, так как 9/10 функий БД в нем использоваться не могут!\n
                Зато есть эта божественная пояснительная записка!\n
                Есть 4 основыные части Интерфейса: Меню, Окно Файлов и 2 Таблицы.\n
                В Первой таблице видна структура документа
                Во Второй - данные
                В приложении есть меню файлов: Вы можете открывать и создавать файлы.\n
                Есть ограничения касательно форматов. Они видны в меню открытия файлов.\n
                Поддерживаются форматы *.db *.sqlite и *.sqlite3\n
                Вы действительно можете открыть файл формата .csv или какого-либо другого, но
                работать они не будут.

            '''
        )
        self.lay.setContentsMargins(10, 10, 10, 10)
        self.lay.addWidget(self.label)
        self.setLayout(self.lay)
        self.setStyleSheet(
            "background-color: #FFF; font-family:Roboto; font-weight: bold; font-size: 10pt;")