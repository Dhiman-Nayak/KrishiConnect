import joblib
import requests

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
    
    # Add your code here to calculate or fetch moisture data
    # For now, I'm setting it to a placeholder value
    
    
    # Append data to respective lists
    temperature_data.append(temperature)
    humidity_data.append(humidity)
    pressure_data.append(pressure)
    windspeed_data.append(windspeed)
    rain_data.append(rain)

# Print the extracted data for 5 days
# for day in range(5):
    # print(f"Day {day + 1} - Temperature: {temperature_data[day]}°C, Humidity: {humidity_data[day]}%, Pressure: {pressure_data[day]} hPa, Wind Speed: {windspeed_data[day]} m/s")


model = joblib.load('soil_moisture_model.pkl')

# Create a list of input values and reshape it to match the model's input format
for day in range(5):
    input_data = [[temperature_data[day], humidity_data[day], pressure_data[day]/10, windspeed_data[day], rain_data[day]]]

    # Make predictions
    soil_moisture_prediction = model.predict(input_data)

    # Print the predicted soil moisture value
    print(f"Predicted Soil Moisture for day{day+1}: {round(soil_moisture_prediction[0]*100, 2)}%")
