import datetime, requests
import pickle, pandas as pd
import config, line, vehicle, stop

class Predict:
	def _refresh(self, id):
		try:
			self.vehicle = line.fetchOne(id)
		except requests.HTTPError as error:
			if error.response.status_code == 404:
				raise ValueError("Unknown vehicle")
			else:
				raise

	def exit(self):
		self.running = False
	def help(self):
		print("exit - Exit")
		print("help - This")
		print("refresh - Reload vehicle from API")
		print("stop - Predict vehicle's arrival at stop")
	def refresh(self):
		self._refresh(self.vehicle.id)
		print(self.vehicle)
	def stop(self):
		name = input("Enter stop name: ")
		try:
			id = stop.lookup_name2id[name]
		except KeyError:
			raise ValueError("Unknown stop")
		if not name in self.vehicle.stops:
			raise ValueError("This bus does not run through the specified stop")
		start_unixtime = vehicle.Vehicle.iso2unix(self.vehicle.start_timestamp)
		sample = pd.DataFrame([[stop.lookup_id2latitude[id], stop.lookup_id2longitude[id], self.vehicle.line_number + "/" + self.vehicle.direction, start_unixtime]], columns=["latitude", "longitude", "line", "start_timestamp"])
		try:
			duration = int(self.model.predict(sample))
		except ValueError:
			raise ValueError("Line not present in ML model")
		duration_minutes = int(duration / 60)
		duration_seconds = duration % 60
		arrival = datetime.datetime.fromtimestamp(start_unixtime + duration).astimezone().isoformat()
		print("The bus will arrive at " + name + " at " + arrival + " (" + str(duration_minutes) + "min " + str(duration_seconds) + "s into its journey)")

	def __init__(self):
		with open(config.conf["ml"]["model_path"], "rb") as file:
			self.model = pickle.load(file)
		self.commands = {
			"exit": self.exit,
			"help": self.help,
			"refresh": self.refresh,
			"stop": self.stop
		}

	def start(self):
		vehicle_id = input("Enter vehicle ID: ")
		self._refresh(vehicle_id)
		print(self.vehicle)
		self.running = True
		while self.running:
			try:
				cmd = input("predict: ")
				if cmd in self.commands:
					self.commands[cmd]()
				else:
					print("Unknown command")
			except EOFError:
				print()
				self.running = False