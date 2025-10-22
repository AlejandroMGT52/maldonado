from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensaje": "Aplicación funcionando correctamente"})

def sumar(a, b):
    return a + b

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
