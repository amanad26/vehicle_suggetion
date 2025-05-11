from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Route for service recommendation
@app.route('/recommend_service', methods=['POST'])
def recommend_service():
    data = request.get_json()  # Get data from POST request
    
    vehicle_type = data['vehicle_type']  # 0 = car, 1 = bike
    previous_service = data['previous_service']  # 0 = repair, 1 = wash, 2 = full_service
    
    # Prepare the input for prediction
    user_input = np.array([[vehicle_type, previous_service]])
    
    # Predict the next service
    recommended_service = model.predict(user_input)
    
    # Map the result back to the service name
    service_mapping = {0: 'repair', 1: 'wash', 2: 'full_service'}
    recommended_service_name = service_mapping[recommended_service[0]]
    
    return jsonify({'recommended_service': recommended_service_name})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
