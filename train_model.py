import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load the dataset
data = pd.read_csv('vehicle_service_data.csv')

# Feature encoding
data['vehicle_type'] = data['vehicle_type'].map({'car': 0, 'bike': 1})
data['previous_service'] = data['previous_service'].map({'repair': 0, 'wash': 1, 'full_service': 2})

# Features (vehicle type, previous service)
X = data[['vehicle_type', 'previous_service']]

# Target (next service)
y = data['next_service'].map({'repair': 0, 'wash': 1, 'full_service': 2})

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Save the model to a file
joblib.dump(knn, 'model.pkl')

print("Model trained and saved to model.pkl")
