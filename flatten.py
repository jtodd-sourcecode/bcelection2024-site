import os
import json
from datetime import datetime

def generate_html():
    # Load your JSON data
    with open('districts.json', 'r') as file:
        districts = json.load(file)
    with open('markers.json', 'r') as file:
        markers = json.load(file)

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="canonical" href="https://24bc.ca/" />
    <title>2024 BC Election Visualized</title>
    <style>
        body {{
            font-family: sans-serif;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1, h2, h3 {{
            color: #2c3e50;
        }}
        .section {{
            margin-bottom: 30px;
        }}
        .district, .marker {{
            margin-bottom: 20px;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }}
    </style>
</head>
<body>
    <header>
        <h1>2024 BC Election. Visualized.</h1>
    </header>

    <main>
        <section class="section" id="districts">
            <h2>Electoral Districts</h2>
            {generate_districts_html(districts)}
        </section>

        <section class="section" id="markers">
            <h2>Important Locations</h2>
            {generate_markers_html(markers)}
        </section>
    </main>

    <footer>
        <p>&copy; 2024 BC Election Visualized. Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </footer>
</body>
</html>
    """

    return html

def generate_districts_html(districts):
    html = ""
    for name, info in districts.items():
        html += f"""
        <div class="district">
            <h3>{name}</h3>
            <p><a href="{info['url']}" target="_blank">Wikipedia Page</a></p>
            {info['summary']}
        </div>
        """
    return html

def generate_markers_html(markers):
    html = ""
    for marker in markers:
        html += f"""
        <div class="marker">
            <h3>{marker['title']}</h3>
            <p>Coordinates: {marker['coordinates'][0]}, {marker['coordinates'][1]}</p>
            {marker['summary']}
            <p>Icon: {marker['icon']}</p>
        </div>
        """
    return html

if __name__ == "__main__":
    html_file = 'index-rendered.html'
    html_content = generate_html()
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    file_size = os.path.getsize(html_file) / 1024 # Get size in kbytes
    print(f"{html_file} created! Size: {file_size:.2f} KB")