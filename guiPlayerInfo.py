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
        # Remove temporary profile image on exit.
        if os.path.isfile('temp.png'):
            os.remove('temp.png')
        
    def connect_controls(self):
        self.ui.lookupButton.clicked.connect(self.lookup_player)
        
    def lookup_player(self):
        player = controller.PlayerLookup(self.ui.playernameEdit.text())
        # Load profile image for player
        if player.get_player_image():
            pixmap = QtGui.QPixmap('temp.png')
            self.ui.profile_image.setPixmap(pixmap)
        attributes = ['Position', 'Team', 'Weight', 'Height', 'College']
        values = player.get_player_attributes(attributes)
        # Check if all necessary attributes are set, otherwise set to '???'
        for key in attributes:
            if not key in values.keys():
                values[key] = '???'
        self.ui.positionLabel.setText('Pos: %s' % values['Position'].upper())
        self.ui.teamLabel.setText('Team: %s' % values['Team'].upper())
        height = float(values['Height']) / 100.0
        self.ui.heightLabel.setText('H: %3.2f m' % height)
        self.ui.weightLabel.setText('W: %d kg' % int(values['Weight']))
        self.ui.collegeLabel.setText('College: %s' % values['College'])
        # Retrieve stats and corresponding values.
        # Insert them into table afterwards.
        stats, values = player.get_player_stats(2011)
        self.ui.statsTable.setRowCount(1)
        self.ui.statsTable.setColumnCount(len(stats))
        for index, item in enumerate(stats):
            header_item = QtGui.QTableWidgetItem(item)
            self.ui.statsTable.setHorizontalHeaderItem(index, header_item)
            table_item = QtGui.QTableWidgetItem(values[index])
            self.ui.statsTable.setItem(0, index, table_item)
        