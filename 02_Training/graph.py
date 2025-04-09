import sqlite3, pandas as pd
import matplotlib.pyplot as plt
import config

trip_id = input("trip id: ")
with sqlite3.connect(config.conf["db"]["db_path"]) as conn:
	data = pd.read_sql("select distinct unixepoch(start_timestamp) as start_timestamp from Vehicle where position_state in ('at_stop', 'on_track') and gtfs_trip_id = ?;", conn, params=(trip_id,))
	#print(data)
if len(data) <= 0:
	raise ValueError("Unknown trip")
print(data["start_timestamp"])
start_time = int(input("start time: "))
with sqlite3.connect(config.conf["db"]["db_path"]) as conn:
	data = pd.read_sql("select concat(line_name, '/', direction) as line, unixepoch(start_timestamp) as starttimestamp, (unixepoch(timestamp) - unixepoch(start_timestamp)) as duration, latitude, longitude from Vehicle where position_state in ('at_stop', 'on_track') and gtfs_trip_id = ? and duration >= 0 and starttimestamp = ? order by duration;", conn, params=(trip_id, start_time))
	print(data)
if len(data) <= 0:
	raise ValueError("Unknown time")

plt.plot(data["longitude"], data["latitude"], linestyle='-', color='blue', alpha=0.3)
plt.plot(data["longitude"], data["latitude"], linestyle='', marker='+', color='blue', alpha=1.0)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()