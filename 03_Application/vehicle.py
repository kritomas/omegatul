class Vehicle:
	def __init__(self, raw):
		self.id =  raw["properties"]["vehicle_id"]
		self.coordinate_e = raw["geometry"]["coordinates"][0]
		self.coordinate_n = raw["geometry"]["coordinates"][1]
		self.start_timestamp = raw["properties"]["gtfs"]["properties"]["trip"]["start_timestamp"]
		self.timestamp = raw["properties"]["gtfs"]["properties"]["last_position"]["origin_timestamp"]
		self.raw = raw