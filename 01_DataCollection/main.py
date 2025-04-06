import sys

try:
	import requests
except Exception as error:
	print("Error: Module `requests` not installed")
	sys.exit(-1)

try:
	import config
except Exception as error:
	print("Config loading failed:", error)
	sys.exit(-1)

import collector

coll = collector.Collector()

coll.start()