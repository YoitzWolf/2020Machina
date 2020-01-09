# My Personal Widget. Have Menu and QTableWidget
from visual.widgets.hoverButton import HoverButton
from PyQt5 import QtCore, QtGui, QtWidgets, Qt


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
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 5)

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

        self.notOkButton = HoverButton(QtGui.QIcon(
            "visual/images/No.svg"), QtGui.QIcon("visual/images/NoHover.svg"))
        self.notOkButton.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.notOkButton.setObjectName("notOkButton")
        self.gridLayout.addWidget(self.notOkButton, 0, 10, 1, 1)

        self.okButton = HoverButton(QtGui.QIcon(
            "visual/images/Ok.svg"), QtGui.QIcon("visual/images/OkHover.svg"))
        self.okButton.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 0, 9, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 11)

        self.Up = HoverButton(QtGui.QIcon(
            "visual/images/Up.svg"), QtGui.QIcon("visual/images/UpHover.svg"))
        self.Up.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.Up.setObjectName("Up")
        self.gridLayout.addWidget(self.Up, 0, 6, 1, 1)

        self.Down = HoverButton(QtGui.QIcon(
            "visual/images/Down.svg"), QtGui.QIcon("visual/images/DownHover.svg"))
        self.Down.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.Down.setObjectName("Down")
        self.gridLayout.addWidget(self.Down, 0, 7, 1, 1)

        self.ReloadTableButton = HoverButton(QtGui.QIcon(
            "visual/images/Re.svg"), QtGui.QIcon("visual/images/ReHover.svg"))
        self.ReloadTableButton.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.ReloadTableButton.setObjectName("ReloadTableButton")
        self.gridLayout.addWidget(self.ReloadTableButton, 0, 0, 1, 1)

        self.DeleteRowButton = HoverButton(QtGui.QIcon(
            "visual/images/Minus.svg"), QtGui.QIcon("visual/images/MinusHover.svg"))
        self.DeleteRowButton.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.DeleteRowButton.setObjectName("DeleteRowButton")
        self.gridLayout.addWidget(self.DeleteRowButton, 0, 4, 1, 1)

        self.ReductRowButton = HoverButton(QtGui.QIcon(
            "visual/images/Pen.svg"), QtGui.QIcon("visual/images/PenHover.svg"))
        self.ReductRowButton.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.ReductRowButton.setObjectName("ReductRowButton")
        # self.gridLayout.addWidget(self.ReductRowButton, 0, 3, 1, 1)

        self.AddRowButton = HoverButton(QtGui.QIcon(
            "visual/images/Plus.svg"), QtGui.QIcon("visual/images/PlusHover.svg"))
        self.AddRowButton.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.AddRowButton.setObjectName("AddRowButton")
        self.gridLayout.addWidget(self.AddRowButton, 0, 2, 1, 1)

        self.setLayout(self.gridLayout)

    def initStyles(self, helpColor):
        self.tableWidget.setStyleSheet(
            "QTableWidget::item:hover{"
            f"background-color: #{helpColor};"
            "}"
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
                background-color: rgb(200, 200, 200);
                color: rgb(1, 1, 1);
                border: 1px solid black;
            }    
            QHeaderView::section {
                  padding-left: 5px;
                  background-color: #FFF;
                  border: 0px;
            }

        '''
        )
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
            "padding-bottom: 10px;"
            "}"
            "QPushButton:pressed{"
            "padding: 0px;"
            "padding-top: 10px;"
            "}"
        )
