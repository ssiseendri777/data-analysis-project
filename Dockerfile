# Dockerize the project

# Step 1: Use official Python image
FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy requirements first (for caching)
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Step 5: Copy project files
COPY . .
COPY models/random_forest_model.pkl models/

# Step 6: Default command (start Flask API)
CMD ["python", "app.py"]

