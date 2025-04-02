import time, dateutil
import stop

class Vehicle:
	@classmethod
	def iso2unix(cls, timestamp):
		return time.mktime(dateutil.parser.parse(timestamp).timetuple())

	def __init__(self, raw):
		self.raw = raw
		self.id =  raw["properties"]["vehicle_id"]
		self.longitude = raw["geometry"]["coordinates"][0]
		self.latitude = raw["geometry"]["coordinates"][1]
		self.start_timestamp = raw["properties"]["gtfs"]["properties"]["trip"]["start_timestamp"]
		self.timestamp = raw["properties"]["gtfs"]["properties"]["last_position"]["origin_timestamp"]
		self.next_stop = raw["properties"]["gtfs"]["properties"]["last_position"]["next_stop"]["id"]
		self.line_number = raw["properties"]["gtfs"]["properties"]["trip"]["gtfs"]["route_short_name"]
		self.direction = raw["properties"]["gtfs"]["properties"]["trip"]["gtfs"]["trip_headsign"]

	def __str__(self):
		info = ""
		info += self.id + ": "
		info += "Currently at " + str(self.longitude) + "E " + str(self.latitude) + "N, "
		info += "started at " + self.start_timestamp
		duration = int(Vehicle.iso2unix(self.timestamp)) -int(Vehicle.iso2unix(self.start_timestamp))
		duration_minutes = int(duration / 60)
		duration_seconds = duration % 60
		if duration > 0:
			info += " (" + str(duration_minutes) + "min " + str(duration_seconds) + "s into its journey)"
		else:
			info += " (not on track yet)"
		if self.next_stop != None:
			info += ", headed for " + stop.lookup_id2name[self.next_stop]
		return info