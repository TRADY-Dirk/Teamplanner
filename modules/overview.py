import os.path
import sqlite3
import random
import time
from functools import partial

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel


def handleButton(button, user, key):
    status = user.toggleSkill(key)
    button.setProperty('is_active', status)
    button.style().polish(button)


def overview(self):
    layout = QVBoxLayout()

    skill_buttons = {
        "organize": {
            "group": "action",
            "tooltip": ""
        },
        "realize": {
            "group": "action",
            "tooltip": ""
        },
        "perfection": {
            "group": "action",
            "tooltip": ""
        },
        "coordination": {
            "group": "communication",
            "tooltip": ""
        },
        "teamplay": {
            "group": "communication",
            "tooltip": ""
        },
        "communication": {
            "group": "communication",
            "tooltip": ""
        },
        "renew": {
            "group": "knowledge",
            "tooltip": ""
        },
        "specialize": {
            "group": "knowledge",
            "tooltip": ""
        },
        "observe": {
            "group": "knowledge",
            "tooltip": ""
        }
    }

    for index, user in enumerate(self.users):
        layout_h = QHBoxLayout()

        avatar = QPushButton(self.icons['narwhal'], self)
        avatar.setProperty("is_icon", True)
        avatar.setProperty("is_avatar", True)
        layout_h.addWidget(avatar)

        label = QLabel(user.name)
        label.setFixedWidth(200)
        layout_h.addWidget(label)

        for key in skill_buttons:
            skill = skill_buttons[key]
            button = QPushButton(self.icons[key], self)
            button.setObjectName(f'{str(user.uid)}_{key}')
            button.setProperty("is_icon", True)
            button.setProperty("is_active", user.skillset[key])
            button.setProperty("section_" + skill["group"], True)
            button.clicked.connect(partial(handleButton, button, user, key))
            layout_h.addWidget(button)

        layout.addLayout(layout_h)
        self.layout_main.addLayout(layout)

    widget = QWidget()
    widget.setLayout(layout)
    widget.setFixedWidth(200)


# Preperation for a class with SQLite connection
"""
class Ui_Overview():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR, "modules/circular_progress.ui")
    db_path = os.path.join(BASE_DIR, "db.sqlite")
    dbConnection = ''

    def initDBConnection(self):
        self.dbConnection = sqlite3.connect(self.db_path)

    def __init__(self):
        super(Ui_Overview, self).__init__()
        uic.loadUi(self.UI_FILE, self)
        self.readBtn.clicked.connect(self.showTableData)
        self.initDBConnection()

    def showTableData(self):
        result = self.dbConnection.cursor().execute("SELECT * FROM users")
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if(column_number == 0):
                    item = self.getImageLabel(column_data)
                    self.tableWidget.setCellWidget(row_number, column_number, item)
                else:
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.verticalHeader().setDefaultSectionSize(80)

    def getImageLabel(self, image):
        imageLabel = QtWidgets.QLabel(self.centralwidget)
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image, 'jpg')
        imageLabel.setPixmap(pixmap)
        return imageLabel
"""
