import line
import predict

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
			print(v)
	def vehicle(self):
		vehicle_id = input("Enter vehicle ID: ")
		vehicle = line.fetchOne(vehicle_id)
		print(vehicle)

	def __init__(self):
		self.commands = {
			"exit": self.exit,
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