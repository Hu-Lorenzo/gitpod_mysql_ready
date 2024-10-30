from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route("/")

def index():
    return "Hello world!"

@app.route("/books")
def books():
    return send_file('books.json')

@app.route("/Tokusatsu")
def books():
    return send_file('Tokusatsu.json')
if __name__ == "__main__":
 
    app.run()