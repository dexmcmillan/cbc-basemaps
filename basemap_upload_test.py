import requests
import json

# Load DW taken from auth.txt file in project root.
with open('./auth.txt', 'r') as f:
        DW_AUTH_TOKEN = f.read().strip()

# Open up the geojson I want to load as the base map.
with open("bc-kelowna-census_tracts.json") as f:
    jsonObject = json.load(f)


# Define headers for request below.
headers = {
    "Authorization": f"Bearer {DW_AUTH_TOKEN}",
    "Content-Type": "application/json"
}

id = "ce2uC"

r = requests.put(f"https://api.datawrapper.de/v3/charts/{id}/assets/{id}.map.json", headers=headers, json=json.dumps(jsonObject))

print(r)

chart = requests.get(f"https://api.datawrapper.de/v3/charts/{id}", headers=headers)

print(chart.json()["metadata"]['visualize'])