# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from IMPORT import *
from table import TableStruct

class MAIN(QtWidgets.QWidget):
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
                f"background-color: #FFF;"
            "}"
        )
        self.Splitter.addWidget(self.treeWidget)
        

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab = QtWidgets.QTabWidget()
        self.tab.setObjectName("tab")

        self.Tab1 = TableStruct()
        self.Tab1.setObjectName("Tab1")
        self.tab.addTab(self.Tab1, "Structure")


        self.Tab2 = QtWidgets.QWidget()
        self.Tab2.setObjectName("Tab2")
        self.tab.addTab(self.Tab2, "Data")

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
                    'right: 1px;'
                '}'

                'QTabWidget::tab-bar:right {'
                    'left: 1px;'
                '}'

                'QTabBar::tab {'
                    'border: 1px solid #111;'
                    'font-size: 8pt;'
                    'width: 80px;'
                '}'

                'QTabBar::tab:top:first{'
                    'border-top-left-radius: 20px;'
                '}'

                'QTabBar::tab:top:last{'
                    'border-top-right-radius: 20px;'
                '}'
                'QTabBar::tab:top:last:selected{'
                    "right: 10px;"
                    "width: 85px;"
                '}'
                'QTabBar::tab:top:first:selected{'
                    "width: 85px;"
                    "padding-left: 5px;"
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


        self.bar = QtWidgets.QMenuBar(self)
        self.bar.setFixedHeight(26)
        self.bar.setStyleSheet(BAR_STYLE)
        self.menuFile = self.bar.addMenu('File')
        self.menuHelp = self.bar.addMenu('Help')
        self.menuFile.setStyleSheet(MENU_STYLE)
        self.menuHelp.setStyleSheet(MENU_STYLE)
        self.actionAdd = QtWidgets.QAction("Add", self)
        self.actionAdd.setObjectName("actionAdd")
        self.menuFile.addAction(self.actionAdd)
        

    def __init__(self):
        super(MAIN, self).__init__()
        self.setWindowTitle("Simple SQL")
        self.setWindowIcon(QtGui.QIcon("images/LogoGreen.svg"))
        self.HelpColor = "EEB8EE"
        self.borderColor2 = "lightGray"
        self.treeBgColor = "FFF"
        self.setupUi()
        self.setStyleSheet(TOTAL_STYLE)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MAIN()
    sys.exit(app.exec_())

