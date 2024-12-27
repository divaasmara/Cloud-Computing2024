# Aplikasi Ramalan Cuaca
Repository ini adalah dokumentasi Final Project dari mata kuliah "Komputasi Awan" yaitu, aplikasi ramalan cuaca dengan menggunakan docker dan kubernetes (minikube).

## Anggota Kelompok:
1. Kartika Diva Asmara Gita (5025211039)
2. Hana Maheswari (5025211182)
3. Zakia Kolbi (5025211049)

## Berikut Langkah-Langkah Menjalankan Program:

### 1. Instalasi Docker

- Cek Versi Docker
docker --version

- Aktifkan & Jalankan Docker
sudo systemctl start docker
sudo systemctl enable docker

- Tambahkan ke Grup
sudo usermod -aG docker $USER

### 2. Instalasi Kubernetes (Minikube)

- Install Dependencies
sudo apt install -y curl apt-transport-https

- Install Kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

- Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube

- Mulai Minikube
minikube start 

- Cek cluster
kubectl cluster-info

### 3. Menyiapkan Projek,  Build, dan Push Docker Image

- Clone Repo GitHub
git clone https://github.com/divaasmara/Cloud-Computing2024.git
cd Cloud-Computing2024/Tugas5

- Build Docker Image
docker build -t weather_app:latest -f app/Dockerfile ./app

- Login Docker Hub
sudo docker login

- Tag & Push ke Docker Hub
sudo docker tag weather_app:latest eileithyi4l/weather_app:latest
sudo docker push eileithyi4l/weather_app:latest

note : ganti eileithyi4l dengan nama username docker hub kalian

### 4. Menyiapkan Kubernetes & Manifest Kubernetes

- Buat Namespace
kubectl create namespace weather-app

- Deployment & Service
kubectl apply -f k8s/deployment.yaml -n weather-app
kubectl apply -f k8s/service.yaml -n weather-app

### 5. Menjalankan & Memverifikasi

- Cek status Pod & Service
kubectl get pods -n weather-app
kubectl get svc -n weather-app

- Akses Aplikasi
minikube service weather-app-service -n weather-app

- Cek log Pod
kubectl logs -l app=weather-app -n weather-app

- tampilkan dashboard
minikube dashboard       

### 7. Re-Build Perubahan Baru

- Build Docker Image
docker build --no-cache -t eileithyi4l/weather_app:latest -f app/Dockerfile ./app

- Validasi Docker Image
docker run -p 5000:5000 eileithyi4l/weather_app:latest

- Push Image Baru
sudo docker push eileithyi4l/weather_app:latest

- Restart Deployment di Kubernetes (memastikan pod memuat image baru)
kubectl rollout restart deployment/weather-app -n weather-app

- Periksa Pod Baru 
kubectl get pods -n weather-app
kubectl describe pod <pod-name> -n weather-app

- Jalankan
minikube service weather-app-service -n weather-app

- Debug Log (buat cek aja, memastikan aplikasi membaca file HTML baru)
kubectl logs -l app=weather-app -n weather-app
