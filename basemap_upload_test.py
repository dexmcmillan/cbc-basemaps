import requests
import json

# Load DW taken from auth.txt file in project root.
with open('./auth.txt', 'r') as f:
        DW_AUTH_TOKEN = f.read().strip()

# Open up the geojson I want to load as the base map.
with open("./data/cities/sk-regina-census_tracts.geojson") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonObject["type"] = "Topology"
    jsonFile.close()


# Define headers for request below.
headers = {
    "Accept": "*/*",
    "Authorization": f"Bearer {DW_AUTH_TOKEN}",
    "Content-Type": "application/json"
}

id = "whDn4"

r = requests.put(f"https://api.datawrapper.de/v3/charts/{id}/assets/{id}.map.json", headers=headers, json=json.dumps(jsonObject))

print(r)