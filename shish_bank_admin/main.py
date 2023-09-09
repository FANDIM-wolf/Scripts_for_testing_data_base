# Script for testing DataBase
# Issue : there is problem with colummn INN .


from pprint import pformat
import pymysql

from pyfiglet import figlet_format
from controller import *

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QDialog , QVBoxLayout, QWidget, QSizePolicy , QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mainwindow import Ui_MainWindow
from workwindow_ui import Ui_Dialog
from graph_ui import Ui_Dialog_graph
from creditwindow import Ui_Dialog_credit
from bank_credit_functions import *
# Variable  is True while program in work , when user quits program ,it is false


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # Connect UI elements to event handlers (slots)
        #self.pushButton.clicked.connect(self.handle_login)
        self.pushButton_2.clicked.connect(self.open_creditwindow)

    def open_creditwindow(self):
        creditwindow = CreditWindow()
        creditwindow.exec()

    #def handle_login(self):
    #    print("Function is started")
    #    login = self.lineEdit.text()
    #    print("Login :", login)
    #    password = self.lineEdit_2.text()
    #    print("Login :", password)
    #
    #    client = get_client_by_login_password(connection, login, password)
    #
    #        if client:
    #            # Perform necessary action when client is found
    #               print(client)
    #               workwindow = WorkWindow()
    #            workwindow.exec()
    #            self.hide()  # Hide the main window
    #        else:
    #            # Display an error message or dialog when client is not found
    #            print("No client found with provided login and password.")





class WorkWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(WorkWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.handle_function_create_user)
        self.pushButton_3.clicked.connect(self.handle_function_open_creditwindow)
    def handle_function_open_creditwindow(self):
        creditwindow = CreditWindow()
        creditwindow.exec()
        self.hide()
    def handle_function_create_user(self):
        self.label.hide()# for testing 

class CreditWindow(QDialog, Ui_Dialog_credit):
    annuity = False # to define  credit payment method 
    def __init__(self, parent=None):
        super(CreditWindow, self).__init__(parent)
        self.setupUi(self)
        self.label_4.hide()

        self.pushButton_2.hide() #in begin it is hidden , while table is not displayed 
        self.tableWidget.hide()
        self.radioButton.toggled.connect(self.onClicked)
        self.radioButton_2.toggled.connect(self.onClicked_second)
      
        self.pushButton.clicked.connect(self.onClicked_credit_function)
    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.label_4.hide()
            self.label_3.show()
            self.annuity = True
    def onClicked_second(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.label_3.hide()
            self.label_4.show()
            self.annuity = False
   
    
    def onClicked_credit_function(self):
        loan_amount = self.lineEdit.text()
        annual_interest_rate = self.lineEdit_2.text()
        loans_terms_months_or_years = self.lineEdit_3.text()
        print(loan_amount , annual_interest_rate , loans_terms_months_or_years)
        loan_amount = float(loan_amount)
        annual_interest_rate =float(annual_interest_rate)
        loans_terms_months_or_years = int(loans_terms_months_or_years)
        if(self.annuity == True):
            schedule = annuity_payment_schedule(loan_amount,annual_interest_rate,loans_terms_months_or_years)
            #testing loop
            for i in range(len(schedule)):
                print(schedule[i])
            
            self.pushButton_2.show()
            self.tableWidget.show()
            self.tableWidget.setRowCount(len(schedule)) # в данном примере идет платеж на 12 месяцев
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["month", "interest_payment" , "principal_payment" , "loan_amount"])

            # Add sample data to the table
            for row in range(len(schedule)):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(schedule[row][0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(schedule[row][1])))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(schedule[row][2])))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(schedule[row][3])))

            #for row_number, row_data in enumerate(schedule):
            #    self.add_data_to_table(row_number, row_data)
    #def add_data_to_table(self, row_number, row_data):
    #    self.tableWidget.insertRow(row_number)
    #    for column_number, column_data in enumerate(row_data):
    #        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
            

class MatplotlibWidget(QDialog , Ui_Dialog_graph):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Matplotlib Example')

       

        # Create the QVBoxLayout and add the canvas and toolbar to it
        layout = QVBoxLayout()

        # Create a Matplotlib canvas with a figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.updateGeometry()

        # Create a toolbar for the Matplotlib canvas
        #self.toolbar = NavigationToolbar(self.canvas, self)

        #layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.widget_graph.setLayout(layout)
        
        self.plot_sample_graph()

    def plot_sample_graph(self):
        x = [0, 1, 2, 3, 4]
        y = [2, 1, 4, 3, 5]

        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(x, y)
        ax.set_title('Sample Graph')

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    connection = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="elkin",
        database="bank_test",
        cursorclass=pymysql.cursors.DictCursor
    )

    main_window = MyMainWindow()
    main_window.show()

    #main_window = MatplotlibWidget()
    #main_window.show()


    exit_code = app.exec_()
    connection.close()
    sys.exit(exit_code)
