from ML.classifier import *

import pandas as pd
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
import pickle

# Assume 'classifier' is your trained RandomForestClassifier
# Assume 'features' is a list of feature names used in training the model

def predict_traffic_level(input_date, hour_of_day, junction):
    # Convert input_date to a datetime object
    input_datetime = datetime.strptime(input_date, '%Y-%m-%d %H:%M:%S')
    
    # Determine the day of the week (Monday is 0, Sunday is 6)
    day_of_week = input_datetime.weekday()
    
    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'HourOfDay': [hour_of_day],
        'DayOfWeek': [day_of_week],
        'Junction_2': [1 if junction == 2 else 0],
        'Junction_3': [1 if junction == 3 else 0],
        'Junction_4': [1 if junction == 4 else 0],
        'Junction_5': [1 if junction == 5 else 0],
        'Junction_6': [1 if junction == 6 else 0],
        'Junction_7': [1 if junction == 7 else 0]
    })
    
    # Make a prediction using the trained classifier
    infile = open("classifier", 'rb')
    modele_charge = pickle.load(infile)
    
    traffic_level = modele_charge.predict(input_data[features])[0]
    
    # Interpret the predicted traffic level
    if traffic_level == 0:
        return 0
    elif traffic_level == 1:
        return 1
    else:
        return -1

# # Example usage
# input_date = '2023-01-01 14:00:00'
# hour = 14  # Example hour of the day
# junction = 1  # Example junction

# predicted_traffic_level = predict_traffic_level(input_date, hour, junction)
# print(f'Predicted Traffic Level: {predicted_traffic_level}')
