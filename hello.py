import pandas as pd
import random

# Sample values
vehicle_types = ['car', 'bike']
services = ['repair', 'wash', 'full_service']

# Generate 100,000 rows of data
data = []
for i in range(1, 999901):
    user_id = i
    vehicle_type = random.choice(vehicle_types)
    previous_service = random.choice(services)
    history_length = random.randint(1, 4)
    service_history = ';'.join(random.choices(services, k=history_length))
    next_service = random.choice(services)
    
    data.append({
        'user_id': user_id,
        'vehicle_type': vehicle_type,
        'previous_service': previous_service,
        'service_history': service_history,
        'next_service': next_service
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('vehicle_service_data.csv', index=False)

print("CSV file with 100,000 rows has been created successfully.")
