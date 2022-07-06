import os.path

from PyQt5.QtWidgets import QGridLayout, QFileDialog, QDialog
from PyQt5 import QtCore
from pathlib import Path


class Project:
    def __init__(self):
        self.filename = "multifile"

    def load(self):
        load = True
        # Open Filesystem
        # Load JSON
        # Close Filesystem
        # Set JSON as Project

    def open(self):
        # File Dialog
        if self.fname is not None and os.path.isfile(self.fname):
            eeg_cap_dir = os.path.dirname(self.fname)
        else:
            eeg_cap_dir = QtCore.QDir.currentPath()

        dialog = QFileDialog(self)
        dialog.setWindowTitle('Open Project')
        dialog.setNameFilter('Project Files (*.af)')
        dialog.setDirectory(eeg_cap_dir)
        dialog.setFileMode(QFileDialog.ExistingFile)

        if dialog.exec_() == QDialog.Accepted:
            filename = dialog.selectedFiles()
        else:
            filename = None

        if filename:
            self.fname = str(filename[0])
            self.group_box.lineEdit.setText(self.fname)

        # Load Project
        self.project_load(self)

    def save(self):
        save = True
        home = str(Path.home())

        try:
            print(f'Trying to save the project in {str(path)}')
            # Open Filesystem
            # Write JSON to file
            # Close Filesystem
        except:
            print('Error while saving the File')

    def generate_pdf(self):
        pdf = True
        # Import PDF Template
        # Write Content to Template
        return pdf

    def export(self):
        export = True
        # Lambda file select
        # Set Filename to selected
        pdf = self.generate_pdf()
        # Save PDF to Filesystem
        # Close Filesystem

    def print(self):
        print = True
        pdf = self.generate_pdf()
