import requests
import dbctl, config

class Collector:
	def __init__(self):
		self.headers = {"X-Access-Token": config.conf["api"]["token"], "User-Agent": "Omegatul"}
		self.dbctl = dbctl.DBController()

	def start(self):
		try:
			response = requests.get("https://api.golemio.cz/v2/public/vehiclepositions", headers=self.headers)
			response.raise_for_status()
			data = response.json()
			print(data)
			print(response.status_code)
			print(response.headers)
		except requests.HTTPError as error:
			print(error.response.status_code) # 401=Bad Token, 429=Rate Limit