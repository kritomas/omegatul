import sys

try:
	import pandas
except Exception as error:
	print("Error: Module `pandas` not installed")
	sys.exit(-1)
try:
	import dateutil
except Exception as error:
	print("Error: Module `python-dateutil` not installed")
	sys.exit(-1)
try:
	import requests
except Exception as error:
	print("Error: Module `requests` not installed")
	sys.exit(-1)
try:
	import sklearn
except Exception as error:
	print("Error: Module `scikit-learn` not installed")
	sys.exit(-1)

try:
	import config
except Exception as error:
	print("Config loading failed:", error)
	sys.exit(-1)

import interface

i = interface.Interface()
i.start()