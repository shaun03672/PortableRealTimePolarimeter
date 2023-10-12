import sys
from PyQt5 import QtWidgets
from gui import Interface

class Main:

    # path = "/home/polarimeter/Documents/PortableRealTimePolarimeter/Software/Frontend/InterfaceV1/gui.ui"
    path = "gui.ui"

    def __init__(self, argv):
        app = QtWidgets.QApplication(argv)
        window = Interface(self.path)
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    Main(sys.argv)
