## Render Deployment
This project is deployed on Render.

- API URL: https://data-analysis-project-api.onrender.com
- Endpoint: `/predict`
- Method: POST
- Input: JSON with 10 features in order:
  ["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked_Q","Embarked_S","FamilySize","IsAlone"]

Example:
```bash
 curl -X POST https://data-analysis-project-api.onrender.com/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [3,1,22,1,0,7.25,0,1,2,0]}'   

## Output in json
{"prediction":0}