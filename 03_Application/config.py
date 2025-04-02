import json, numbers

CONFIG_LOCATION = "./config.json"

with open(CONFIG_LOCATION) as file:
	conf = json.load(file)

if not "api" in conf:
	raise ValueError("Config entry api not found")
if not "token" in conf["api"]:
	raise ValueError("Config entry api.token not found")
if not "ml" in conf:
	raise ValueError("Config entry ml not found")
if not "model_path" in conf["ml"]:
	raise ValueError("Config entry ml.model_path not found")

if not isinstance(conf["api"]["token"], str):
	raise ValueError("Config entry api.token must be a string")
if not isinstance(conf["ml"]["model_path"], str):
	raise ValueError("Config entry ml.model_path must be a string")