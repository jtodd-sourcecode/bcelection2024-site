#!/bin/bash -e
source venv/bin/activate
rm -f districts.csv markers.csv
osascript export-csv.scpt
python districts.py
python markers.py
python flatten.py