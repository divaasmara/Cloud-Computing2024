# Gunakan image dasar Nginx dan PHP-FPM
FROM nginx:alpine

# Copy file konfigurasi Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copy source code aplikasi
COPY . /usr/share/nginx/html

# Jalankan Nginx
CMD ["nginx", "-g", "daemon off;"]
