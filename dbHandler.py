import mysql.connector

class dbHandler:

    def __init__(self, user="ritvik", password="root", host="172.17.0.4",database='mydb'):
        self.user = user
        self.password = password
        self.host = host
        self.database = database    
    
    def createConnection(self):
        connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host,database=self.database)
        return connection

    def putData(self,connection,key,value):
        cursor = connection.cursor()
        cursor.execute("Insert into records Values('%(key)s','%(value)s');" % locals()))
        for i in cursor:
            return i

    
    def getData(self,connection,key):
        print(key)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM records WHERE userkey = '%(key)s';" % locals())
        for i in cursor:
            return i
