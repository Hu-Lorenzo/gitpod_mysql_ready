import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)
mycursor = mydb.cursor()
def inserisci_animali():
    for i in range(5):
        print("Inserisci i dati per l'animale :")
        id_animale = input("ID: ")
        nome_proprio = input("Nome Proprio: ")
        razza = input("Razza: ")
        peso = input("Peso (in kg): ")
        eta = input("Età (in anni): ")
        sql = "INSERT INTO Mammiferi (Id, Nome_Proprio, Razza, Peso, eta) VALUES (%s, %s, %s, %s, %s)"
        val = (id_animale, nome_proprio, razza, peso, eta)
        mycursor.execute(sql, val)
        i=i+1
    mydb.commit()
    print(mycursor.rowcount, "animali inseriti.")
inserisci_animali()