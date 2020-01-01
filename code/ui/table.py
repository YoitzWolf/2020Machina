from IMPORT import *

class TableStruct(QtWidgets.QWidget):
    def __init__(self):
        super(TableStruct, self).__init__()

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 10, 0, 0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.label.setText("table name:")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.line_2 = QtWidgets.QFrame()
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 5, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 2)

        
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame()

        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.gridLayout.addWidget(self.line_3, 0, 8, 1, 1)

        self.notOkButton = QtWidgets.QPushButton(QtGui.QIcon("images/No.svg"), "")
        self.notOkButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.notOkButton.setObjectName("notOkButton")
        self.gridLayout.addWidget(self.notOkButton, 0, 10, 1, 1)

        self.okButton = QtWidgets.QPushButton(QtGui.QIcon("images/Ok.svg"), "")
        self.okButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 0, 9, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setStyleSheet(
        '''
            QTableWidget{
                background-color: rgb(238, 238, 238);
            }
            QTableWidget QHeaderView{
                background-color: #FFF;
                border: 0px;
            }

            QTableWidget::item{
                background-color: rgb(238, 238, 238);
            }
            QTableWidget::item:selected{
                background-color: rgb(150, 150, 150);
                color: black;
                font-size: 10pt;
            }
            QTableWidget::item:selected{
                background-color: rgb(200, 200, 200);
                color: rgb(1, 1, 1);
                border: 1px solid black;
            }    
            QHeaderView::section {
                  padding-left: 5px;
                  background-color: #FFF;
                  border: 0px;
            }

        ''')
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 11)

        self.Up = QtWidgets.QPushButton(QtGui.QIcon("images/Up.svg"), "")
        self.Up.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.Up.setObjectName("Up")
        self.gridLayout.addWidget(self.Up, 0, 6, 1, 1)

        self.Down = QtWidgets.QPushButton(QtGui.QIcon("images/Down.svg"), "")
        self.Down.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.Down.setObjectName("Down")
        self.gridLayout.addWidget(self.Down, 0, 7, 1, 1)


        self.ReloadTableButton = QtWidgets.QPushButton(QtGui.QIcon("images/Re.svg"), "")
        self.ReloadTableButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.ReloadTableButton.setObjectName("ReloadTableButton")
        self.gridLayout.addWidget(self.ReloadTableButton, 0, 0, 1, 1)

        self.DeleteColumnButton = QtWidgets.QPushButton(QtGui.QIcon("images/Minus.svg"), "")
        self.DeleteColumnButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.DeleteColumnButton.setObjectName("DeleteColumnButton")
        self.gridLayout.addWidget(self.DeleteColumnButton, 0, 4, 1, 1)

        self.ReductColumnButton = QtWidgets.QPushButton(QtGui.QIcon("images/Pen.svg"), "")
        self.ReductColumnButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.ReductColumnButton.setObjectName("ReductColumnButton")
        self.gridLayout.addWidget(self.ReductColumnButton, 0, 3, 1, 1)

        self.AddColumnButton = QtWidgets.QPushButton(QtGui.QIcon("images/Plus.svg"), "")
        self.AddColumnButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.AddColumnButton.setObjectName("AddColumnButton")
        self.gridLayout.addWidget(self.AddColumnButton, 0, 2, 1, 1)

        self.setLayout(self.gridLayout)

    def initStyles(self, helpColor):
        self.setStyleSheet(
            "QFrame{"
                "border-left: 1px solid black;"
                "width: 0px;"
            "}"
            "QTableWidget{"
                "border: 1px solid black;"
            "}"
            "QLabel{"
                "border: 0px;"
                "font-size: 8pt;"
            "}"
            "QLineEdit{"
                "border-bottom: 1px solid black;"
                "font-size: 8pt;"
                "font-weight: bold;"
            "}"
            "QLineEdit:hover{"
                f"border-bottom: 1px solid #{helpColor};"
            "}"
            "QPushButton{"
                "margin: 0;"
                "padding-bottom: 4px;"
            "}"
            "QPushButton:hover{"
                "border-bottom: 1px solid black;"
            "}"
            "QPushButton:pressed{"
                "padding-top: 10px;"
            "}"

        )


