import os

from PyQt4 import QtGui

import controller
import gui


class PlayerInfoGui(QtGui.QMainWindow):
    def __init__(self):
        super(PlayerInfoGui, self).__init__()
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_controls()
    
    def __del__(self):
        if os.path.isfile('temp.png'):
            os.remove('temp.png')
        
    def connect_controls(self):
        self.ui.lookupButton.clicked.connect(self.lookup_player)
        
    def lookup_player(self):
        player = controller.PlayerLookup(self.ui.playernameEdit.text())
        if player.get_player_image():
            pixmap = QtGui.QPixmap('temp.png')
            self.ui.profile_image.setPixmap(pixmap)
        attributes = ['Position', 'Team', 'Weight', 'Height']
        values = player.get_player_attributes(attributes)
        self.ui.positionLabel.setText('Pos: %s' % values['Position'].upper())
        self.ui.teamLabel.setText('Team: %s' % values['Team'].upper())
        height = float(values['Height']) / 100.0
        self.ui.heightLabel.setText('H: %3.2f m' % height)
        self.ui.weightLabel.setText('W: %d kg' % int(values['Weight']))