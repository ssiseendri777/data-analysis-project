from flask import Flask, request, jsonify
import joblib
import numpy as np
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Load model
model = joblib.load("models/random_forest_model.pkl")

@app.route("/")
def home():
    return "Flask API is running. Use /predict endpoint."

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict survival based on Titanic features
    ---
    parameters:
      - name: features
        in: body
        type: array
        required: true
        description: List of 10 feature values in order
        schema:
          type: object
          properties:
            features:
              type: array
              items:
                type: number
              example: [3,1,22,1,0,7.25,0,1,2,0]
    responses:
      200:
        description: Prediction result
        schema:
          type: object
          properties:
            prediction:
              type: integer
    """
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/features", methods=["GET"])
def features():
    """
    Get expected feature names
    ---
    responses:
      200:
        description: List of expected features
        schema:
          type: object
          properties:
            expected_features:
              type: array
              items:
                type: string
    """
    return jsonify({"expected_features": list(model.feature_names_in_)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
