# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first (Docker layer caching optimization)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Environment variable for port (Cloud Run compatibility)
ENV PORT=8080

# Use gunicorn for production serving
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
#EOF
