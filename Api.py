from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return f"<h1>Hola mundo</h1>"

@app.route('/suma')
def suma():
    resultado = 5 + 5
    return f"<h1>5 + 5 = {resultado}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)