import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib  # for model persistence

# Load your dataset
data = pd.read_csv('combined.csv')

# Split data into features (X) and target (y)
X = data[['TEMP', 'RELHUMID', 'PRESS', 'WINDSP', 'PRECI']]
y = data['Moisture']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}")

# Save the trained model for future use
joblib.dump(model, 'soil_moisture_model.pkl')
