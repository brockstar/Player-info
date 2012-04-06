from PyQt4 import QtGui

import controller
import gui

class PlayerInfoGui(QtGui.QMainWindow):
    def __init__(self):
        super(PlayerInfoGui, self).__init__()
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_controls()
        
    def connect_controls(self):
        self.ui.lookupButton.clicked.connect(self.lookup_player)
        
    def lookup_player(self):
        print 'Looking up player...',
        name = self.ui.playernameEdit.text() 
        if controller.get_player_image(name):
            pixmap = QtGui.QPixmap('temp.jpg')
            self.ui.profile_image.setPixmap(pixmap)
            print 'Done.'
        else:
            print 'Failed.'
        attributes = {'Pos', 'Team', 'Weight', 'Height'}