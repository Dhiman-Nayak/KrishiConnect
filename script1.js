// Function to fetch and update soil moisture data
function fetchSoilMoisture() {
    // Simulate fetching random data
    const simulatedSoilMoisture = getRandomNumber(20, 80); // Simulated soil moisture between 20% and 80%

    // Update the soil moisture element with the fetched data
    document.getElementById("soil-moisture").textContent = `${simulatedSoilMoisture}%`;
}

// Function to generate a random number between min and max (inclusive)
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Call the fetchSoilMoisture function initially to display data
fetchSoilMoisture();

// Set up an event listener for the refresh button
document.getElementById("refresh-button").addEventListener("click", fetchSoilMoisture);
