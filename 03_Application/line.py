import requests, time
import config

def fetch(number, direction):
	headers = {"X-Access-Token": config.conf["api"]["token"], "User-Agent": "Omegatul"}
	vehicle_params = {"routeType": ["bus", "trolleybus"], "routeShortName": number}

	response = requests.get("https://api.golemio.cz/v2/public/vehiclepositions", headers=headers, params=vehicle_params)
	response.raise_for_status()
	data = response.json()
	result = []
	for vehicle in data["features"]:
		trip_id = vehicle["properties"]["gtfs_trip_id"]
		retrying = True
		while retrying:
			try:
				response = requests.get(f"https://api.golemio.cz/v2/vehiclepositions/{trip_id}", headers=headers)
				response.raise_for_status()
				retrying = False
				trip = response.json()
				vehicle["properties"]["gtfs"] = trip
				if trip["properties"]["trip"]["gtfs"]["trip_headsign"] == direction:
					result.append(vehicle)
			except requests.HTTPError as error:
				if error.response.status_code == 429: # 401=Bad Token, 429=Rate Limit
					time.sleep(1)
				elif error.response.status_code == 404:
					retrying = False
				else:
					raise
					retrying = False
					#print(error)
			except Exception as error:
				raise
				retrying = False
				#print(error)
	return result

def fetchOne(vehicle_id):
	headers = {"X-Access-Token": config.conf["api"]["token"], "User-Agent": "Omegatul"}
	vehicle_params = {"scopes": ["info"]}

	response = requests.get(f"https://api.golemio.cz/v2/public/vehiclepositions/{vehicle_id}", headers=headers, params=vehicle_params)
	response.raise_for_status()
	vehicle = response.json()
	vehicle["properties"] = vehicle
	vehicle["properties"]["vehicle_id"] = vehicle_id
	trip_id = vehicle["gtfs_trip_id"]
	retrying = True
	while retrying:
		try:
			response = requests.get(f"https://api.golemio.cz/v2/vehiclepositions/{trip_id}", headers=headers)
			response.raise_for_status()
			retrying = False
			trip = response.json()
			vehicle["gtfs"] = trip
		except requests.HTTPError as error:
			if error.response.status_code == 429: # 401=Bad Token, 429=Rate Limit
				time.sleep(1)
			elif error.response.status_code == 404:
				retrying = False
			else:
				raise
				retrying = False
				#print(error)
		except Exception as error:
			raise
			retrying = False
			#print(error)
	return vehicle