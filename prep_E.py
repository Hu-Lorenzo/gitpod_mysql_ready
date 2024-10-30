import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
   database="Animali"
)
mycursor = mydb.cursor()

def visualizza_animali_peso_2():
    mycursor.execute("SELECT * FROM Mammiferi WHERE Peso > 2")
    result = mycursor.fetchall()
    for animali in result:
        print(animali)

visualizza_animali_peso_2()