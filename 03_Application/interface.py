import time, dateutil
import line

class Interface:
	def exit(self):
		self.running = False
	def line(self):
		try:
			number, direction = input("Enter line ('number/direction'): ").split("/", 1)
		except ValueError:
			raise ValueError("Incorrectly formatted line")
		vehicles = line.fetch(number, direction)
		for v in vehicles:
			info = v["properties"]["vehicle_id"] + ": "
			info += "Currently at " + str(v["geometry"]["coordinates"][0]) + "E " + str(v["geometry"]["coordinates"][1]) + "N, "
			info += "started at " + v["properties"]["gtfs"]["properties"]["trip"]["start_timestamp"]
			duration = int(time.mktime(dateutil.parser.parse(v["properties"]["gtfs"]["properties"]["last_position"]["origin_timestamp"]).timetuple())) -int(time.mktime(dateutil.parser.parse(v["properties"]["gtfs"]["properties"]["trip"]["start_timestamp"]).timetuple()))
			duration_minutes = int(duration / 60)
			duration_seconds = duration % 60
			if duration > 0:
				info += " (" + str(duration_minutes) + "min " + str(duration_seconds) + "s into its journey)"
			else:
				info += " (not on track yet)"
			print(info)

	def __init__(self):
		self.commands = {
			"exit": self.exit,
			"line": self.line
		}

	def start(self):
		self.running = True
		while self.running:
			try:
				cmd = input(": ")
				if cmd in self.commands:
					self.commands[cmd]()
				else:
					print("Unknown command")
			except EOFError:
				self.running = False

interface = Interface()
interface.start()