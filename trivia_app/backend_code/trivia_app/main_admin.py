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

class admin_manage:
    """<user objects"""
    Admin_register_code = "abcde"# shaco

    def __init__(self,**kwargs):#
        if len(kwargs)==3:
          self.username = kwargs["username"]
          self.password = kwargs["password"]
          self.code = kwargs["code"]
        elif len(kwargs)==2:
          self.username = kwargs["username"]
          self.password = kwargs["password"]
        else:
            pass

    """user objects>"""


    """<main functions"""

    #check if table is empty

    def if_table_is_empty(self):#checks if the table is empty
        mycursor.execute("SELECT COUNT(*) FROM admin")
        arr = mycursor.fetchall()#the rows of table
        if arr[0][0] == 0:
            return True
        return False


