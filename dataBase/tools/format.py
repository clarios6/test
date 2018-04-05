import json

with open('tracks.geojson') as f:
    data = json.load(f)

print(json.dumps(data, indent=2, sort_keys=False))
print(data["features"][0][3])