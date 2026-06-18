from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

modelo = joblib.load("modelo_rf.pkl")

@app.route("/")
def home():
    return render_template("formulario.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        brand = float(request.form["brand"])
        processor_speed = float(request.form["processor_speed"])
        ram_size = float(request.form["ram_size"])
        storage_capacity = float(request.form["storage_capacity"])
        screen_size = float(request.form["screen_size"])
        weight = float(request.form["weight"])

        datos = pd.DataFrame([{
            "Brand": brand,
            "Processor_Speed": processor_speed,
            "RAM_Size": ram_size,
            "Storage_Capacity": storage_capacity,
            "Screen_Size": screen_size,
            "Weight": weight
        }])

        precio = modelo.predict(datos)[0]

        return jsonify({"precio": round(float(precio), 2)})

    except Exception as e:
        return jsonify({"error": "Error: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)