## ''' Main file of ShishBankAdmin System '''
##


from pprint import pformat
import typing
from PyQt5 import QtCore ,  QtWidgets , QtGui
import pymysql

from pyfiglet import figlet_format
from controller import *
from cypher_module import *
import sys
from PyQt5.QtCore import pyqtSignal , Qt 
from PyQt5.QtWidgets import QApplication, QMainWindow , QDialog , QVBoxLayout, QWidget, QSizePolicy , QTableWidgetItem ,  QMessageBox , QLabel  
from PyQt5.QtGui import QMouseEvent
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mainwindow import Ui_MainWindow
from workwindow_ui import Ui_Dialog
from graph_ui import Ui_Dialog_graph
from creditwindow import Ui_Dialog_credit
from registerwindow import Ui_Dialog_Register
from bank_credit_functions import *
from tool_functions import *
from passport_data import Ui_Dialog_Passport_Data
# Variable  is True while program in work , when user quits program ,it is false


connection = pymysql.connect(
        host="localhost",
        port=port,
        user="user",
        password="password",
        database="database",
        cursorclass=pymysql.cursors.DictCursor
)

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.tableWidget.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.pushButton_4.hide()
        # Connect UI elements to event handlers (slots)
        #self.pushButton.clicked.connect(self.handle_login)
        self.pushButton_2.clicked.connect(self.open_creditwindow)
        self.pushButton.clicked.connect(self.show_elements)
        self.pushButton_4.clicked.connect(self.get_data_about_user)
        self.pushButton_Register_user.clicked.connect(self.open_register_dialog)
    def open_creditwindow(self):
        creditwindow = CreditWindow()
        creditwindow.exec()
    def show_elements(self):
        
        self.label_6.show()
        self.label_7.show()
        
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.pushButton_4.show()
    def get_data_about_user(self):
        self.label.show()
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.tableWidget.show()
        self.label_5.show()
        self.label_8.show()
        client = get_client_by_phone_and_email(connection ,self.lineEdit.text() , self.lineEdit_2.text() )
        print(client)
        
        credits = get_credit_data_by_user_id(connection , client.user_id)
        inn = get_INN(connection, client.user_id)
        self.label.setText(client.FSS)
        self.label_2.setText(client.address)
        self.label_3.setText(client.email)
        self.label_4.setText(str(client.phone))
        self.label_5.setText(str(inn.inn))
        
        self.tableWidget.setRowCount(len(credits)) # в данном примере идет платеж на 12 месяцев
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["credit_id", "user_id" , "loan_amount" , "annual_interest_rate","loan_term","type_of_payment"])
        for i in range(len(credits)):
            print(credits[i]["user_id"])
        # Add sample data to the table
        for row in range(len(credits)):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(credits[row]["credit_id"])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(credits[row]["user_id"])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(credits[row]["loan_amount"])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(credits[row]["annual_interest_rate"])))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(credits[row]["loan_term"])))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(str(credits[row]["type_of_payment"])))
    def open_register_dialog(self):
        registerwindow = RegisterWindow()
        registerwindow.exec()

            
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



# ''' SIGNALS '''

    def label_clicked():
        print("Label clicked")

#  ''' 

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            print("shit")
            self.clicked.emit()


#class with functions  RegisterWindow 
class RegisterWindow(QDialog, Ui_Dialog_Register ):
    
    
    def __init__(self, parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)
        self.label_6 = ClickableLabel(self)
        self.label_6.clicked.connect(self.on_label_6_click)
        self.label_6.setGeometry(QtCore.QRect(520, 110, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: \"#FF5500\"")
        self.label_6.setObjectName("label_6")
        
    def on_label_6_click(self):
        print("Label_6 clicked") 
        passportdata = PassportData()
        passportdata.exec() 
    def on_label_7_click(self):
        print("Label_6 clicked") 
    
class PassportData(QDialog , Ui_Dialog_Passport_Data):
    def __init__(self, parent=None):
        super(PassportData, self).__init__(parent)  
        self.setupUi(self)

       
        print(self.calendarWidget.selectedDate())
        
        self.pushButton.clicked.connect(self.insert_data)
    def insert_data(self):
        passport_number = self.lineEdit_2.text()
        address_of_issue = self.lineEdit_3.text()
        date_of_issue = self.lineEdit_4.text()
        code_of_district = self.lineEdit_5.text()
        sex =self.lineEdit_6.text()
        date = self.calendarWidget.selectedDate()
        day = date.day()
        month = date.month()
        year = date.year()  
        place_of_birth_date = self.lineEdit_8.text()
        # next step , encrypt and insert data in db 
        insert_passport_data(connection , passport_number, address_of_issue, date_of_issue, code_of_district, sex, day , month ,year, place_of_birth_date)


        
    
    
class WorkWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(WorkWindow, self).__init__(parent)
        self.setupUi(self)
        #hide main elements
        
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
        if(self.annuity == False):
            schedule = differential_payment_algorithm(loan_amount,annual_interest_rate,loans_terms_months_or_years)
            #testing loop
            for i in range(len(schedule)):
                print(schedule[i])
            
            self.pushButton_2.show()
            self.tableWidget.show()
            self.tableWidget.setRowCount(len(schedule)) # в данном примере идет платеж на 12 месяцев
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["years", "interest_payment" , "principal_payment" , "loan_amount"])

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

  
    main_window = MyMainWindow()
    main_window.show()

    #main_window = MatplotlibWidget()
    #main_window.show()


    exit_code = app.exec_()
    connection.close()
    sys.exit(exit_code)
