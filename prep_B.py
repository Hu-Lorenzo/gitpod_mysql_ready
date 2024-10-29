
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Id,Nome_Proprio,Razza,Peso,eta) VALUES (%s, %s,%s, %s,%s)"
val = [
  ('1','Leo','Leone','190','8'),
  ('2','Bella','Elefante','6000','25'),
  ('3','Max','Orso Bruno','300','15'),
  ('4','Daisy','Zebra','350','6'),
  ('5','charlie','Gorilla','180','12'),
  
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
