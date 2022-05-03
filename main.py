import json

with open ("Python\Projects\Rhythm Game Sheet Convert\smalltest.json", encoding="utf8") as f:
	sdata = json.load(f)

# for all objects in the json file, return... whatever we want
for object in sdata:
	print(object["chartID"])