from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

db_config = {
    'host': 'localhost',      
    'user': 'root',     
    'password': '', 
    'database': 'Animali'  
}

@app.route('/dati', methods=['GET'])
@app.route('/dati/<filtro>/<valore>', methods=['GET'])
@app.route('/dati/<filtro>/<valore_min>/<valore_max>', methods=['GET'])
def get_data(filtro=None, valore=None, valore_min=None, valore_max=None):
    try:
       
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
       
        query = "SELECT * FROM Mammiferi"
        params = ()

        
        if filtro and valore and not valore_min and not valore_max:
            if filtro in ['id','Nome_Proprio', 'Razza', 'Peso', 'eta']:
                query += f" WHERE {filtro} = %s"
                params = (valore,)
        elif filtro and valore_min and valore_max:
            if filtro in ['eta', 'Peso', 'id']:  
                query += f" WHERE {filtro} BETWEEN %s AND %s"
                params = (valore_min, valore_max)
        
      
        cursor.execute(query, params)
        result = cursor.fetchall()

      
        return jsonify(result)
    
    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile connettersi al database"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app.run()
