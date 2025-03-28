import json, numbers

CONFIG_LOCATION = "./config.json"

with open(CONFIG_LOCATION) as file:
	conf = json.load(file)

conf["db"] = {}
conf["db"]["db_path"] = "./data/data.db" # TODO