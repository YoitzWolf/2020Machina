# I want to have Icons on Buttons in my TableStruct.
# I Create Class of Buttons with concrete Hover function
# I Create it to change images on Buttons
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

class HoverButton(QtWidgets.QPushButton):
    def __init__(self, defaultImage, hoverImage="", pressedImage=""):
        if hoverImage == "":
            hoverImage = defaultImage
        if pressedImage == "":
            pressedImage = hoverImage
        self.defaultImage = defaultImage
        self.hoverImage = hoverImage
        super(HoverButton, self).__init__(self.defaultImage, "")
        self.setMouseTracking(True)

    def enterEvent(self,event):
        self.setIcon(self.hoverImage)
    
    def leaveEvent(self,event):
        self.setIcon(self.defaultImage)

    