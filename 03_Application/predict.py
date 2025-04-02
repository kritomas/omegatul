import datetime
import pickle, pandas as pd
import config, line, vehicle, stop

class Predict:
	def exit(self):
		self.running = False
	def stop(self):
		name = input("Enter stop name: ")
		id = stop.lookup_name2id[name]
		start_unixtime = vehicle.Vehicle.iso2unix(self.vehicle.start_timestamp)
		sample = pd.DataFrame([[stop.lookup_id2latitude[id], stop.lookup_id2longitude[id], self.vehicle.line_number + "/" + self.vehicle.direction, start_unixtime]], columns=["latitude", "longitude", "line", "start_timestamp"])
		duration = int(self.model.predict(sample))
		duration_minutes = int(duration / 60)
		duration_seconds = duration % 60
		arrival = datetime.datetime.utcfromtimestamp(start_unixtime + duration).isoformat() + "Z"
		print("The bus will arrive at " + name + " at " + arrival + " (" + str(duration_minutes) + "min " + str(duration_seconds) + "s into its journey)")

	def __init__(self):
		with open(config.conf["ml"]["model_path"], "rb") as file:
			self.model = pickle.load(file)
		self.commands = {
			"exit": self.exit,
			"stop": self.stop
		}

	def start(self):
		vehicle_id = input("Enter vehicle ID: ")
		self.vehicle = line.fetchOne(vehicle_id)
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