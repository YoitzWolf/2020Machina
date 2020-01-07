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
		self.setStyleSheet("background-color: #FFF; font-family:Roboto; font-weight: bold; font-size: 12pt;")