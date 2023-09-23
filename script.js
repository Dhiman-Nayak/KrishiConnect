// Function to fetch and update temperature and humidity data
// function fetchTemperatureAndHumidity() {
//     // Simulate fetching random data
//     const simulatedTemperature = getRandomNumber(20, 35); // Simulated temperature between 20 and 35 degrees Celsius
//     const simulatedHumidity = getRandomNumber(30, 70); // Simulated humidity between 30% and 70%

//     // Update the temperature and humidity elements with the fetched data
//     document.getElementById("temperature").textContent = `${simulatedTemperature}°C`;
//     document.getElementById("humidity").textContent = `${simulatedHumidity}%`;
// }

// // Function to generate a random number between min and max (inclusive)
// function getRandomNumber(min, max) {
//     return Math.floor(Math.random() * (max - min + 1)) + min;
// }

// // Call the fetchTemperatureAndHumidity function initially to display data
// fetchTemperatureAndHumidity();

// // Set up an interval to refresh the data periodically (every 5 seconds in this example)
// setInterval(fetchTemperatureAndHumidity, 5000); // 5000 milliseconds = 5 seconds

// // Initialize the humidity gauge
// var humidityGauge = new JustGage({
//     id: "humidityGauge", // ID of the gauge div element
//     value: 50, // Initial humidity value
//     min: 0, // Minimum humidity value (0%)
//     max: 100, // Maximum humidity value (100%)
//     title: "Humidity", // Gauge title
//     label: "%", // Gauge label
//     valueFontColor: "#333", // Font color for the value
//     levelColors: ["#ff0000", "#ffff00", "#00ff00"], // Color ranges for the gauge
// });

// Simulate real-time temperature and humidity updates (replace with your real data source)
// function updateData() {
//     var temperatureValue = Math.floor(Math.random() * (40 - 10 + 1)) + 10; // Random temperature between 10 and 40
//     var humidityValue = Math.floor(Math.random() * (100 - 0 + 1)); // Random humidity between 0 and 100

//     document.getElementById("temperature").textContent = temperatureValue + " °C";
//     humidityGauge.refresh(humidityValue);
// }

// // Initialize the humidity gauge
// var humidityGauge = new JustGage({
//     id: "humidity",
//     value: 0,    // Initial humidity value (adjust as needed)
//     min: 0,      // Minimum value (0%)
//     max: 100,    // Maximum value (100%)
//     title: "Humidity",
//     label: "%",
//     gaugeWidthScale: 0.6, // Adjust the width of the gauge
// });

// // Update data every 2 seconds (simulated, replace with actual data)
// setInterval(updateData, 2000);

// Simulate real-time temperature and humidity updates (replace with your real data source)
function updateData() {
    var temperatureValue = Math.floor(Math.random() * (40 - 10 + 1)) + 10; // Random temperature between 10 and 40
    var humidityValue = Math.floor(Math.random() * (100 - 0 + 1)); // Random humidity between 0 and 100

    document.getElementById("temperature").textContent = temperatureValue + " °C";
    humidityGauge.refresh(humidityValue);
}

// Initialize the humidity gauge
var humidityGauge = new JustGage({
    id: "humidity",
    value: 0,    // Initial humidity value (adjust as needed)
    min: 0,      // Minimum value (0%)
    max: 100,    // Maximum value (100%)
    title: "Humidity",
    label: "%",
    gaugeWidthScale: 0.6, // Adjust the width of the gauge
});

// Update data every 2 seconds (simulated, replace with actual data)
setInterval(updateData, 2000);




