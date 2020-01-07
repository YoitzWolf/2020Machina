import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sqlite3
import os


HELP_COLOR = "6D88B4" # "EEB8EE" # another help color? 

MENU_STYLE = """
                QMenu::item{
                    padding: 4px 10px;
                    border-radius: 4px;
                    background-color: transparent;
                }
                QMenu::item:selected {
                    background: #6D88B4;
                    color: #FFF;
                }
                QMenu::item:pressed {
                    background: black;
                    color: #FFF;
                }

            """
BAR_STYLE = '''
            QMenuBar{
                background-color: lightGray;
            }
            QMenuBar::item {
                margin: 1px;
                padding: 3px;
                border-radius: 3px;
            }
            QMenuBar::item:selected{
                background: #6D88B4;
                color: #FFF;
            }
            QMenuBar::item:selected{
                background: black;
                color: #FFF;
            }
            '''
TOTAL_STYLE = '''
                    QWidget{
                        outline: 0;
                        font-family: Roboto;
                    }
                    QScrollBar:vertical {
                                        border: 1px solid #dddddd;
                                        background:white;
                                        width:10px;
                                        margin: 0px 0px 0px 0px;
                                        border-radius: 4px;
                    }
                    QScrollBar::handle:vertical {
                                        background: rgb(120, 120, 120);
                                        min-height: 0px;
                                        border-radius: 4px;
                    }
                    QScrollBar::add-line:vertical {
                                        background: rgb(120, 120, 120);
                                        height: 0px;
                                        subcontrol-position: bottom;
                                        subcontrol-origin: margin;
                                        border-radius: 4px;
                    }
                    QScrollBar::sub-line:vertical {
                                        background: rgb(120, 120, 120);
                                        height: 0 px;
                                        subcontrol-position: top;
                                        subcontrol-origin: margin;
                                        border-radius: 4px;
                    }

                    QScrollBar:horizontal {
                                        border: 1px solid #dddddd;
                                        background:white;
                                        height:10px;
                                        margin: 0px 0px 0px 0px;
                                        border-radius: 4px;
                    }
                    QScrollBar::handle:horizontal {
                                        background: rgb(120, 120, 120);
                                        min-width: 0px;
                                        border-radius: 4px;
                    }
                    QScrollBar::add-line:horizontal {
                                        background: rgb(120, 120, 120);
                                        width: 0px;
                                        subcontrol-position: bottom;
                                        subcontrol-origin: margin;
                                        border-radius: 4px;
                    }
                    QScrollBar::sub-line:horizontal {
                                        background: rgb(120, 120, 120);
                                        width: 0 px;
                                        subcontrol-position: top;
                                        subcontrol-origin: margin;
                                        border-radius: 4px;
                    }
            '''
