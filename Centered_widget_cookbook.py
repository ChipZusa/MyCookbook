#! /usr/bin/env python3
"""Created by chris at 4/2/23

Centering a dialog on the screen.

Ref: https://python-commandments.org/pyqt-center-window/
"""
import sys

from PyQt5.QtGui import QScreen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox,
    QVBoxLayout, QLabel, QWidget
)


class MainWindow(QMainWindow):
    """Skeleton app with a button"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("This Window is Centered")

        # use default buttonbox accept/reject which can be handled
        # after custom dialog created and returned
        button_ok = QPushButton("Ok/Cancel")  # done
        button_ok.clicked.connect(self.button_ok_clicked)

        # use default buttonbox accept/reject which can be handled
        # after custom dialog created and returned
        button_save = QPushButton("Save")  # QDialogButtonBox.Save
        button_save.clicked.connect(self.button_save_clicked)

        # QDialogButtonBox.Open | QDialogButtonBox.Save | QDialogButtonBox.Abort
        # To handle multiple buttons, create my own buttons and add them
        # to the buttonbox ... and connect to their own slots if necessary.
        self.button_opensaveabort = QPushButton("Open/Save/Abort")
        self.button_opensaveabort.clicked.connect(self.button_opensaveabort_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button_ok)
        layout.addWidget(button_save)
        layout.addWidget(self.button_opensaveabort)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # fg = self.frameGeometry()
        # print(f"frameGeometry: {fg}")
        # print(fg.height(), fg.width())

        # Show the widget now while still in the init so
        # the frameGeometry() can grab actual instead of
        # default dimensions.
        # In order to get the true dimensions of a widget, instead of
        # defaults, must call the frameGeometry AFTER the widget has
        # been physically displayed.
        self.show()

        self.centerWidgetOnScreen(self)
        # fg = self.frameGeometry()
        # print(f"frameGeometry: {fg}")
        # print(fg.height(), fg.width())

    def centerWidgetOnScreen(self, widget):
        """once a widget has been displayed, this will
        center the widget on the screen"""
        centerPoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fg = widget.frameGeometry()
        # print(fg.height(), fg.width())
        fg.moveCenter(centerPoint)
        widget.move(fg.topLeft())

    def button_opensaveabort_clicked(self, s):
        """slot method to show a response"""
        print("click", s)

        # Will pass "self" into CustomDialog so
        # it will recognize the MainWindow as
        # parent (and place the dialog over the parent)
        dlg = OpensaveabortDialog(self)

        # Once we have created the dialog, we start it using .exec()
        # - an entire new event loop specific for the dialog is created
        if dlg.exec():
            print("Success!")

            # if self.button_sender == QDialogButtonBox.Open:
            #     print("sent by Open")
        else:
            print("Cancel!")

    def button_ok_clicked(self, s):
        """slot method to show a response"""
        print("click", s)

        # Will pass "self" into CustomDialog so
        # it will recognize the MainWindow as
        # parent (and place the dialog over the parent)
        dlg = OkDialog(self)
        # Once we have created the dialog, we start it using .exec()
        # - an entire new event loop specific for the dialog is created
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    def button_save_clicked(self, s):
        """slot method to show a response"""
        print("click", s)

        # Will pass "self" into CustomDialog so
        # it will recognize the MainWindow as
        # parent (and place the dialog over the parent)
        dlg = SaveDialog(self)
        # Once we have created the dialog, we start it using .exec()
        # - an entire new event loop specific for the dialog is created
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")


class SaveDialog(QDialog):
    """for OK and CANCEL
    ... also try with standard buttons instead of a
    buttonBox"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # The parent in the above will cause the dialog
        # to be placed over the widget passed in as
        # the parent.

        self.setWindowTitle("Save")

        # define the buttons to show
        # You can construct a line of multiple buttons by OR-ing them
        # together using a pipe (|). Qt will handle the order automatically,
        # according to platform standards.
        # QBtn will contain an integer value representing those
        # two buttons
        QBtn = QDialogButtonBox.Save | QDialogButtonBox.Cancel

        # create the QDialogButtonBox instance to hold the buttons.
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Save dialog")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class OkDialog(QDialog):
    """for OK and CANCEL
    ... also try with standard buttons instead of a
    buttonBox"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # The parent in the above will cause the dialog
        # to be placed over the widget passed in as
        # the parent.

        self.setWindowTitle("HELLO!")

        # define the buttons to show
        # You can construct a line of multiple buttons by OR-ing them
        # together using a pipe (|). Qt will handle the order automatically,
        # according to platform standards.
        # QBtn will contain an integer value representing those
        # two buttons
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        # create the QDialogButtonBox instance to hold the buttons.
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class OpensaveabortDialog(QDialog):
    """for OK and CANCEL
    ... also try with standard buttons instead of a
    buttonBox"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # The parent in the above will cause the dialog
        # to be placed over the widget passed in as
        # the parent.

        # MainWindow.button_sender = self.sender()
        self.setWindowTitle("opensaveabort")

        # define the buttons to show
        # You can construct a line of multiple buttons by OR-ing them
        # together using a pipe (|). Qt will handle the order automatically,
        # according to platform standards.
        # QBtn will contain an integer value representing those
        # two buttons
        # QBtn = QDialogButtonBox.Open | QDialogButtonBox.Save | QDialogButtonBox.Abort

        # create the QDialogButtonBox instance to hold the buttons.
        open_button = QPushButton("Open")
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")

        buttonBox = QDialogButtonBox()
        buttonBox.addButton(QDialogButtonBox.Abort)
        buttonBox.addButton(open_button, QDialogButtonBox.AcceptRole)
        buttonBox.addButton(save_button, QDialogButtonBox.ApplyRole)

        open_button.clicked.connect(self.my_open)
        save_button.clicked.connect(self.my_save)
        buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Open/Save/Abort dialog")
        self.layout.addWidget(message)
        self.layout.addWidget(buttonBox)
        self.setLayout(self.layout)

    def my_open(self):
        print("CCC: Open button clicked")

    def my_save(self):
        print("CCC: Save button clicked")

    # Ctrl+Alt+Shift+L


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    # window.show()

    app.exec()
