import requests, time
import dbctl, config

class Collector:
	def __init__(self):
		self.headers = {"X-Access-Token": config.conf["api"]["token"], "User-Agent": "Omegatul"}
		self.dbctl = dbctl.DBController()
		self.vehicle_params = {"routeType": ["bus", "trolleybus"]}

	def processVehicle(self, vehicle):
		trip_id = vehicle["properties"]["gtfs_trip_id"]
		retrying = True
		while retrying:
			try:
				response = requests.get(f"https://api.golemio.cz/v2/vehiclepositions/{trip_id}", headers=self.headers)
				response.raise_for_status()
				retrying = False
				trip = response.json()
				self.dbctl.addVehicle(trip["properties"]["trip"]["gtfs"]["trip_id"], trip["geometry"]["coordinates"][0], trip["geometry"]["coordinates"][1], trip["properties"]["trip"]["origin_route_name"], trip["properties"]["last_position"]["origin_timestamp"], trip["properties"]["last_position"]["state_position"], vehicle["properties"]["route_type"], trip["properties"]["last_position"]["last_stop"]["id"], trip["properties"]["last_position"]["next_stop"]["id"])
			except requests.HTTPError as error:
				if error.response.status_code == 429: # 401=Bad Token, 429=Rate Limit
					time.sleep(1)
				elif error.response.status_code == 404:
					retrying = False
				else:
					#raise
					retrying = False
					print(error)

	def start(self):
		while (self.dbctl.countRecords() < config.conf["db"]["total_records"]):
			print("New iteration:", time.strftime("%Y-%m-%dT%H:%M:%SZ"))
			start_time = time.time()
			retrying = True
			while retrying:
				try:
					response = requests.get("https://api.golemio.cz/v2/public/vehiclepositions", headers=self.headers, params=self.vehicle_params)
					response.raise_for_status()
					retrying = False
					data = response.json()
					for vehicle in data["features"]:
						self.processVehicle(vehicle)
				except requests.HTTPError as error:
					if error.response.status_code == 429: # 401=Bad Token, 429=Rate Limit
						time.sleep(1)
					else:
						#raise
						retrying = False
						print(error)
			total_time = time.time() - start_time
			delay = max(config.conf["api"]["refresh_interval"] - total_time, 0)
			time.sleep(delay)