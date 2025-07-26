FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Expose the Flask port (optional but good practice)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
