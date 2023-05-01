#! /usr/bin/env python3
"""Created by chris at 4/2/23

Examples of simple message dialogs

Ref: https://www.pythonguis.com/tutorials/pyqt-dialogs/
"""
import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox
)


class MainWindow(QMainWindow):
    """Skeleton app with a button"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        # button.clicked.connect(self.variation_button_clicked)
        self.setCentralWidget(button)



    def button_clicked(self, s):
        """simpler message box with builtin methods"""
        button = QMessageBox.question(self, "Question dialog", "The longer message.")

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")


    def variation_button_clicked(self, s):
        """message box does not have an icon
        and other variations"""
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("Holy Cow!")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Warning)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")


    def notbutton_clicked(self, s):
        """slot method to show a response"""
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("OK!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
