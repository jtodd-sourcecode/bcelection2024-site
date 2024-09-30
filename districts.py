import pandas as pd
import json
import re

def clean_whitespace(value):
    # Check if the value is a string
    if isinstance(value, str):
        # Use regex to replace multiple spaces with a single space
        return re.sub(r'\s+', ' ', value).strip()
    return value

# Load the CSV into a pandas DataFrame
csv_file_path = 'districts.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path, index_col=0)

# Apply the whitespace cleaning function to all values in the DataFrame
df_cleaned = df.applymap(clean_whitespace)

# Convert the cleaned DataFrame back into a dictionary and then into a JSON string
data_dict = df_cleaned.to_dict(orient='index')
json_data = json.dumps(data_dict, separators=(',', ':'))  # indent=4)

# Write the JSON string to a file
json_file_path = 'districts.json'  # Replace with desired output JSON file path
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"CSV has been converted back to JSON with cleaned whitespace and saved as '{json_file_path}'.")