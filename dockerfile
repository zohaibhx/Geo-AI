FROM python:3.11-slim

# Install system-level geospatial dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables so Python can find GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY . .

CMD ["python", "main.py"]