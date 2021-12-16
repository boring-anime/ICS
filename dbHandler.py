import mysql.connector

class dbHandler:

    def __init__(self, user="ritvik", password="root", host="172.17.0.2",database='ics_database'):
        self.user = user
        self.password = password
        self.host = host
        self.database = database    
        self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host,database=self.database)

    
    def createConnection(self):
        return self.connection

    def putData(self,key,value):
        cursor = self.connection.cursor()
        cursor.execute("Insert into records Values('%(key)s','%(value)s');" % locals())
        self.connection.commit()
        for i in cursor:
            return i

    
    def getData(self,key):
        print(key)
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM records WHERE userkey = '%(key)s';" % locals())
        for i in cursor:
            return i

