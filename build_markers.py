import csv
import json

# Define the CSV file path
csv_file = 'markers.csv'

# Create an empty list to store the JSON data
json_data = []

# Open the CSV file for reading
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV
    for row in reader:
        # Convert the latitude and longitude back to a coordinates list
        coordinates = [float(row['latitude']), float(row['longitude'])]
        
        # Create a dictionary for each row and append it to the json_data list
        json_data.append({
            'address': row['address'],
            'coordinates': coordinates,
            'title': row['title'],
            'summary': row['summary'],
            'icon': row['icon'],
            'url': row['url']
        })

# Define the JSON output file
json_file = 'markers.json'

# Write the list to a JSON file
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(json_data, file, separators=(',', ':'))

print(f"Data successfully written to {json_file}")