# Script for testing DataBase
# Issue : there is problem with colummn INN .


from pprint import pformat
import pymysql

from pyfiglet import figlet_format
from controller import *

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QDialog
from mainwindow_ui import Ui_MainWindow
from workwindow_ui import Ui_Dialog

# Variable  is True while program in work , when user quits program ,it is false


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # Connect UI elements to event handlers (slots)
        self.pushButton.clicked.connect(self.handle_login)


    def handle_login(self):
        print("Function is started")
        login = self.lineEdit.text()
        print("Login :", login)
        password = self.lineEdit_2.text()
        print("Login :", password)

        client = get_client_by_login_password(connection, login, password)

        if client:
            # Perform necessary action when client is found
            print(client)
        else:
            # Display an error message or dialog when client is not found
            print("No client found with provided login and password.")




class WorkWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(WorkWindow, self).__init__(parent)
        self.setupUi(self)







if __name__ == '__main__':
    app = QApplication(sys.argv)

    connection = pymysql.connect(
        host="host",
        port=port,
        user="user",
        password="password",
        database="database",
        cursorclass=pymysql.cursors.DictCursor
    )

    main_window = MyMainWindow()
    main_window.show()

    exit_code = app.exec_()
    connection.close()
    sys.exit(exit_code)
