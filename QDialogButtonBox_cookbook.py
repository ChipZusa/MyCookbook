#! /usr/bin/env python3
"""Created by chris at 4/2/23

Dialog button examples
    - uses QDialogButtonBox to keep standards for different
      operating systems

Ref: https://www.pythonguis.com/tutorials/pyqt-dialogs/
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

        self.setWindowTitle("My App")

        # use default buttonbox accept/reject which can be handled
        # after custom dialog created and returned
        button_ok = QPushButton("Ok/Cancel")
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

        button_yestoall = QPushButton("YesToAll")  # QDialogButtonBox.YesToAll
        button_yestoall.clicked.connect(self.button_yestoall_clicked)

        button_nobutton = QPushButton("NoButton")  # QDialogButtonBox.NoButton
        button_nobutton.clicked.connect(self.button_nobutton_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button_ok)
        layout.addWidget(button_save)
        layout.addWidget(self.button_opensaveabort)
        layout.addWidget(button_yestoall)
        layout.addWidget(button_nobutton)

        # Note that in order to add a layout to the QMainWindow
        # we apply it to a dummy QWidget. This allows
        # us to then use .setCentralWidget to apply the widget
        # (and the layout) to the window.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

        # In order to get the true dimensions of a widget (instead of
        # defaults) must call the frameGeometry AFTER the widget has
        # been physically displayed -- using self.show().
        self.centerWidgetOnScreen(self)
        # fg = self.frameGeometry()
        # print(f"frameGeometry: {fg}")
        # print(fg.height(), fg.width())

    def centerWidgetOnScreen(self, widget):
        centerPoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fg = widget.frameGeometry()
        # print(help(fg))
        print(fg.height(), fg.width())
        fg.moveCenter(centerPoint)
        widget.move(fg.topLeft())

    def button_nobutton_clicked(self, s):
        """slot method to show a response"""
        print("click", s)

        # Will pass "self" into CustomDialog so
        # it will recognize the MainWindow as
        # parent (and place the dialog over the parent)
        dlg = NoButtonDialog(self)

        # Once we have created the dialog, we start it using .exec()
        # - an entire new event loop specific for the dialog is created
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    def button_yestoall_clicked(self, s):
        """slot method to show a response"""
        print("click", s)

        # Will pass "self" into CustomDialog so
        # it will recognize the MainWindow as
        # parent (and place the dialog over the parent)
        dlg = YesToAllDialog(self)

        # Once we have created the dialog, we start it using .exec()
        # - an entire new event loop specific for the dialog is created
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

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


class NoButtonDialog(QDialog):
    """for nobutton"""

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
        QBtn = QDialogButtonBox.NoButton

        # create the QDialogButtonBox instance to hold the buttons.
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
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


class YesToAllDialog(QDialog):
    """for yestoall"""

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
        QBtn = QDialogButtonBox.YesToAll

        # create the QDialogButtonBox instance to hold the buttons.
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    # Ctrl+Alt+Shift+L


if __name__ == "__main__":
    # --> force message to appear over parent.
    app = QApplication(sys.argv)

    window = MainWindow()
    # window.show()

    app.exec()
