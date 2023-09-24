import joblib
import requests
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to get future dates
def get_future_dates(start_date, num_days):
    dates = []
    for day in range(num_days):
        date = start_date + timedelta(days=day)
        dates.append(date.strftime("%Y-%m-%d"))
    return dates

# API request to get future weather data
url = "https://api.tomorrow.io/v4/weather/forecast?location=kolkata&timesteps=daily&apikey=NWbU1ceSDImxoVp6CmKLzUrXScmgL1c2"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()  # Parse the JSON response

# Extract the daily forecast data for 5 days
daily_forecast = data['timelines']['daily'][:5]

# Initialize lists to store extracted data
temperature_data = []
humidity_data = []
pressure_data = []
windspeed_data = []
rain_data = []

# Extract data for each day
for day_data in daily_forecast:
    temperature = day_data['values']['temperatureAvg']
    humidity = day_data['values']['humidityAvg']
    pressure = day_data['values']['pressureSurfaceLevelAvg']
    windspeed = day_data['values']['windSpeedAvg']
    rain = day_data['values']['rainAccumulationAvg']
    
    temperature_data.append(temperature)
    humidity_data.append(humidity)
    pressure_data.append(pressure)
    windspeed_data.append(windspeed)
    rain_data.append(rain)

# Load the soil moisture prediction model
model = joblib.load('soil_moisture_model.pkl')

# Create a list of input values and reshape it to match the model's input format
input_data = []
for day in range(5):
    input_data.append([temperature_data[day], humidity_data[day], pressure_data[day]/10, windspeed_data[day], rain_data[day]])

# Make predictions for the next 5 days
soil_moisture_predictions = model.predict(input_data)

# Synthetic data for the previous 5 days (you can replace this with actual data)
synthetic_data = [0.60, 0.50, 0.55, 0.69, 0.63]

# Combine the previous and next 5 days of soil moisture data
soil_moisture_data = synthetic_data + list(soil_moisture_predictions)

# Get future dates
current_date = datetime.now()
future_dates = get_future_dates(current_date, 5)
past_dates = get_future_dates(current_date - timedelta(days=5), 5)

# Plot soil moisture data with different colors and labels
plt.plot(past_dates, synthetic_data, label='Previous 5 Days', color='blue', marker='o')
plt.plot(future_dates, soil_moisture_predictions, label='Next 5 Days', color='green', marker='o')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Add labels and legend
plt.xlabel('Date')
plt.ylabel('Soil Moisture Prediction')
plt.legend()
plt.title('Predicted Soil Moisture Data')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
