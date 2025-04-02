import time, dateutil
import line, stop

class Interface:
	def _formatVehicle(self, vehicle):
		info = ""
		info += vehicle.id + ": "
		info += "Currently at " + str(vehicle.coordinate_e) + "E " + str(vehicle.coordinate_n) + "N, "
		info += "started at " + vehicle.start_timestamp
		duration = int(time.mktime(dateutil.parser.parse(vehicle.timestamp).timetuple())) -int(time.mktime(dateutil.parser.parse(vehicle.start_timestamp).timetuple()))
		duration_minutes = int(duration / 60)
		duration_seconds = duration % 60
		if duration > 0:
			info += " (" + str(duration_minutes) + "min " + str(duration_seconds) + "s into its journey)"
		else:
			info += " (not on track yet)"
		if vehicle.next_stop != None:
			info += ", headed for " + stop.lookup_id2name[vehicle.next_stop]
		return info

	def exit(self):
		self.running = False
	def line(self):
		try:
			number, direction = input("Enter line ('number/direction'): ").split("/", 1)
		except ValueError:
			raise ValueError("Incorrectly formatted line")
		vehicles = line.fetch(number, direction)
		for v in vehicles:
			print(self._formatVehicle(v))
	def vehicle(self):
		vehicle_id = input("Enter vehicle ID: ")
		vehicle = line.fetchOne(vehicle_id)
		print(self._formatVehicle(vehicle))

	def __init__(self):
		self.commands = {
			"exit": self.exit,
			"line": self.line,
			"vehicle": self.vehicle
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