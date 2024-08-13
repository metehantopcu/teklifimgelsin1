# Python imajını temel alarak başla
FROM python:3.12.4

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .
EXPOSE 8000
# Gunicorn'u çalıştır
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
