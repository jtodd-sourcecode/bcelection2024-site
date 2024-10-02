# BC Electoral Districts Map Website

## Project Overview
This project is a web-based interactive map of British Columbia’s electoral districts, allowing users to click on each district and be redirected to a corresponding Perplexity page with more information about that district. The site was built using **Mapbox** and **Perplexity.ai**, and is hosted on **GitHub Pages**. 

## Key Features
- **Interactive map**: Displays electoral districts of BC with clickable regions and markers.
- **Hosted on GitHub Pages**: Easily deployable and scalable using GitHub’s free hosting.
- **DNS Management**: Domain is managed through GoDaddy, with DNS pointing to GitHub Pages.

---

## Steps to Build the Website

### Sourcing the Electoral District Data
The 2023 electoral district boundaries were sourced from the **BC Data Catalogue**:
- I downloaded them as a **GeoJSON** file from the BC government’s open data portal.
- The GeoJSON file contained detailed geometry and properties for each district, including the district name (`ED_NAME`).

###  Converting the GeoJSON with Tippecanoe
- The original GeoJSON file was quite large and complex, so I used **Tippecanoe** to convert it into a **vector tileset** for efficient rendering.
- I ran **Tippecanoe** offline to set the zoom levels and simplify the data for better performance:
  `tippecanoe -o bc_elec.mbtiles -Z 3 -z 15 EBC_ELECTORAL_DISTS_BS11_SVW.geojson`. This conversion allowed the map to render smoothly even at various zoom levels, from a provincial view down to street-level details.

### Setting up the Map in Mapbox Studio

- I created a custom style in Mapbox Studio, using the uploaded tileset to display the electoral districts.
- The style was customized to show the district boundaries clearly, and I published it to make it available for my website.
- I then integrated this style into my website using Mapbox GL JS.
- I also generated a tile set using wildfire data that I got from the BC data catalogue

### Extracting District Names and Building the URL Mapping

- I used a Python script to extract the district names from the GeoJSON file and create json that maps each district name to a corresponding URL (using a placeholder URL for now):
```python
import json

# Load the GeoJSON file
with open('EBC_ELECTORAL_DISTS_BS11_SVW.geojson', 'r') as f:
    geojson = json.load(f)

# Create a dictionary with district names as keys and URLs as values
district_mapping = {feature['properties']['ED_NAME']: 'http://example.com' for feature in geojson['features']}

# Save the mapping to a JSON file
with open('district_mapping.json', 'w') as f:
    json.dump(district_mapping, f, indent=2)
```