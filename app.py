#Flask API for Predictions

from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load your trained model (adjust path if needed)
model = joblib.load("models/random_forest_model.pkl")

@app.route("/")
def home():
    return "Flask API is running. Use /predict endpoint."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Expect JSON input: {"features": [val1, val2, ...]}
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Run on port 5000 inside container
    app.run(host="0.0.0.0", port=5000)
