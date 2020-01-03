from visual.IMPORT.IMPORT import *  # Import all packages I need
# Import class with Interface, styles and some activities
from visual.mainWindow import MAIN
from visual.widgets.treeItem import TreeItem

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
            print(self.DB, self.CSV, self.Opened)
            for ans in self.Opened:
                try:
                    if len(ans) > 1:
                        if "*." + ans.split('.')[-1] in self.DB:
                            self.tree.addTopLevelItem(TreeItem(ans.split('/')[0], self.tree, 'sql'))
                        elif "*." + ans.split('.')[-1] in self.CSV:
                            self.tree.addTopLevelItem(TreeItem(ans.split('/')[0], self.tree, 'csv'))
                        else:
                            self.tree.addTopLevelItem(TreeItem(ans.split('/')[0], self.tree, 'unk'))
                    #print(ans)
                except OSError:
                    print("NoFiles")
        except OSError:
            writer = open("config.txt", 'w')
            writer.write(", ".join(DB_CLASSIC) + "\n")
            writer.write(", ".join(CSV_CLASSIC) + "\n")
            writer.write(", ".join([]) + "\n")

    def Open(self):
        try:
            dialog = QtWidgets.QFileDialog(self, 'Open file')
            ans = dialog.getOpenFileName(filter='; '.join(self.DB) + ";;" + ', '.join(self.CSV) + ';;All files (*.*)')
            #print(ans[0].split('.')[-1])
            if len(ans[0]) > 1:
                self.Opened.append(ans[0])
                if "*." + ans[0].split('.')[-1] in self.DB:
                    self.tree.addTopLevelItem(TreeItem(ans[0], self.tree, 'sql'))
                elif "*." + ans[0].split('.')[-1] in self.CSV:
                    self.tree.addTopLevelItem(TreeItem(ans[0], self.tree, 'csv'))
                else:
                    self.tree.addTopLevelItem(TreeItem(ans[0], self.tree, 'unk'))
            #print(ans)
        except OSError:
            pass
    
    def TreeItemPressedLow(self, item, row):
        if item.type == 'low':
            for j in range(self.tree.topLevelItemCount()):
                # print(self.tree.topLevelItem(j).Tables)
                for i in self.tree.topLevelItem(j).Tables:
                    i.setIcon(0, QtGui.QIcon(""))
            item.setIcon(0, QtGui.QIcon("visual/images/Pen.svg"))

    def setActs(self):
        self.tree.itemClicked.connect(self.TreeItemPressedLow)
        self.actionOpen.triggered.connect(self.Open)

    def __init__(self):
        super().__init__()
        self.DB = []
        self.CSV = []
        self.Opened = []
        self.readConfigFile()
        self.setActs()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = SimpleSQL()
    ex.show()  # show
    sys.exit(app.exec_())
