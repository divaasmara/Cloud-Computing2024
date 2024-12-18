# Gunakan image dasar Node.js
FROM node:14

# Set working directory
WORKDIR /app

# Copy package.json dan install dependencies
COPY package.json .
RUN npm install

# Copy semua file aplikasi ke dalam container
COPY . .

# Jalankan aplikasi
CMD ["npm", "start"]
