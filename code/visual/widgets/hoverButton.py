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

    