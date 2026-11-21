
from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "ml", "car_price_model.pkl")
LOOKUP_PATH = os.path.join(BASE_DIR, "..", "dataset", "car_specs.csv")

model = joblib.load(MODEL_PATH)
car_specs = pd.read_csv(LOOKUP_PATH)


@app.route("/")
def home():
    brands = sorted(car_specs["Brand"].dropna().unique().tolist())

    return render_template(
        "index.html",
        brands=brands
    )


@app.route("/get_models/<brand>")
def get_models(brand):
    models = car_specs[
        car_specs["Brand"] == brand
    ]["Name"].unique().tolist()

    return jsonify(sorted(models))


@app.route("/get_car_specs")
def get_car_specs():
    car_name = request.args.get("name")

    car = car_specs[
        car_specs["Name"] == car_name
    ]

    if car.empty:
        return jsonify({"error": "Car not found"}), 404

    car = car.iloc[0]

    specs = {
        "Fuel_Type": car["Fuel_Type"],
        "Transmission": car["Transmission"],
        "Mileage": float(car["Mileage"]),
        "Engine": float(car["Engine"]),
        "Power": float(car["Power"]),
        "Seats": float(car["Seats"])
    }

    return jsonify(specs)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        car_data = {
            "Location": request.form["Location"],
            "Year": int(request.form["Year"]),
            "Kilometers_Driven": int(request.form["Kilometers_Driven"]),
            "Fuel_Type": request.form["Fuel_Type"],
            "Transmission": request.form["Transmission"],
            "Owner_Type": request.form["Owner_Type"],
            "Mileage": float(request.form["Mileage"]),
            "Engine": float(request.form["Engine"]),
            "Power": float(request.form["Power"]),
            "Seats": float(request.form["Seats"]),
            "Brand": request.form["Brand"]
        }

        input_df = pd.DataFrame([car_data])

        prediction = model.predict(input_df)[0]

        return render_template(
            "index.html",
            brands=sorted(car_specs["Brand"].dropna().unique().tolist()),
            prediction=round(prediction, 2)
        )

    except (ValueError, KeyError):
        return render_template(
            "index.html",
            brands=sorted(car_specs["Brand"].dropna().unique().tolist()),
            error="Please enter valid car details."
        )


if __name__ == "__main__":
    app.run(debug=False)
