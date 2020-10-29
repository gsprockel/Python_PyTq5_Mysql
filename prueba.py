# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="factura_mysql_guillermo_sprockel "
# )

# print(mydb)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
 
db = QSqlDatabase.addDatabase("QPSQL");
db.setHostName("acidalia");
db.setDatabaseName("customdb");
db.setUserName("mojito");
db.setPassword("J0a1m8");
estado = db.open()
if estado == False:
    print("Fallo conect")
else:
    print ("todo OK")