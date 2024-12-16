<?php
$apiKey = "YOUR_API_KEY";
$city = "Jakarta";
$apiUrl = "http://api.openweathermap.org/data/2.5/weather?q=$city&appid=$apiKey";

$response = file_get_contents($apiUrl);
$data = json_decode($response, true);

$temp = $data['main']['temp'];
$weather = $data['weather'][0]['description'];

echo "Weather in $city: $weather, Temperature: $temp K";
?>
