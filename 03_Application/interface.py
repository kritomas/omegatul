import requests
import line
import predict

class Interface:
	def exit(self):
		self.running = False
	def help(self):
		print("exit - Exit")
		print("help - This")
		print("line - Get vehicles on line")
		print("vehicle - Get specific vehicle")
		print("predict - Predict specific vehicle")
	def line(self):
		try:
			number, direction = input("Enter line ('number/direction'): ").split("/", 1)
		except ValueError:
			raise ValueError("Incorrectly formatted line")
		vehicles = line.fetch(number, direction)
		if len(vehicles) <= 0:
			raise ValueError("Unknown line or there are no vehicles on this line")
		for v in vehicles:
			print(v)
	def vehicle(self):
		vehicle_id = input("Enter vehicle ID: ")
		try:
			vehicle = line.fetchOne(vehicle_id)
		except requests.HTTPError as error:
			if error.response.status_code == 404:
				raise ValueError("Unknown vehicle")
			else:
				raise
		print(vehicle)

	def __init__(self):
		self.commands = {
			"exit": self.exit,
			"help": self.help,
			"line": self.line,
			"vehicle": self.vehicle,
			"predict": predict.Predict().start
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
				print()
				self.running = False

interface = Interface()
interface.start()