from flask import Flask, jsonify, request
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

@app.route('/dati/aggiungi', methods=['POST'])
def aggiungi_dati():
    try:
        dati = request.get_json()
        if not dati or not all(k in dati for k in ['Nome_Proprio', 'Razza', 'Peso', 'eta']):
            return jsonify({"errore": "Dati incompleti"}), 400
        nome_proprio = dati['Nome_Proprio']
        razza = dati['Razza']
        peso = dati['Peso']
        eta = dati['eta']
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = """
        INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, eta) 
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (nome_proprio, razza, peso, eta))

        conn.commit()

        return jsonify({"messaggio": "Dati inseriti con successo"}), 201
    
    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile connettersi al database"}), 500
    
    except Exception as e:
        print("Errore generico:", e)
        return jsonify({"errore": "Si è verificato un errore"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/dati/aggiorna/<int:id>', methods=['PUT'])
def aggiorna_dati(id):
    try:
        dati = request.get_json()
        if not dati or not any(k in dati for k in ['Nome_Proprio', 'Razza', 'Peso', 'eta']):
            return jsonify({"errore": "Dati incompleti"}), 400

        nome_proprio = dati.get('Nome_Proprio')
        razza = dati.get('Razza')
        peso = dati.get('Peso')
        eta = dati.get('eta')

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "UPDATE Mammiferi SET"
        updates = []

        if nome_proprio:
            updates.append(f" Nome_Proprio = %s")
        if razza:
            updates.append(f" Razza = %s")
        if peso:
            updates.append(f" Peso = %s")
        if eta:
            updates.append(f" eta = %s")

        if not updates:
            return jsonify({"errore": "Nessun campo da aggiornare"}), 400

        query += ",".join(updates) + " WHERE id = %s"
        params = tuple(valore for valore in [nome_proprio, razza, peso, eta] if valore is not None) + (id,)

        cursor.execute(query, params)

        conn.commit()

        return jsonify({"messaggio": f"Dati aggiornati per id {id} con successo"}), 200
    
    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile connettersi al database"}), 500
    
    except Exception as e:
        print("Errore generico:", e)
        return jsonify({"errore": "Si è verificato un errore"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/dati/elimina/<int:id>', methods=['DELETE'])
def elimina_dati(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "DELETE FROM Mammiferi WHERE id = %s"
        cursor.execute(query, (id,))

        if cursor.rowcount == 0:
            return jsonify({"errore": f"Nessun record trovato con id {id}"}), 404

        conn.commit()

        return jsonify({"messaggio": f"Record con id {id} eliminato con successo"}), 200
    
    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile connettersi al database"}), 500
    
    except Exception as e:
        print("Errore generico:", e)
        return jsonify({"errore": "Si è verificato un errore"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app.run()
