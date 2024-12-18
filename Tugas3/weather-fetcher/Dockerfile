# Gunakan image dasar Python
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy file requirements.txt dan install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy semua file aplikasi ke dalam container
COPY . .

# Jalankan script
CMD ["python", "weather_fetcher.py"]
