# Step 1: Use a tiny Python environment
FROM python:3.12-slim

# Step 2: Set the folder inside the container
WORKDIR /app

# Step 3: Copy your requirements and install them
# (If you don't have a requirements.txt yet, just comment this out)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy your app.py into the container
COPY app.py .

# Step 5: Tell Docker how to run your script
CMD ["python", "app.py"]
