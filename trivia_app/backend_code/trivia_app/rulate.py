import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="josh17rog",
  database="project#2",
  autocommit=True
)
mycursor = mydb.cursor()

class rulate_manage:
    def __init__(self,**kwargs):
        if len(kwargs)==2:
          self.name = kwargs["product_name"]
          self.amount = kwargs["amount"]
        elif len(kwargs)==1:
          self.amount = kwargs["amount"]
        else:
            pass
    
    def RegisterItem(self):#register new product
      sql_query = "INSERT INTO prize_pool product_name,amount VALUES %s,%s"
      value_sql = (self.name, self.amount)
      mycursor.execute(sql_query, value_sql)

    def ChangeAmount(self):#change amount of specific product
      sql_query = "UPDATE prize_pool SET amount=%s where product_name=%s"
      value_sql = (self.amount,self.name)
      mycursor.execute(sql_query, value_sql)

    def JoinWheel(self):#getting all avliable products
      mycursor.execute("Select * from prize_pool")
      arara=[]
      items =  mycursor.fetchall()
      for item in items:
        arara.append(item[1])
      return arara

    def UserWin(self):
      pass

def DeleteOneItemForShortPeriod(list_item):
  for item in list_item:
    sql_query="UPDATE FROM prize_pool WHERE product_name=%s set amount=%s"
    value_sql = (item[0],item[1]-1)
    mycursor.execute(sql_query, value_sql)
  

def AutoDelteItem():#auto delete the item when admin register
    mycursor.execute("Select * from prize_pool")
    list_of_items = mycursor.fetchall()
    for item in list_of_items:
        if item[2]<=0:
            sql_query="DELETE FROM prize_pool WHERE product_name=%s"
            value_sql = (item[1],)
            mycursor.execute(sql_query, value_sql)



    