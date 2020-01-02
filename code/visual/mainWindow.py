from visual.IMPORT.IMPORT import *
from visual.widgets.table import TableStruct
from visual.widgets.treeItem import TreeItem

class MAIN(QtWidgets.QWidget):
    def resizeEvent(self, event):
        self.treeWidget.setMaximumWidth(self.width()*0.25)

    def setupUi(self):
        self.setObjectName("main")
        self.resize(1080, 720)
        self.setMinimumSize(720, 360)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 26, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.Splitter = QtWidgets.QSplitter()
        self.Splitter.setOrientation(QtCore.Qt.Horizontal)

        self.treeLayout = QtWidgets.QVBoxLayout()
        self.treeLayout.setObjectName("verticalLayout")
        self.tree = QtWidgets.QTreeWidget()
        self.tree.setObjectName("tree")
        self.tree.setHeaderHidden(True)
        self.treeLayout.addWidget(self.tree)
        self.treeWidget = QtWidgets.QWidget()
        self.treeWidget.setLayout(self.treeLayout)
        self.treeWidget.setContentsMargins(0, 0, 0, 0)
        self.treeWidget.setStyleSheet(
            "QWidget{"
                "border: 0px;"
                "padding: 0px;"
                "margin: 0px;"
            "}"
            "QTreeWidget{"
                "border: 0px;"
                "padding: 5px;"
                "background-color: #FFF;"
            "}"
        )
        self.Splitter.addWidget(self.treeWidget)
        self.treeWidget.setMaximumWidth(self.width()*0.3)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab = QtWidgets.QTabWidget()
        self.tab.setObjectName("tab")

        self.Tab1 = TableStruct()
        self.Tab1.setObjectName("Tab1")
        self.tab.addTab(self.Tab1, "Structure")


        self.Tab2 = TableStruct()
        self.Tab2.setObjectName("Tab2")
        self.tab.addTab(self.Tab2, "Data")

        self.Tab3 = QtWidgets.QWidget()
        self.Tab3.setObjectName("Tab3")
        self.tab.addTab(self.Tab3, "Smth More")

        self.verticalLayout.addWidget(self.tab)
        self.TabWidget = QtWidgets.QWidget()
        self.TabWidget.setLayout(self.verticalLayout)
        self.TabWidget.setContentsMargins(0, 0, 0, 0)
        self.TabWidget.setStyleSheet(
            "QWidget{"
                "border: 0px;"
                "padding: 0px;"
                "margin: 0px;"
            "}"

                'QTabWidget::pane {'
                    'border-top: 1px solid #111;'
                    'background: white;'
                '}'

                'QTabWidget::tab-bar:top {'
                    'top: 1px;'
                '}'

                'QTabWidget::tab-bar:bottom {'
                    'bottom: 0px;'
                '}'

                'QTabWidget::tab-bar:left {'
                    'right: 0px;'
                '}'

                'QTabWidget::tab-bar:right {'
                    'left: 0px;'
                '}'

                'QTabBar::tab {'
                    'border: 1px solid #111;'
                    'font-size: 8pt;'
                    'width: 80px;'
                '}'

                'QTabBar::tab:top:first{'
                    'border-top-left-radius: 10px;'
                '}'

                'QTabBar::tab:top:last{'
                    'border-top-right-radius: 10px;'
                '}'
                'QTabBar::tab:top:last:selected{'
                    "right: 10px;"
                    "width: 85px;"
                '}'
                'QTabBar::tab:top:first:selected{'
                    "width: 85px;"
                    "padding-left: 5px;"
                '}'
                'QTabBar::tab:top:selected{'
                    "width: 85px;"
                    "padding-right: 5px;"
                '}'
                'QTabBar::tab:selected {'
                    'background: #111;'
                    'border-top-left-radius: 1px;'
                    'border-top-right-radius: 1px;'
                '}'

                'QTabBar::tab:!selected {'
                    'background: silver;'
                    'border: 0px;'
                    'border-bottom: 1px solid black;'
                '}'

                'QTabBar::tab:!selected:hover {'
                    f'background: #{self.HelpColor};'
                '}'

                'QTabBar::tab:top:!selected {'
                    'margin-top: 3px;'
                '}'

                'QTabBar::tab:bottom:!selected {'
                    'margin-bottom: 3px;'
                '}'

                'QTabBar::tab:top, QTabBar::tab:bottom {'
                    'min-width: 50px;'
                    'margin-right: -1px;'
                    'padding: 5px 10px 5px 10px;'
                '}'

                'QTabBar::tab:top:selected {'
                    'border-bottom-color: none;'
                    'color: #FFF;'
                '}'

                'QTabBar::tab:bottom:selected {'
                    'border-top-color: none;'
                '}'
        )
        self.Splitter.addWidget(self.TabWidget)
        self.Splitter.setStyleSheet(

            "QSplitter::items{"
                "border: 0px;"
                "padding: 0px;"
                "margin: 0px;"
                "background-color: #FFF"
            "}"

            "QSplitter::handle"
            "{"
                "padding: 0px;"
                "margin: 0px;"
                "border: 0.5px solid lightGray;"
            "}"
            "QSplitter{"
                "background-color: #FFF;"
            "}"
            )
        self.Splitter.setHandleWidth(0);
        self.Splitter.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.Splitter)
        self.setLayout(self.horizontalLayout)

        self.Tab1.initStyles(self.HelpColor)
        self.Tab2.initStyles(self.HelpColor)


        self.bar = QtWidgets.QMenuBar(self)
        self.bar.setFixedHeight(26)
        self.bar.setStyleSheet(BAR_STYLE)
        self.menuFile = self.bar.addMenu('File')
        self.menuHelp = self.bar.addMenu('Help')
        self.menuFile.setStyleSheet(MENU_STYLE)
        self.menuHelp.setStyleSheet(MENU_STYLE)

        self.actionOpen = QtWidgets.QAction("Open", self)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.actionNew = QtWidgets.QAction("New", self)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.actionClose = QtWidgets.QAction("Close", self)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        

    def __init__(self):
        super(MAIN, self).__init__()
        self.setUp()

    def setUp(self):
        self.setWindowTitle("Simple SQL")
        self.setWindowIcon(QtGui.QIcon("visual/images/LogoBlack.svg"))
        self.HelpColor = HELP_COLOR
        self.borderColor2 = "lightGray"
        self.treeBgColor = "FFF"
        self.setupUi()
        self.setStyleSheet(TOTAL_STYLE)
        self.tree.setColumnCount(1)
        self.tree.setStyleSheet(
            "QTreeWidget::item{"
                "padding: 2px;"
                "border-radius: 5px;"
                "background: lightGray;"
                "margin-bottom: 5px;"
            "}"
            "QTreeView::item:open{"
                "background: #555;"
                "color: #FFF"
            "}"
            "QTreeView::item:!selected{"
                "background: lightGray;"
            "}"
            "QTreeView:selected{"
                "background: #111;"
                "color: #FFF"
            "}"
            "QTreeView::item:hover:!open{"
                f"background: #{HELP_COLOR};"
            "}"
            "QTreeView::item:open:!selected {"
                "background: #555;"
            "}"
            "QTreeView::item:!open:selected {"
                "background: #111;"
                "color: #FFF;"
            "}"
            "QTreeWidget::branch{"
                "margin-right: 5px;"
                "margin-bottom: 5px;"
            "}"
            "QTreeView::branch:has-siblings:!adjoins-item{"
                "image: none;"
            "}"
            "QTreeView::branch:!has-children:!has-siblings:adjoins-item {"
                "image: none;"
            "}"

            "QTreeView::branch:has-siblings:adjoins-item{"
                "image: none;"
            "}"
            "QTreeView::branch:has-children:!has-siblings:closed,"
            "QTreeView::branch:closed:has-children:has-siblings {"
            "    image: url(visual/images/SQL.svg);"
            "}"

            "QTreeView::branch:open:has-children:!has-siblings,"
            "QTreeView::branch:open:has-children:has-siblings  {"
            "        image: url(visual/images/SQL_ACTIVE.svg);"
            "}"
        )


if __name__ == '__main__':
    from IMPORT.IMPORT import *
    from widgets.table import TableStruct
    from widgets.treeItem import TreeItem
    from widgets.hoverButton import HoverButton
    app = QtWidgets.QApplication(sys.argv)
    ex = MAIN()
    ex.show()
    sys.exit(app.exec_())

