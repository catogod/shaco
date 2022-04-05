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
      if len(kwargs)==3:
        self.code=kwargs["code"]
        self.inv_code=kwargs["inv_code"]
        self.rulate_p=kwargs["rulate_p"]
      elif 'code' in kwargs:
        self.code=kwargs["code"]
      elif 'inv_code' in kwargs:
        self.code=kwargs["inv_code"]
      elif 'rulate_p' in kwargs:
        self.code=kwargs["rulste_p"]
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
    
    def InsertCode(self):
      if self.if_table_is_empty() == False:
        sql_query = "INSERT INTO main_admin (main_code, admin_inv_code, points_for_rulate) VALUES (%s, %s,%s)"
        value_sql = (self.code, self.inv_code, self.rulate_p)
        mycursor.execute(sql_query, value_sql)
        return True
      return False



