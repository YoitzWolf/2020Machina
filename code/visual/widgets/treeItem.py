# Its TreeWidget Item.
# It has his own database and tables (maybe)
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sqlite3 as sql

class TreeItem(QtWidgets.QTreeWidgetItem):
    def createChildren(self):
        self.Tables = []
        if self.type == 'sql':
            self.base = sql.connect(self.DataBaseName)
            crs = self.base.cursor()
            comm = list(crs.execute("SELECT name FROM sqlite_master WHERE type='table'"))
            for i in comm:
                self.Tables.append(TreeItem(i[0], self, "low"))

    def createChildrenCsv(self):
        self.Tables = []
        if self.type == 'csv':
            self.base = open(self.DataBaseName, 'r').read()
            comm = self.base.split('\n')
            self.Tables.append(TreeItem("Table", self, "low"))

    def reload(self):
        return TreeItem(self.DataBaseName, self.parent(), self.type)

    def __init__(self, basename, parent=None, _type='sql'):
        self.opened = False
        self.separator = ''
        self.DataBaseName = basename
        self.basename = basename.split('/')[-1]
        super(TreeItem, self).__init__(parent, [self.basename], 0)
        self.type = _type
        if _type == "low":
            self.DataBaseName = self.basename
            self.icon = QtGui.QIcon("")
            self.setText(0, "Table: " + self.text(0))
        elif _type == 'sql':
            self.setIcon(0, QtGui.QIcon("visual/images/SQL.svg"))
            self.icon = QtGui.QIcon("visual/images/SQL.svg")
            self.iconActive = QtGui.QIcon("visual/images/SQL_ACTIVE.svg")
        elif _type == 'csv':
            self.setIcon(0, QtGui.QIcon("visual/images/CSV.svg"))
            self.icon = QtGui.QIcon("visual/images/CSV.svg")
            self.iconActive = QtGui.QIcon("visual/images/CSV_ACTIVE.svg")
        else:
            self.setIcon(0, QtGui.QIcon("visual/images/UNK.svg"))
            self.icon = QtGui.QIcon("visual/images/UNK.svg")
        if _type != "low":
            self.createChildren()