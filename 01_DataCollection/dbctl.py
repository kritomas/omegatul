import sqlite3, os
import config

class DBContext:
	connection = None

	def __enter__(self):
		if DBContext.connection == None:
			DBContext.connection = sqlite3.connect(config.conf["db"]["db_path"])
		self.cursor = self.connection.cursor()
		return self.cursor
	def __exit__(self, exc_type, exc_value, traceback):
		self.connection.commit()

	@classmethod
	def _reset(cls):
		"""
		Resets the database. THIS WILL WIPE ALL DATA.
		"""
		if cls.connection != None:
			cls.connection.close()
		cls.connection = None
		os.remove(config.conf["db"]["db_path"])
		with open(config.conf["db"]["schema_path"]) as file:
			sql = file.read()
			with DBContext() as cursor:
				cursor.executescript(sql)

class DBController:
	def __init__(self):
		try:
			with DBContext() as cursor:
				cursor.execute("select is_ready from Controller;")
				res = cursor.fetchone()
				if res == None:
					raise Exception("DB not properly initialized")
				if res[0] != 1:
					raise Exception("DB not properly initialized")
		except:
			self._reset()
	def _reset(self):
		DBContext._reset()

	def countRecords(self):
		with DBContext() as cursor:
			cursor.execute("select count(*) from Vehicle;")
			res = cursor.fetchone()
			return res[0]

	def addVehicle(self, gtfs_trip_id, longitude, latitude, line_name, timestamp, position_state, vehicle_type):
		with DBContext() as cursor:
			cursor.execute("insert into Vehicle (gtfs_trip_id, longitude, latitude, line_name, timestamp, position_state, vehicle_type) values (?, ?, ?, ?, ?, ?, ?)", (gtfs_trip_id, longitude, latitude, line_name, timestamp, position_state, vehicle_type))