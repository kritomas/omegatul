import time, pickle
from datetime import datetime
import pandas as pd

# Example ISO 8601 timestamp
iso_timestamp = "2024-03-30T00:00:00Z"

# Convert to datetime object
dt = datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%SZ")

# Convert to Unix timestamp
unix_timestamp = int(time.mktime(dt.timetuple()))

print(unix_timestamp)

with open("models/model.pickle", "rb") as file:
	model = pickle.load(file)


sample = pd.DataFrame([["154", "Sídliště Libuš", unix_timestamp, 1050]], columns=["line_name", "direction", "start_timestamp", "duration"])

print(model.predict(sample))