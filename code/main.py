from visual.IMPORT.IMPORT import *  # Import all packages I need
# Import classes with Interface, styles and some activities
import sqlite3 as sql
from visual.mainWindow import MAIN
from visual.widgets.treeItem import TreeItem
from visual.widgets.errDialog import ErrorDialogue

DB_CLASSIC = ['*.db', '*.sqlite3', '*.sqlite']
CSV_CLASSIC = ['*.csv']


class SimpleSQL(MAIN):
    # total Application Class

    def readConfigFile(self):
        try:
            reader = open("config.txt", 'r').read().split('\n')
            self.DB = reader[0].split(", ")
            self.CSV = reader[1].split(", ")
            self.Opened = reader[2].split(", ")
            # print(self.DB, self.CSV, self.Opened)
            for ans in self.Opened:
                try:
                    if len(ans) > 1:
                        if "*." + ans.split('.')[-1] in self.DB:
                            self.tree.addTopLevelItem(
                                TreeItem(ans.split('/')[0], self.tree, 'sql'))
                        elif "*." + ans.split('.')[-1] in self.CSV:
                            self.tree.addTopLevelItem(
                                TreeItem(ans.split('/')[0], self.tree, 'csv'))
                        else:
                            self.tree.addTopLevelItem(
                                TreeItem(ans.split('/')[0], self.tree, 'unk'))
                    # print(ans)
                except OSError:
                    print("NoFiles")
        except OSError:
            writer = open("config.txt", 'w')
            writer.write(", ".join(DB_CLASSIC) + "\n")
            writer.write(", ".join(CSV_CLASSIC) + "\n")
            writer.write(", ".join([]) + "\n")
            writer.close()

    def Open(self):
        try:
            dialog = QtWidgets.QFileDialog(self, 'Open file')
            ans = dialog.getOpenFileName(filter='; '.join(
                self.DB) + ";;" + '; '.join(self.CSV) + ';;All files (*.*)')
            if len(ans[0]) > 1:
                self.Opened.append(ans[0])
                if "*." + ans[0].split('.')[-1] in self.DB:
                    self.tree.addTopLevelItem(
                        TreeItem(ans[0], self.tree, 'sql'))
                elif "*." + ans[0].split('.')[-1] in self.CSV:
                    dialog = QtWidgets.QInputDialog.getText(
                        self, "Choose Separator", "Separator:", False)
                    t = TreeItem(ans[0], self.tree, 'csv')
                    t.Separator = dialog
                    t.createChildrenCsv()
                    self.tree.addTopLevelItem(t)
                else:
                    self.tree.addTopLevelItem(
                        TreeItem(ans[0], self.tree, 'unk'))
        except OSError:
            pass

    def setTable(self, parent, item):
        if parent.type == 'sql':
            crs = parent.base.cursor()
            vals = list(crs.execute(
                "SELECT * FROM {}".format(item.DataBaseName)))
            ans = crs.description
            columnVals = list(crs.execute(
                "PRAGMA table_info('{}')".format(item.DataBaseName)))
            self.Tab1.tableWidget.setRowCount(len(ans))
            self.Tab1.tableWidget.setColumnCount(len(columnVals[0]))
            self.Tab1.lineEdit.setText(item.basename)
            for i in range(len(columnVals)):
                for j in range(len(columnVals[i])):
                    self.Tab1.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(columnVals[i][j])))

            # set databse values to table
            self.Tab2.tableWidget.setRowCount(len(vals))
            self.Tab2.tableWidget.setColumnCount(len(ans))
            self.Tab2.tableWidget.setHorizontalHeaderLabels(
                list(map(lambda x: x[0], ans)))
            self.Tab2.lineEdit.setText(item.basename)
            for i in range(len(vals)):
                for j in range(len(vals[i])):
                    self.Tab2.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(vals[i][j])))
            # self.Tab1 is columns table
            # self.Tab2 is data table

    def TreeItemPressedLow(self, item, row):
        if item.type == 'low':
            for j in range(self.tree.topLevelItemCount()):
                self.tree.topLevelItem(j).setIcon(
                    0, self.tree.topLevelItem(j).icon)
                for i in self.tree.topLevelItem(j).Tables:
                    i.setIcon(0, QtGui.QIcon(""))
            item.setIcon(0, QtGui.QIcon("visual/images/Pen.svg"))
            item.parent().setIcon(0, item.parent().iconActive)
            self.selectedTreeItem = item
            self.setTable(item.parent(), item)

    def rowSelection(self, item):
        t = item.selectedItems()
        if len(t) > 0:
            item.selectRow(t[0].row())

    def itemChanged(self, item, x):
        pass

    def reloadTables(self):
        if len(self.tree.selectedItems()) == 0:
            return None
        item = self.tree.selectedItems()[0]
        if item is None or item.parent() is None:
            return None
        if item.parent().type == 'sql':
            try:
                base = sql.connect(item.parent().DataBaseName)
                crs = base.cursor()
                vals = list(crs.execute(
                    "SELECT * FROM {}".format(item.DataBaseName)))
                ans = crs.description
                columnVals = list(crs.execute(
                    "PRAGMA table_info('{}')".format(item.DataBaseName)))
                self.Tab1.tableWidget.setRowCount(len(ans))
                self.Tab1.tableWidget.setColumnCount(len(columnVals[0]))
                self.Tab1.lineEdit.setText(item.basename)
                for i in range(len(columnVals)):
                    for j in range(len(columnVals[i])):
                        self.Tab1.tableWidget.setItem(
                            i, j, QtWidgets.QTableWidgetItem(str(columnVals[i][j])))

                # set databse values to table
                self.Tab2.tableWidget.setRowCount(len(vals))
                self.Tab2.tableWidget.setColumnCount(len(ans))
                self.Tab2.tableWidget.setHorizontalHeaderLabels(
                    list(map(lambda x: x[0], ans)))
                self.Tab2.lineEdit.setText(item.basename)
                for i in range(len(vals)):
                    for j in range(len(vals[i])):
                        self.Tab2.tableWidget.setItem(
                            i, j, QtWidgets.QTableWidgetItem(str(vals[i][j])))
            except:
                pass
        if item.type == 'low':
            item = item.parent()
        index = self.tree.indexOfTopLevelItem(item)
        news = self.tree.takeTopLevelItem(index)
        news = news.reload()
        if self.tree.topLevelItemCount() > 0:
            self.tree.insertTopLevelItem(index, news)
        else:
            self.tree.addTopLevelItem(news)
        self.tree.collapseItem(self.tree.topLevelItem(index))
        self.tree.expandItem(self.tree.topLevelItem(index))
        self.Tab1.tableWidget.clear()
        self.Tab1.lineEdit.setText("")
        self.Tab2.tableWidget.clear()
        self.Tab2.lineEdit.setText("")

    def reloadStruct(self):
        if len(self.tree.selectedItems()) == 0:
            return None
        item = self.tree.selectedItems()[0]
        parent = item.parent()
        if parent.type == 'sql':
            crs = parent.base.cursor()
            vals = list(crs.execute(
                "SELECT * FROM {}".format(item.DataBaseName)))
            ans = crs.description
            columnVals = list(crs.execute(
                "PRAGMA table_info('{}')".format(item.DataBaseName)))
            self.Tab1.tableWidget.setRowCount(len(ans))
            self.Tab1.tableWidget.setColumnCount(len(columnVals[0]))
            self.Tab1.lineEdit.setText(item.basename)
            for i in range(len(columnVals)):
                for j in range(len(columnVals[i])):
                    self.Tab1.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(columnVals[i][j])))
            self.Tab1.lineEdit.setText(item.basename)
            self.Tab2.lineEdit.setText(item.basename)

    def reloadValues(self):
        if len(self.tree.selectedItems()) == 0:
            return None
        item = self.tree.selectedItems()[0]
        parent = item.parent()
        if parent.type == 'sql':
            crs = parent.base.cursor()
            vals = list(crs.execute(
                "SELECT * FROM {}".format(item.DataBaseName)))
            ans = crs.description
            self.Tab2.tableWidget.setRowCount(len(vals))
            self.Tab2.tableWidget.setColumnCount(len(ans))
            self.Tab2.tableWidget.setHorizontalHeaderLabels(
                list(map(lambda x: x[0], ans)))
            self.Tab2.lineEdit.setText(item.basename)
            for i in range(len(vals)):
                for j in range(len(vals[i])):
                    self.Tab2.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(vals[i][j])))

    def saveValuesChanges(self):
        if self.selectedTreeItem is None:
            return None
        if self.selectedTreeItem == -1:
            return None
        if len(self.tree.selectedItems()) == 0:
            return None
        if self.selectedTreeItem.parent().type == 'sql':
            parent = self.selectedTreeItem.parent()
            # trying to save new name:
            base = sql.connect(parent.DataBaseName)
            crs = base.cursor()
            if self.selectedTreeItem.DataBaseName != self.Tab2.lineEdit.text():
                try:
                    ChangeNameCommand = "ALTER TABLE {} RENAME TO {}".format(
                        self.selectedTreeItem.DataBaseName, self.Tab2.lineEdit.text())
                    crs.execute(ChangeNameCommand)
                    self.selectedTreeItem.DataBaseName = self.Tab2.lineEdit.text()
                    self.selectedTreeItem.setText(0, self.Tab2.lineEdit.text())
                except sql.OperationalError:
                    dialog = ErrorDialogue(
                        self, "INVALID NEW NAME :: " + self.Tab2.lineEdit.text())
                    self.Tab2.lineEdit.setText(
                        self.selectedTreeItem.DataBaseName)
                    dialog.exec_()
                    return None
            deleteAll = "DELETE FROM {}".format(self.selectedTreeItem.DataBaseName)
            crs.execute(deleteAll)
            createNew = "INSERT INTO {} VALUES".format(self.selectedTreeItem.DataBaseName)
            for i in range(self.Tab2.tableWidget.rowCount()):
                createNew += " ("
                for j in range(self.Tab1.tableWidget.rowCount()):
                    createNew += "'" + self.Tab2.tableWidget.item(i, j).text() + "', "
                createNew[:-2] + "), "
            createNew = createNew[:-2] + ")" 
            if self.Tab2.tableWidget.rowCount() > 0:
                crs.execute(createNew)
            # save all in base
            base.commit()
            index = self.tree.indexOfTopLevelItem(self.selectedTreeItem.parent())
            item = self.tree.takeTopLevelItem(index)
            item.base = base
            item = item.reload()
            self.tree.insertTopLevelItem(index, item)
        self.Tab1.tableWidget.clear()
        self.Tab1.tableWidget.setRowCount(0)
        self.Tab1.tableWidget.setColumnCount(0)
        self.Tab1.lineEdit.setText("")
        self.Tab2.tableWidget.clear()
        self.Tab2.tableWidget.setRowCount(0)
        self.Tab2.tableWidget.setColumnCount(0)
        self.Tab2.lineEdit.setText("")

    def saveStructChanges(self):
        if self.selectedTreeItem is None:
            return None
        if self.selectedTreeItem == -1:
            return None
        if len(self.tree.selectedItems()) == 0:
            return None
        if self.selectedTreeItem.parent().type == 'sql':
            parent = self.selectedTreeItem.parent()
            # trying to save new name:
            base = sql.connect(parent.DataBaseName)
            crs = base.cursor()
            if self.selectedTreeItem.DataBaseName != self.Tab1.lineEdit.text():
                try:
                    ChangeNameCommand = "ALTER TABLE {} RENAME TO {}".format(
                        self.selectedTreeItem.DataBaseName, self.Tab1.lineEdit.text())
                    crs.execute(ChangeNameCommand)
                    self.selectedTreeItem.DataBaseName = self.Tab1.lineEdit.text()
                    self.selectedTreeItem.setText(0, self.Tab1.lineEdit.text())
                except sql.OperationalError:
                    dialog = ErrorDialogue(
                        self, "INVALID NEW NAME :: " + self.Tab1.lineEdit.text())
                    self.Tab1.lineEdit.setText(
                        self.selectedTreeItem.DataBaseName)
                    dialog.exec_()
                    return None
                # trying to save struct Items results
                # print(self.selectedTreeItem.DataBaseName)
            try:
                upadate = "CREATE TABLE {}(".format(
                    "SIMPLESQLTIMEECENTDELETEMELATERJUSTSYSTEMKILLMEPLS" + self.selectedTreeItem.DataBaseName)
                for i in range(self.Tab1.tableWidget.rowCount()):
                    for j in range(1, self.Tab1.tableWidget.columnCount()):
                        if self.Tab1.tableWidget.item(i, j) is not None:
                            if j == 4:
                                upadate += "DEFAULT " + \
                                    str(self.Tab1.tableWidget.item(i, j).text()).replace(
                                        "None", "NULL") + " "
                            elif self.Tab1.tableWidget.item(i, j).text() != '0' and self.Tab1.tableWidget.item(i, j).text() != '1':
                                upadate += self.Tab1.tableWidget.item(
                                    i, j).text().replace("None", "NULL") + " "
                    upadate += ",\n"
                upadate = upadate[:-2] + ')'
                # print(upadate) # here update is a command wich create the
                # same tabe as in the self.Tabq.tableWidget
                crs.execute(upadate)
                deleteAll = "DROP TABLE {}".format(
                    self.selectedTreeItem.DataBaseName)
                crs.execute(deleteAll)
                ChangeNameCommand = "ALTER TABLE {} RENAME TO {}".format(
                    "SIMPLESQLTIMEECENTDELETEMELATERJUSTSYSTEMKILLMEPLS" +
                    self.selectedTreeItem.DataBaseName,
                    self.selectedTreeItem.DataBaseName)
                crs.execute(ChangeNameCommand)
            except sql.OperationalError:
                dialog = ErrorDialogue(
                    self, "INVALID DATA IN TABLES !")
                self.Tab1.lineEdit.setText(self.selectedTreeItem.DataBaseName)
                dialog.exec_()
                return None

            base.commit()
            index = self.tree.indexOfTopLevelItem(
                self.selectedTreeItem.parent())
            item = self.tree.takeTopLevelItem(index)
            item.base = base
            item = item.reload()
            self.tree.insertTopLevelItem(index, item)
        self.Tab1.tableWidget.clear()
        self.Tab1.tableWidget.setRowCount(0)
        self.Tab1.tableWidget.setColumnCount(0)
        self.Tab1.lineEdit.setText("")
        self.Tab2.tableWidget.clear()
        self.Tab2.tableWidget.setRowCount(0)
        self.Tab2.tableWidget.setColumnCount(0)
        self.Tab2.lineEdit.setText("")

    def test(self):
        dialog = ErrorDialogue(self, "TEST Error Dialog")
        dialog.exec_()

    def checkUpdate(self):
        self.Tab2.tableWidget.setColumnCount(self.Tab1.tableWidget.rowCount())
        vals = []
        for i in range(self.Tab1.tableWidget.rowCount()):
            vals.append(self.Tab1.tableWidget.item(i, 1).text())
        self.Tab2.tableWidget.setHorizontalHeaderLabels(vals)

    def AddRow(self, tab):
        try:
            tab.tableWidget.setRowCount(tab.tableWidget.rowCount() + 1)
            for i in range(tab.tableWidget.columnCount()):
                tab.tableWidget.setItem(tab.tableWidget.rowCount(
                ) - 1, i, QtWidgets.QTableWidgetItem(""))
            if tab.tableWidget.columnCount() == 0:
                tab.tableWidget.setRowCount(0)
            self.checkUpdate()
        except AttributeError:
            pass

    def DelRow(self, tab):
        tab.tableWidget.setRowCount(max(0, tab.tableWidget.rowCount() - 1))
        self.checkUpdate()

    def chekMoveUpdate(self, a, b):
        for i in range(self.Tab2.tableWidget.rowCount()):
            dat = self.Tab2.tableWidget.takeItem(i, a).text() + " "
            self.Tab2.tableWidget.setItem(i, a, QtWidgets.QTableWidgetItem(
                self.Tab2.tableWidget.takeItem(i, b).text()))
            self.Tab2.tableWidget.setItem(
                i, b, QtWidgets.QTableWidgetItem(dat))
        self.checkUpdate()

    def UpRow(self, tab):
        # Swap Selected Row Up
        t = tab.tableWidget.selectedItems()
        if len(t) == 0:
            return None
        row = t[0].row()
        lastIndex = None
        newIndex = None
        for i in range(tab.tableWidget.columnCount()):
            dat = tab.tableWidget.item(row, i).text() + ""
            if row != 0:
                lastIndex = row
                newIndex = row - 1
                tab.tableWidget.setItem(
                    row, i, tab.tableWidget.takeItem(row - 1, i))
                tab.tableWidget.setItem(
                    row - 1, i, QtWidgets.QTableWidgetItem(dat))
        if tab == self.Tab1 and lastIndex is not None:
            self.chekMoveUpdate(lastIndex, newIndex)

    def DownRow(self, tab):
        # Swap Selected Row Down
        t = tab.tableWidget.selectedItems()
        if len(t) == 0:
            return None
        row = t[0].row()
        lastIndex = None
        newIndex = None
        for i in range(tab.tableWidget.columnCount()):
            dat = tab.tableWidget.item(row, i).text() + ""
            if row != tab.tableWidget.rowCount() - 1:
                lastIndex = row
                newIndex = row + 1
                tab.tableWidget.setItem(
                    row, i, tab.tableWidget.takeItem(row + 1, i))
                tab.tableWidget.setItem(
                    row + 1, i, QtWidgets.QTableWidgetItem(dat))
        if tab == self.Tab1 and lastIndex is not None:
            self.chekMoveUpdate(lastIndex, newIndex)

    def newBase(self):
        dialog = QtWidgets.QFileDialog(self, 'New file')
        dialog.setStyleSheet("background-color: #ddd;")
        ans = dialog.getSaveFileName(filter='; '.join(
                self.DB) + ";;" + '; '.join(self.CSV) + ';;All files (*.*)')
        try:
            sql.connect(ans[0])
            if len(ans[0]) > 1:
                self.Opened.append(ans[0])
                if "*." + ans[0].split('.')[-1] in self.DB:
                    self.tree.addTopLevelItem(
                        TreeItem(ans[0], self.tree, 'sql'))
                elif "*." + ans[0].split('.')[-1] in self.CSV:
                    dialog = QtWidgets.QInputDialog.getText(
                        self, "Choose Separator", "Separator:", False)
                    t = TreeItem(ans[0], self.tree, 'csv')
                    t.Separator = dialog
                    t.createChildrenCsv()
                    self.tree.addTopLevelItem(t)
                else:
                    self.tree.addTopLevelItem(
                        TreeItem(ans[0], self.tree, 'unk'))
        except OSError:
            ErrorDialogue(self, "PATH TO FILE ERROR :: INCORRECT WAY").exec_()

    def setActs(self):
        # Create actions of Buttons and Widgets
        self.Tab1.tableWidget.itemSelectionChanged.connect(
            lambda: self.rowSelection(self.Tab1.tableWidget))
        self.Tab1.ReloadTableButton.clicked.connect(self.reloadTables)
        self.Tab1.okButton.clicked.connect(self.saveStructChanges)
        self.Tab1.notOkButton.clicked.connect(self.reloadStruct)
        self.Tab1.AddRowButton.clicked.connect(lambda: self.AddRow(self.Tab1))
        self.Tab1.DeleteRowButton.clicked.connect(
            lambda: self.DelRow(self.Tab1))
        self.Tab1.Down.clicked.connect(lambda: self.DownRow(self.Tab1))
        self.Tab1.Up.clicked.connect(lambda: self.UpRow(self.Tab1))

        self.Tab2.tableWidget.itemSelectionChanged.connect(
            lambda: self.rowSelection(self.Tab2.tableWidget))
        self.Tab2.ReloadTableButton.clicked.connect(self.reloadTables)
        self.Tab2.okButton.clicked.connect(self.saveValuesChanges)
        self.Tab2.notOkButton.clicked.connect(self.reloadValues)
        self.Tab2.AddRowButton.clicked.connect(lambda: self.AddRow(self.Tab2))
        self.Tab2.DeleteRowButton.clicked.connect(
            lambda: self.DelRow(self.Tab2))
        self.Tab2.Down.clicked.connect(lambda: self.DownRow(self.Tab2))
        self.Tab2.Up.clicked.connect(lambda: self.UpRow(self.Tab2))

        self.tree.itemClicked.connect(self.TreeItemPressedLow)
        self.actionOpen.triggered.connect(self.Open)
        self.actionNew.triggered.connect(self.newBase)
        self.actionClose.triggered.connect(lambda: self.close())

    def DeleteSelectedItemFromTree(self, *args, item=None):
        if item is None:
            pass
        try:
            if (len(self.tree.selectedItems()) != 0 and
                    (self.tree.selectedItems()[0].parent() == item or self.tree.selectedItems()[0].parent() == item)):
                self.Tab1.tableWidget.clear()
                self.Tab1.tableWidget.setRowCount(0)
                self.Tab1.tableWidget.setColumnCount(0)
                self.Tab1.lineEdit.setText('')
                self.Tab2.tableWidget.clear()
                self.Tab2.lineEdit.setText('')
                self.Tab2.tableWidget.setRowCount(0)
                self.Tab2.tableWidget.setColumnCount(0)
            self.tree.takeTopLevelItem(self.tree.indexOfTopLevelItem(item))
        except:
            pass

    def nextName(self, res):
        name = "new_table_"
        i = 1
        vals = list(map(lambda x: x[0], res))
        while name + str(i) in vals:
            i += 1
        return name + str(i)

    def addTable(self, parent):
        crs = parent.base.cursor()
        res = list(crs.execute("SELECT name FROM sqlite_master WHERE type='table'"))
        s = self.nextName(res)
        crs.execute("CREATE TABLE {} (column)".format(s))
        parent.base.commit()
        parent.Tables.append(TreeItem(s, parent, "low"))

    def deleteTable(self, item):
        if item.DataBaseName != 'sqlite_sequence':
            crs = item.parent().base.cursor()
            crs.execute("DROP TABLE {}".format(item.DataBaseName))
            self.reloadTables()

    def treeMenuContext(self, point):
        index = self.tree.indexAt(point)
        if not index.isValid():
            return
        item = self.tree.itemAt(point)
        this = item
        if item.type == "low":
            item = item.parent()
        name = item.text(0)
        # We build the menu.
        menu = QtWidgets.QMenu()
        actionDelete = menu.addAction("Delete base " + name + " from list")
        actionDelete.triggered.connect(
            lambda: self.DeleteSelectedItemFromTree(item=item))
        menu.addSeparator()
        if this.type == 'low':
            deleteThisTable = menu.addAction(
                "Delete Table " + this.DataBaseName)
            deleteThisTable.triggered.connect(lambda: self.deleteTable(this))
            menu.addSeparator()
        addTable = menu.addAction("Create new table")
        addTable.triggered.connect(lambda: self.addTable(item))
        menu.setStyleSheet(MENU_STYLE)
        menu.exec_(self.tree.mapToGlobal(point))

    def __init__(self):
        super().__init__()
        self.DB = []
        self.CSV = []
        self.Opened = []
        self.selectedTreeItem = -1
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.treeMenuContext)
        self.Tab1.tableWidget.setColumnCount(0)
        self.Tab2.tableWidget.setColumnCount(0)
        self.Tab1.tableWidget.setRowCount(0)
        self.Tab2.tableWidget.setRowCount(0)
        self.readConfigFile()
        self.setActs()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = SimpleSQL()
    ex.show()  # show
    sys.exit(app.exec_())
