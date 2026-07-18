## Flask API

Input: JSON features  
curl -X POST http://localhost:5000/predict \
 -H "Content-Type: application/json" \
 -d '{"features": [3,1,22,1,0,7.25,0,1,2,0]}'

Output: Prediction result  
Prediction: [0]


## Swagger API Docs
Swagger UI is integrated with Flasgger.

- Docs URL: https://data-analysis-project-swagger.onrender.com/apidocs
- Endpoints:
  - `/predict` → POST with JSON features
  - `/features` → GET expected feature names

You can test endpoints directly in the browser via Swagger UI.