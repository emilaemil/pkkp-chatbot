# Dockerfile untuk aplikasi Flask

# Menggunakan base image Python Alpine
FROM python:3.8-alpine

# Set environment variables
ENV NIXPACKS_PATH=/opt/venv/bin:$NIXPACKS_PATH
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Membuat direktori kerja di dalam container
WORKDIR /app

# Menyalin file-file aplikasi ke dalam direktori kerja di dalam container
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Menjalankan aplikasi Flask
CMD ["flask", "run", "--host=0.0.0.0"]
