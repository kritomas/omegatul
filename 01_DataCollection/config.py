import json

CONFIG_LOCATION = "./config.json"

with open(CONFIG_LOCATION) as file:
	conf = json.load(file)

if not "api" in conf:
	raise ValueError("Config entry api not found")
if not "token" in conf["api"]:
	raise ValueError("Config entry api.token not found")

if not isinstance(conf["api"]["token"], str):
	raise ValueError("Config entry api.token must be a string")

conf["db"] = {"db_path": "./data.db", "schema_path": "schema.sql"} # TODO