FROM python:3.10

# Install only necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Note: Use Docker environment variables or secrets for sensitive data, not hardcoded files

# Use exec form for CMD
CMD ["python3", "bot/main.py"]
