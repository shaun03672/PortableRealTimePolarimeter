import sys
from PyQt5 import QtWidgets
from gui import Ui

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
