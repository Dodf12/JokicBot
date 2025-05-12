FROM python:3.8


# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libpq-dev \
    libx11-dev \
    libxext-dev \
    libxtst-dev \
    libssl-dev \
    libffi-dev \
    qt5-qmake \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install the dependencies
# Upgrade pip and install Python dependencies

RUN pip install --no-cache-dir --verbose -r requirements.txt




# Copy the rest of the application code
COPY . .

# Specify the command to run when the container starts
CMD python3 bot/main.py
