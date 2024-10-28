#questo codice si collega al libreria di mysql poi crea il database sulla stessa pc della codice python nominato mydatabase1 con user root
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase1")

