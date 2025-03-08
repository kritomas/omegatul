import json, numbers

CONFIG_LOCATION = "./config.json"

with open(CONFIG_LOCATION) as file:
	conf = json.load(file)

if not "api" in conf:
	raise ValueError("Config entry api not found")
if not "token" in conf["api"]:
	raise ValueError("Config entry api.token not found")
if not "refresh_interval" in conf["api"]:
	raise ValueError("Config entry api.refresh_interval not found")
if not "db" in conf:
	raise ValueError("Config entry db not found")
if not "total_records" in conf["db"]:
	raise ValueError("Config entry db.total_records not found")

if not isinstance(conf["api"]["token"], str):
	raise ValueError("Config entry api.token must be a string")
if not isinstance(conf["api"]["refresh_interval"], numbers.Number):
	raise ValueError("Config entry api.refresh_interval must be a number")
if conf["api"]["refresh_interval"] < 0:
	raise ValueError("Config entry api.refresh_interval must not be negative")
if not isinstance(conf["db"]["total_records"], int):
	raise ValueError("Config entry db.total_records must be an integer")
if conf["db"]["total_records"] < 1:
	raise ValueError("Config entry db.total_records must be positive")

conf["db"]["db_path"] = "./data.db" # TODO
conf["db"]["schema_path"] = "schema.sql" # TODO
conf["api"]["refresh_interval"] *= 60