from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

model = pickle.load(open('random_forest_model.pkl', 'rb'))
with open('feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)  # Assuming feature_names.pkl was saved during training

# home route
@app.route('/')
def home():
    return render_template('index.html')

# prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.form

        Mileage = float(input_data['Mileage'])
        Vehicle_color = input_data['Vehicle_color']
        Car_age = int(input_data['Car_age'])
        fuel = input_data['fuel']
        gearbox = input_data['gearbox']
        horsepower = float(input_data['horsepower'])
        car_body = input_data['car_body']

        #pepare a DataFrame
        raw_data = pd.DataFrame(
            [[Mileage, Vehicle_color, Car_age, fuel, gearbox, horsepower, car_body]],
            columns=['Mileage', 'Vehicle_color', 'Car_age', 'fuel', 'gearbox', 'horsepower', 'car_body']
        )

        encoded_data = pd.get_dummies(raw_data, columns=['Vehicle_color', 'fuel', 'car_body', 'gearbox'])

        for col in feature_names:
            if col not in encoded_data:
                encoded_data[col] = 0  # Add missing columns
        encoded_data = encoded_data[feature_names]  # Reorder columns to match training

        prediction = model.predict(encoded_data)[0]

        return jsonify({'predicted_price': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
