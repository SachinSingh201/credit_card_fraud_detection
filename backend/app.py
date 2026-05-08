from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import os

# =========================
# Flask App Configuration
# =========================

app = Flask(
    __name__,
    template_folder='../frontend/templates',
    static_folder='../frontend/static'
)

# =========================
# Base Directory
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================
# Load Models
# =========================

model = joblib.load(
    os.path.join(BASE_DIR, 'model/xgb_model.pkl')
)

scaler = joblib.load(
    os.path.join(BASE_DIR, 'model/scaler.pkl')
)

selected_features = joblib.load(
    os.path.join(BASE_DIR, 'model/selected_features.pkl')
)

# =========================
# Home Route
# =========================

@app.route('/')
def home():
    return render_template('index.html')

# =========================
# Prediction Route
# =========================

@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = request.get_json()

        input_df = pd.DataFrame([data])

        # Numeric columns for scaling
        scale_cols = [
            'amt',
            'city_pop',
            'lat',
            'long',
            'unix_time',
            'merch_lat',
            'merch_long'
        ]

        available_scale_cols = [
            col for col in scale_cols if col in input_df.columns
        ]

        if len(available_scale_cols) > 0:
            input_df[available_scale_cols] = scaler.transform(
                input_df[available_scale_cols]
            )

        # Add missing columns
        for col in selected_features:
            if col not in input_df.columns:
                input_df[col] = 0

        # Reorder columns
        input_df = input_df[selected_features]

        # Prediction
        prediction = model.predict(input_df)[0]

        probability = model.predict_proba(input_df)[0][1]

        result = (
            "Fraud Transaction"
            if prediction == 1
            else "Normal Transaction"
        )

        # Print result to terminal
        print(f"Prediction: {result} | Probability: {probability:.4f}")

        return jsonify({
            'prediction': result,
            'fraud_probability': float(probability)
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        })

# =========================
# Run App
# =========================

if __name__ == '__main__':
    app.run(debug=True)