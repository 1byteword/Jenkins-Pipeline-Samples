import json
import os
from collections import OrderedDict

with open('jenkinstest.json', "r+") as jsonFile:
	data = json.load(jsonFile, object_pairs_hook=OrderedDict)

#	tmp = data["location"]
	data["parameters"]["adminUsername"]["value"] = os.environ["username"]
	data["parameters"]["adminPassword"]["value"] = os.environ["password"]

	jsonFile.seek(0)
	json.dump(data, jsonFile, indent=4)
	jsonFile.truncate()
