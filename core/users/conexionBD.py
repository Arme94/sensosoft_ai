import mysql.connector
conexion = mysql.connector.connect(user='root' , password ='',host='localhost') #,database = 'sensosoft_ai',port='3306')

#print(conexion)
cursor = conexion.cursor()

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
    conexion.close()