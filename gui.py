# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlayerInfo_GUI.ui'
#
# Created: Fri Apr  6 14:21:59 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(321, 386)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.playernameEdit = QtGui.QLineEdit(self.centralwidget)
        self.playernameEdit.setGeometry(QtCore.QRect(10, 10, 181, 27))
        self.playernameEdit.setText(QtGui.QApplication.translate("MainWindow", "Eli Manning", None, QtGui.QApplication.UnicodeUTF8))
        self.playernameEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Player name", None, QtGui.QApplication.UnicodeUTF8))
        self.playernameEdit.setObjectName(_fromUtf8("playernameEdit"))
        self.lookupButton = QtGui.QPushButton(self.centralwidget)
        self.lookupButton.setGeometry(QtCore.QRect(210, 10, 97, 27))
        self.lookupButton.setText(QtGui.QApplication.translate("MainWindow", "Look up!", None, QtGui.QApplication.UnicodeUTF8))
        self.lookupButton.setObjectName(_fromUtf8("lookupButton"))
        self.profile_image = QtGui.QLabel(self.centralwidget)
        self.profile_image.setGeometry(QtCore.QRect(10, 50, 65, 90))
        self.profile_image.setMinimumSize(QtCore.QSize(65, 90))
        self.profile_image.setText(_fromUtf8(""))
        self.profile_image.setPixmap(QtGui.QPixmap(_fromUtf8("dummy.png")))
        self.profile_image.setObjectName(_fromUtf8("profile_image"))
        self.positionLabel = QtGui.QLabel(self.centralwidget)
        self.positionLabel.setGeometry(QtCore.QRect(90, 50, 101, 17))
        self.positionLabel.setText(QtGui.QApplication.translate("MainWindow", "Pos:", None, QtGui.QApplication.UnicodeUTF8))
        self.positionLabel.setObjectName(_fromUtf8("positionLabel"))
        self.teamLabel = QtGui.QLabel(self.centralwidget)
        self.teamLabel.setGeometry(QtCore.QRect(90, 90, 101, 10))
        self.teamLabel.setText(QtGui.QApplication.translate("MainWindow", "Team:", None, QtGui.QApplication.UnicodeUTF8))
        self.teamLabel.setObjectName(_fromUtf8("teamLabel"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 120, 101, 17))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "W/H:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

