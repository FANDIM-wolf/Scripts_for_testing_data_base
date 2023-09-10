
from models import *



def get_all_data(cursor):
    # SQL-запрос для выборки всех данных из таблицы 'clients'
    sql = "SELECT * FROM clients"

    cursor.execute(sql)
    # Получение всех результатов
    rows = cursor.fetchall()

    # Создание списка объектов
    clients = []
    for row in rows:
        client = Client(
            user_id=row["user_id"],
            FSS=row["FSS"],
            phone=row["phone"],
            address=row["adress"],
            
            email=row["email"]
        )
        clients.append(client)

    return clients

def get_all_private_data(cursor):
    sql = "SELECT * FROM private_data"

    cursor.execute(sql)
    rows = cursor.fetchall()

    private_data_list = []
    for row in rows:
        private_data = PrivateData(
            _id=row['id'],
            user_id=row['user_id'],
            password=row['password'],
            login =row['login']
        )
        private_data_list.append(private_data)

    return private_data_list

def get_client_by_login_password(connection, login, password):
    sql = """SELECT *
             FROM private_data AS p
             INNER JOIN clients AS c ON p.user_id = c.user_id
             WHERE p.login = %s AND p.password = %s"""
    cursor = connection.cursor()
    cursor.execute(sql, (login, password))
    row = cursor.fetchone()

    if row:
        client = Client(
            user_id=row["user_id"],
            FSS=row["FSS"],
            phone=row["phone"],
            address=row["adress"],
            
            email=row["email"]
            
        )
        return client
    else:
        return None
    
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
            
            print("Data was successufully added in 'clients' .")
    except Exception as error:
        print(f"Error in arguments : {error}")

def get_client_by_phone_and_email( connection , phone, email):
    
     
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM clients WHERE phone = %s AND email = %s", (phone, email))
    client_data = cursor.fetchone()

    if client_data:
        client = Client(
            user_id=client_data["user_id"],
            FSS=client_data["FSS"],
            phone=client_data["phone"],
            address=client_data["adress"],
            
            email=client_data["email"]
        )
    else:
        client = None

    cursor.close()
    #connection.close()

    return client
# Function to fetch credit data by user_id
def get_credit_data_by_user_id( connection ,user_id):
    # Replace the following placeholders with your actual database credentials
   

    try:
        # Create a cursor to execute the SQL query
        with connection.cursor() as cursor:
            # SQL query to get credit data by user_id
            sql_query = """
                SELECT * FROM credits
                WHERE user_id = %s;
            """

            # Execute the SQL query
            cursor.execute(sql_query, (user_id,))

            # Fetch all rows and store them as a list of tuples
            credit_data = cursor.fetchall()

        # Close the database connection
        #connection.close()

        # Return the credit data
        return credit_data

    except Exception as e:
        print("Error:", e)
        # Close the database connection
        #connection.close()
        return None
def get_INN( connection , user_id):
    
     
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM inns WHERE user_id = %s ", (user_id))
    client_data = cursor.fetchone()

    if client_data:
        client = INN_private_data(
            user_id=client_data["user_id"],
            inn=client_data["inn"]
            
        )
    else:
        client = None

    cursor.close()
    #connection.close()

    return client