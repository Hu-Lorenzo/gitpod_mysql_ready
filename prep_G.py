import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)
mycursor = mydb.cursor()



def inserisci_A():
    nome_proprio = input("Nome Proprio : ")
    razza = input("Razza: ")
    peso = input("Peso (in kg): ")
    eta = input("Età (in anni): ")
    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, eta) VALUES (%s, %s, %s, %s)"
    val = (nome_proprio, razza, peso, eta)
    mycursor.execute(sql, val)

def visualizza_A():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Mammiferi")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
def elimina_A():
    id = int(input("Inserisci l'ID dell'animale da eliminare: "))
    sql = "DELETE FROM Mammiferi WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Animale con ID {id} eliminato con successo.")

def modifica_A():
    id = int(input("Inserisci l'ID dell'animale da modificare: "))
    nome_proprio = input("Inserisci il nuovo nome proprio: ")
    razza = input("Inserisci la nuova razza: ")
    peso = int(input("Inserisci il nuovo peso (in kg): "))
    eta = int(input("Inserisci la nuova età: "))
    sql = "UPDATE Mammiferi SET Nome_Proprio = %s, Razza = %s, Peso = %s, Eta = %s WHERE id = %s"
    val = (nome_proprio, razza, peso, eta, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Animale con ID {id} modificato con successo.")

def menuSelezione():
    while True:
        print("\nMENU PER SELEIONE POSSIBILI OPZIONI:")
        print("1 - Inserisci un nuovo animale")
        print("2 - Visualizza tutti gli animali")
        print("3 - Elimina un animale")
        print("4 - Modifica un animale")
        print("0 - Esci")
        scelta = input("Seleziona un numero del Opzione: ")
        if scelta == '1':
            n = int(input("Quanti animali vuoi inserire? "))
            for _ in range(n):
                inserisci_A()
                if input("Vuoi continuare ad aggiungere animali? (s/n): ").lower() != 's':
                    break
        elif scelta == '2':
            visualizza_A()
        elif scelta == '3':
            elimina_A()
        elif scelta == '4':
            modifica_A()
        elif scelta == '0':
            print("Uscita dal programma.")
            break
        else:
            print("ERRORE:opzione non valida, riprova.")

menuSelezione()
