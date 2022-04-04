import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="josh17rog",
    database="project#2",
    autocommit=True
)

mycursor = mydb.cursor()

#dont forget to do  mydb.commit()

class main_admin:
    """<user objects"""
    Admin_register_code = "abcde"# shaco

    def __init__(self,kwargs):#
      if len(kwargs)==1:
        self.code=kwargs["code"]
      else:
        pass

    """user objects>"""


    """<main functions"""

    #check if table is empty

    def if_table_is_empty(self):#checks if the table is empty
        mycursor.execute("SELECT COUNT(*) FROM main_admin")
        arr = mycursor.fetchall()#the rows of table
        if arr[0][0] == 0:
            return True
        return False

    def CompareCodes(self):
        mycursor.execute("SELECT main_code FROM main_admin")
        sql_code=mycursor.fetchall()
        if self.code==sql_code[0][0]:
          return True
        return False

    def GetGmails(self):
      mycursor.execute("SELECT * from gmail_send")


