import requests
import numpy as np
import os
import matplotlib.pyplot as plt

url = "https://api.tomorrow.io/v4/weather/forecast?location=kolkata&timesteps=daily&apikey=NWbU1ceSDImxoVp6CmKLzUrXScmgL1c2"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
data = response.json()

daily_forecast = data['timelines']['daily'][:5]
rain_data = []

for day_data in daily_forecast:
    rain = day_data['values']['rainAccumulationAvg']
    rain_data.append(rain)

x1 = np.array([0, 1, 2, 3, 4])  # Use day indices as x-axis values
y1 = np.array(rain_data)

# Set tick labels for the x-axis
x_labels = [day_data['time'][:10] for day_data in daily_forecast]
plt.xticks(x1, x_labels, rotation=45)

subArray = [rain_data[0], rain_data[4]]
ids1 = np.nonzero(np.in1d(y1, subArray))[0]

plt.plot(x1, y1)
plt.plot(x1[ids1], y1[ids1], 'bo')

plt.xlabel('Date')
plt.ylabel('Rain Accumulation (Avg)')
plt.title('Predicted Rain Data')
plt.grid(True)

# Adjust the margins to ensure the entire plot is visible
plt.subplots_adjust(bottom=0.2)

plt.savefig(os.path.join('rain.png'))
print("Rain graph plotted!")
