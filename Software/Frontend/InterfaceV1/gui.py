from PyQt5 import QtWidgets, QtCore, uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self)  # Load the .ui file
        self.setFixedSize(self.size())  # Disables window resizing
        self.setWindowTitle("Real-Time Portable Polarimeter")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # Used to hide window frame
        self.move(0, 0)  # Move frame to top left of screen
