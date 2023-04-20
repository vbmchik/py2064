import mysql.connector

class DataHelp:
    
    def __init__(self):
        self.find = mysql.connector.connect(host="localhost", user="vbm", password="!QA2ws3ed")
        #self.replace_data
        #self.replace_condition
        #self.replace_query
        
    def replace_data_set(self, **kwargs):
        self.replace_data_set = kwargs
        return self

    def replace_condition_set( self, **kwargs):
        self.replace_condition_set = kwargs
        return self
    
    def extract_parameters(self, args: dict):
        l = []
        for x, y in args.items() :
            l.append(f"{x}={y}")
        return l
    
    def replace_with_data_and_condition(self):
        query = f'update db2064.train set '
        l = self.extract_parameters(self.replace_data_set)    
        query += ', '.join(l)
        query += " where "
        l = self.extract_parameters(self.replace_condition_set)    
        query += ' and '.join(l)
        self.execute_some_query(query)
        self.find.commit()
    
    def checkExist(self, year, month, business):
        query = f"select * from db2064.train where year={year} and month={month} and business={business} "
        return len(self.execute_some_query(query)) != 0
              
    def execute_some_query(self, query):
        cursor = self.find.cursor()
        cursor.execute(query)
        try:
            r = cursor.fetchall()
            cursor.close()
            return r
        except:
            cursor.close()
            return 
    
    def replace_data(self, year, month, business, income):
        query = f"update db2064.train set income={income} where year={year} and business={business} and month={month}"
        self.execute_some_query(query)
    
    def insert_into_query(self,  **kwargs):
        query = f"insert into db2064.train {tuple(kwargs.keys())} values ".replace("'","")
        query += f'{tuple( [ x[1] for x in kwargs.items()] )}'
        print(query)
        self.execute_some_query(query)
        self.find.commit()
        
    def read_all_data(self):
        query = "select * from db2064.train"
        return self.execute_some_query(query)
        
