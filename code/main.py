from visual.IMPORT.IMPORT import *
from visual.mainWindow import MAIN

class SimpleSQL():

	def __init__(self):
		self = MAIN()
		

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ex = MAIN()
	ex.show()
	sys.exit(app.exec_())
