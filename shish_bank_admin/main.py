
#Script for testing DataBase  
#Issue : there is problem with colummn INN .


from pprint import pformat
import pymysql

from pyfiglet import figlet_format 
from controller import *
from switcher import *
#Variable  is True while program in work , when user quits program ,it is false

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

def main(cursor  ):
    login = input("Enter login")
    password  = input("Enter password")
    
    client = get_client_by_login_password(cursor, login, password)

    if client:
        #print(client)
        print("""
            1) Print basic information - 0 
            2) Quit - 1

"""             )
        choice = int(input())
       
       
        if choice == 0:
            print(client)
            return 0
        if choice == 1:
            input("Press any key to quit")
            return 1
        else:
            print ("Incorrect command")
            return 1
    
        


try:
    connection = pymysql.connect(
        host="host",
        port=port,
        user="user",
        password="password",
        database="database",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print(figlet_format("ShishBank", font = "standard" ))
    cursor = connection.cursor()
    IN_PROGRES = True
    while(IN_PROGRES):
        result = main(cursor )
        if result == 1 :
            IN_PROGRES = False
        if result == 0 : 
            IN_PROGRES = True
        else:
            ("Unexpected error  ,  main function returned : " , result)
        
        
    # Вставить данные в таблицу 'clients'
    #insert_client_values(connection, fss, phone, address, inn, email)

    #clients = get_all_data(cursor) 
    #print_clients(clients)
    
    
except Exception as ex:
    print("Connection refused...")
    print(ex)

finally:
    # Закрывать соединение с базой данных всегда надежно в блоке 'finally'
    if connection:
        connection.close()
        print("Conection with the data base is closed.")
