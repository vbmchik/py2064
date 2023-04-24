from pprint import pprint
import mysql.connector
from mysql.connector import cursor
from dbHelp import DataHelp


class Database():
    def __init__(self,host,user,password,database):
        self.connect = mysql.connector.connect()
        self.host=host,
        self.user=user,
        self.password=password,
        self.database=database
        
        self.cursor = self.connect.cursor()
    
    def create_connection(self,connection,host,user,password,database):
        self.connection = 0
        self.host = host
        self.host=host,
        self.user=user,
        self.password=password,
        self.database=database
         

    
    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def commit(self):
        self.connect.commit()
    
    def close(self):
        self.cursor.close()
        self.connect.close()


def create_connection(host, user, password,database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            
        )
        print("Connection to MySQL DB successful")
    except NameError as e:
        print(f"The error '{e}' occurred")

    return connection


"""host='localhost', user='user2064', password='!QA2ws3ed'"""

"""
print("Welcome to MyQSL Connect")
print(input("Please enter the hostname: "))
print(input("Please enter the username: ")) 
print(input("Please enter the password: "))
print(input("Please enter the database: "))        
"""
   
      

connection = create_connection()
