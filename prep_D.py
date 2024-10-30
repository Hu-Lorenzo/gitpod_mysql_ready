import mysql.connector
import prep_C
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)
mycursor = mydb.cursor()
i=0
for i in range(5):
    nome_proprio = input("Nome Proprio : ")
    razza = input("Razza: ")
    peso = input("Peso (in kg): ")
    eta = input("Età (in anni): ")
    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, eta) VALUES (%s, %s, %s, %s)"
    val = (nome_proprio, razza, peso, eta)
    mycursor.execute(sql, val)
    i=i+1
mydb.commit()
print(mycursor.rowcount, "animali inseriti.")
if i == 5:  
    prep_C.get_Mammiferi()
