# Data Analysis Project

First project using Python for data analysis.
<br>
Work in progress.
<br>
Creator - S SISEENDRI
<br>
MCA Student From Berhampur University

# Titanic Survival Prediction Project

## Overview

This project predicts Titanic passenger survival using machine learning.  
It was built step-by-step across 20 days, covering data cleaning, feature engineering, model training, tuning, validation, interpretability, and deployment.

## Workflow

- Day 1–7: Data preprocessing and cleaning
- Day 8–12: Model building and evaluation
- Day 13–17: Advanced modeling (tuning, validation, ensembles)
- Day 18–19: Deployment and interpretability
- Day 20: Final wrap-up and documentation

## Final Results

- Random Forest ROC-AUC: 0.87
- Gradient Boosting ROC-AUC: 0.89

## Repository Structure

- `data/` → dataset
- `notebooks/` → daily progress notebooks
- `models/` → saved models
- `README.md` → project documentation

## How to Run

```bash
git clone https://github.com/ssiseendri777/data-analysis-project.git
cd data-analysis-project
pip install -r requirements.txt
jupyter notebook notebooks/final_summary.ipynb
```

## Flask API

Input: JSON features  
curl -X POST http://localhost:5000/predict \
 -H "Content-Type: application/json" \
 -d '{"features": [3,1,22,1,0,7.25,0,1,2,0]}'

Output: Prediction result  
Prediction: [0]
