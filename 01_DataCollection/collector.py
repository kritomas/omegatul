import requests, time
import dbctl, config

class Collector:
	def __init__(self):
		self.headers = {"X-Access-Token": config.conf["api"]["token"], "User-Agent": "Omegatul"}
		self.dbctl = dbctl.DBController()

	def processVehicle(self, vehicle):
		trip_id = vehicle["properties"]["gtfs_trip_id"]
		retrying = True
		while retrying:
			try:
				response = requests.get(f"https://api.golemio.cz/v2/vehiclepositions/{trip_id}", headers=self.headers)
				response.raise_for_status()
				retrying = False
				trip = response.json()
				self.dbctl.addVehicle(trip["properties"]["trip"]["gtfs"]["trip_id"], trip["geometry"]["coordinates"][0], trip["geometry"]["coordinates"][0], trip["properties"]["trip"]["origin_route_name"], trip["properties"]["last_position"]["origin_timestamp"], trip["properties"]["last_position"]["state_position"], vehicle["properties"]["route_type"])
			except requests.HTTPError as error:
				if error.response.status_code == 429: # 401=Bad Token, 429=Rate Limit
					time.sleep(1)
				else:
					raise

	def start(self):
		retrying = True
		while retrying:
			try:
				response = requests.get("https://api.golemio.cz/v2/public/vehiclepositions", headers=self.headers)
				response.raise_for_status()
				retrying = False
				data = response.json()
				for vehicle in data["features"]:
					self.processVehicle(vehicle)
			except requests.HTTPError as error:
				if error.response.status_code == 429: # 401=Bad Token, 429=Rate Limit
					time.sleep(1)
				else:
					raise