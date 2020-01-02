from IMPORT import *


class TreeItem(QtWidgets.QTreeWidgetItem):
	def createChildren(self):
		self.Tables = []
		for i in range(2):
			self.Tables.append(QtWidgets.QTreeWidgetItem(self, [str(i)], 0))

	def __init__(self, basename, parent=None, _type = 'sql'):
		super(TreeItem, self).__init__(parent, [basename], 0)
		self.baseName = basename
		self.type = _type
		self.createChildren()