import json, numbers

CONFIG_LOCATION = "./config.json"

with open(CONFIG_LOCATION) as file:
	conf = json.load(file)

if not "ml" in conf:
	raise ValueError("Config entry ml not found")
if not "test_size" in conf["ml"]:
	raise ValueError("Config entry ml.test_size not found")
if not "max_tree_depth" in conf["ml"]:
	raise ValueError("Config entry ml.max_tree_depth not found")
if not "tree_count" in conf["ml"]:
	raise ValueError("Config entry ml.tree_count not found")
if not "gradient_boosts" in conf["ml"]:
	raise ValueError("Config entry ml.gradient_boosts not found")
if not "learning_rate" in conf["ml"]:
	raise ValueError("Config entry ml.learning_rate not found")

if not isinstance(conf["ml"]["test_size"], numbers.Number):
	raise ValueError("Config entry ml.test_size must be a number")
if conf["ml"]["test_size"] <= 0 or conf["ml"]["test_size"] >= 1:
	raise ValueError("Config entry ml.test_size must be between 0 and 1")
if not (isinstance(conf["ml"]["max_tree_depth"], int) or conf["ml"]["max_tree_depth"] is None):
	raise ValueError("Config entry ml.max_tree_depth must be an integer or null")
if isinstance(conf["ml"]["max_tree_depth"], int) and conf["ml"]["max_tree_depth"] <= 0:
	raise ValueError("Config entry ml.max_tree_depth must positive")
if not isinstance(conf["ml"]["tree_count"], int):
	raise ValueError("Config entry ml.tree_count must be an integer")
if conf["ml"]["tree_count"] <= 0:
	raise ValueError("Config entry ml.tree_count must positive")
if not isinstance(conf["ml"]["gradient_boosts"], int):
	raise ValueError("Config entry ml.gradient_boosts must be an integer")
if conf["ml"]["gradient_boosts"] <= 0:
	raise ValueError("Config entry ml.gradient_boosts must positive")
if not isinstance(conf["ml"]["learning_rate"], numbers.Number):
	raise ValueError("Config entry ml.learning_rate must be a number")
if conf["ml"]["test_size"] <= 0 or conf["ml"]["learning_rate"] <= 0:
	raise ValueError("Config entry ml.learning_rate must be positive")

conf["db"] = {}
conf["db"]["db_path"] = "./data/data.db" # TODO