import os
import sys
import subprocess
import os.path
import ctypes
import logging
import configparser

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont, QFontDatabase, QAction
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, \
                              QGridLayout, QVBoxLayout, QHBoxLayout, \
                              QTextEdit, QLabel, QPushButton

# App
from modules.overview import overview
from classes.person import Person

cnf = configparser.ConfigParser()
cnf.sections()
cnf.read('config.ini', encoding='utf-8')
config = cnf['App']
icons = cnf['Icons']

# Taskbar Icon relevant
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(config['Id'])

widgets = {
    "logo": [],
    "button": []
}

users = [
    Person(name="Übersicht", uid=0),
    Person(name="TM 1", uid=1),
    Person(name="TM 2", uid=2),
    Person(name="TM 3", uid=3),
    Person(name="TM 4", uid=4),
    Person(name="TM 5", uid=5),
    Person(name="TM 6", uid=6),
    Person(name="TM 7", uid=7),
    Person(name="TM 8", uid=8),
    Person(name="TM 9", uid=9),
    Person(name="TM 10", uid=10),
    Person(name="Svenja", uid=11),
    Person(name="Thorsten", uid=12)
]
current_user = 0

print('App started')

class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.users = users
        self.icons = icons

        # Window Layout
        logging.debug("Set Layout")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        logging.debug("HBoxLayout")
        self.labelLayout = QHBoxLayout()
        self.layout.addLayout(self.labelLayout)

        layout_left = QVBoxLayout()
        self.layout.addLayout(layout_left)

        self.layout_main = QVBoxLayout()
        self.layout.addLayout(self.layout_main)

        layout_left_top = QHBoxLayout()
        layout_left_center = QVBoxLayout()
        layout_left_bottom = QHBoxLayout()

        system_buttons = [
            "save",
            "export",
            "print"
        ]

        for key in system_buttons:
            button = QPushButton(self.icons[key], self)
            button.setObjectName(key)
            button.setProperty("is_icon", True)

            layout_left_top.addWidget(button)


        for user in self.users:
            print(user.name)
            label = QLabel(user.name)
            label.setObjectName('inactive')
            if user.uid == current_user:
                label.setObjectName('active')
            layout_left_center.addWidget(label)

        button_add = QPushButton(self.icons["add"], self)
        button_add.setProperty("is_icon", True)
        layout_left_bottom.addWidget(button_add)

        layout_left.addLayout(layout_left_top)
        layout_left.addLayout(layout_left_center)
        layout_left.addLayout(layout_left_bottom)

        layout_left.setProperty("layout_left", True)
        overview(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):

        # Font files
        font_id_icons = QFontDatabase.addApplicationFont("assets/fonts/Font Awesome 6 Pro-Regular-400.otf")
        font_id_text = QFontDatabase.addApplicationFont("assets/fonts/circular-bold.otf")

        # Preperation for Icon Font Smoothing
        # QFontDatabase.applicationFontFamilies(font_id).setHintingPreference(QtGui.QFont.HintingPreference.PreferNoHinting)
        # fa = QFont(QFontDatabase.applicationFontFamilies(font_id))
        # fa.setHintingPreference(QFont.HintingPreference.PreferNoHinting)

        # Stylesheet
        with open("assets/themes/stylesheet.qss", "r") as stylefile:
            self.setStyleSheet(stylefile.read())

        # Default Window Settings
        self.setWindowTitle(config['Title'])
        self.resize(int(config['Width']), int(config['Height']))
        self.move(int(config['Position_X']), int(config['Position_Y']))
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        try:
            app_icon = QtGui.QIcon()
            app_icon.addFile('assets/images/icon.png')
            #app_icon.addFile('gui/icons/16x16.png', QtCore.QSize(16, 16))
            #app_icon.addFile('gui/icons/24x24.png', QtCore.QSize(24, 24))
            #app_icon.addFile('gui/icons/32x32.png', QtCore.QSize(32, 32))
            #app_icon.addFile('gui/icons/48x48.png', QtCore.QSize(48, 48))
            #app_icon.addFile('gui/icons/256x256.png', QtCore.QSize(256, 256))
            self.setWindowIcon(app_icon)
        except:
            logging.warning("Problem with the icon file")

        self.setCentralWidget(CentralWidget())

        # Test area Toolbar, Menubar, Statusbar
        """
            exitAct = QAction(QIcon('assets/images/logo.png'), 'Exit', self)
            exitAct.setShortcut('Ctrl+Q')
            exitAct.setStatusTip('Exit application')
            exitAct.triggered.connect(self.close)
    
            menubar = self.menuBar()
            fileMenu = menubar.addMenu('&File')
            fileMenu.addAction(exitAct)
    
            toolbar = self.addToolBar('Exit')
            toolbar.setFixedHeight(48)
            toolbar.setIconSize(QSize(40, 40))
            toolbar.addAction(exitAct)
    
            self.statusBar()
        """

        self.show()

def main(args):
    logging.basicConfig(filename='teamplanner.log', encoding='utf-8', level=logging.DEBUG)
    #logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    logging.debug("__main__")

    app = QApplication(sys.argv)

    logging.debug("Generate Window")
    main_window = MainWindow()

    try:
        sys.exit(app.exec())
    except SystemExit:
        logging.info('Closing Window...')

if __name__ == "__main__":
    # don't auto scale when drag app to a different monitor.
    main(sys.argv[1:])
