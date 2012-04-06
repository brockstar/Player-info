import os
import sys

from PyQt4 import QtGui

import guiPlayerInfo


def main():
    app = QtGui.QApplication(sys.argv)
    gui = guiPlayerInfo.PlayerInfoGui()
    gui.show()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
    