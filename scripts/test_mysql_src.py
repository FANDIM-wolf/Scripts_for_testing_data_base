
#Script for testing DataBase 
# methods:
# 1) get all data from table clients , you can replace with your data
# 2) add data in data base


import pymysql

def get_all_data(cursor):
    # SQL-запрос для выборки всех данных из таблицы 'clients'
    sql = "SELECT * FROM clients"

    cursor.execute(sql)
    # Получение всех результатов
    rows = cursor.fetchall()

    # Создание списка объектов
    clients = []
    for row in rows:
        client = {
            "user_id": row["user_id"],
            "FSS": row["FSS"],
            "phone": row["phone"],
            "adress": row["adress"],
            "INN": row["INN"],
            "email": row["email"]
        }
        clients.append(client)

    return clients

def print_clients(clients):
    for client in clients:
        print(client)

def insert_client_values(connection, fss, phone, address, inn, email):
    try:
        with connection.cursor() as cursor:
            # SQL-запрос для добавления данных в таблицу 'clients'.
            query = """
                INSERT INTO clients (FSS, phone, adress, INN, email)
                VALUES (%s, %s, %s, %s, %s)
            """
            
            values = (fss, phone, address, inn, email)
            
            # Выполнить запрос и внести изменения.
            cursor.execute(query, values)
            connection.commit()
            
            print("Данные успешно добавлены в таблицу 'clients'.")
    except Exception as error:
        print(f"Ошибка при вставке данных: {error}")

try:
    connection = pymysql.connect(
        host="host",
        port="port",
        user="user",
        password="password",
        database="database",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    cursor = connection.cursor()
    fss = "Some FSS"
    phone = 1234567890
    address = "Some Address"
    inn = 0
    email = "mail@example.com"
    
    # Вставить данные в таблицу 'clients'
    #insert_client_values(connection, fss, phone, address, inn, email)

    clients = get_all_data(cursor) 
    print_clients(clients)

except Exception as ex:
    print("Connection refused...")
    print(ex)

finally:
    # Закрывать соединение с базой данных всегда надежно в блоке 'finally'
    if connection:
        connection.close()
        print("Соединение с базой данных закрыто.")
