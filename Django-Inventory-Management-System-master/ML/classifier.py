import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pickle
from sklearn.metrics import accuracy_score, classification_report

# Assume 'traffic_data' is your DataFrame

# Read the traffic data
traffic_data = pd.read_csv('/home/gilles-tuf/Desktop/UbuntuBoris/project/predict_trafic/Django-Inventory-Management-System-master/ML/traffic1.csv', sep=";")

#print(traffic_data)


# Feature Engineering
traffic_data['DateTime'] = pd.to_datetime(traffic_data['DateTime'], format='%d/%m/%Y %H:%M', dayfirst=True)
traffic_data['HourOfDay'] = traffic_data['DateTime'].dt.hour
traffic_data['DayOfWeek'] = traffic_data['DateTime'].dt.dayofweek

# Encode categorical variable 'Junction'
traffic_data = pd.get_dummies(traffic_data, columns=['Junction'], drop_first=True)


# Define features and target
features = ['HourOfDay', 'DayOfWeek', 'Junction_2', 'Junction_3', 'Junction_4','Junction_5', 'Junction_6', 'Junction_7']
target = 'Vehicles'

# Set a threshold to classify as high or low traffic
threshold = 30  # You can adjust this threshold based on your problem

# Create a binary target variable
traffic_data['TrafficLevel'] = (traffic_data[target] > threshold).astype(int)

# Split the data into training and testing sets
train_data, test_data = train_test_split(traffic_data, test_size=0.3, random_state=50)

# Separate features and target in the training and testing sets
X_train, y_train = train_data[features], train_data['TrafficLevel']
X_test, y_test = test_data[features], test_data['TrafficLevel']

# Train a random forest classifier
classifier = RandomForestClassifier(random_state=50)
classifier.fit(X_train, y_train)

# Make predictions on the test set
predictions = classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
classification_report_str = classification_report(y_test, predictions)

pickle.dump(classifier, open('classifier', 'wb'))

# # Print the metrics
# print(f'Accuracy: {accuracy:.2%}')
# print('Classification Report:')
# print(classification_report_str)
