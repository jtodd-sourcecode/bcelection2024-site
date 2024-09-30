import pandas as pd
import json

# Load the CSV into a pandas DataFrame
csv_file_path = 'districts.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path, index_col=0)

# Convert the DataFrame back into a dictionary and then into a JSON string
data_dict = df.to_dict(orient='index')
json_data = json.dumps(data_dict, indent=4)

# Write the JSON string to a file
json_file_path = 'districts.json'  # Replace with desired output JSON file path
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"CSV has been converted back to JSON and saved as '{json_file_path}'.")