<?php
$host = 'mysql-weather';
$dbname = 'weatherdb';
$username = 'root';
$password = 'rootpassword';

try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $apiKey = "YOUR_API_KEY";
    $city = "Jakarta";
    $apiUrl = "http://api.openweathermap.org/data/2.5/weather?q=$city&appid=$apiKey";
    
    $response = file_get_contents($apiUrl);
    $data = json_decode($response, true);

    $temp = $data['main']['temp'];
    $weather = $data['weather'][0]['description'];

    $sql = "INSERT INTO weather (city, temperature, description) VALUES ('$city', '$temp', '$weather')";
    $conn->exec($sql);

    echo "Weather data saved successfully!";
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
