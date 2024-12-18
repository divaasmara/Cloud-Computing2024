<?php
$servername = "db";
$username = "root";
$password = "example";
$dbname = "weather_data";

// Buat koneksi
$conn = new mysqli($servername, $username, $password, $dbname);

// Periksa koneksi
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT city, temperature, description, timestamp FROM weather ORDER BY timestamp DESC LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // Output data dari setiap baris
  while($row = $result->fetch_assoc()) {
    echo "City: " . $row["city"]. " - Temperature: " . $row["temperature"]. " - Description: " . $row["description"]. " - Timestamp: " . $row["timestamp"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();
?>
