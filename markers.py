import csv
import json
import geopy
import os

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
        geolong = float(row['latitude']) if row['latitude'] else None
        geolat = float(row['longitude']) if row['longitude'] else None
        
        if not geolat or not geolong:
            # Use the geopy library to get the coordinates from the address
            geolocator = geopy.Nominatim(user_agent='markers.py')
            location = geolocator.geocode(row['address'])
            if location:
                geolat = location.latitude
                geolong = location.longitude
                print(f"Update coordinates for {row['address']} are {geolat}, {geolong}")
            else:
                raise RuntimeError(f"Could not find coordinates for {row['address']}")  

        # Create a dictionary for each row and append it to the json_data list
        json_data.append({
            'address': row['address'],
            'coordinates': [geolong, geolat],
            'title': row['title'],
            'summary': row['summary'],
            'icon': row['icon'],
        })

# Define the JSON output file
json_file = 'markers.json'

# Write the list to a JSON file
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(json_data, file, separators=(',', ':'))

file_size = os.path.getsize(json_file) / 1024 # Get size in bytes
print(f"{json_file} created! Size: {file_size:.2f} KB")
