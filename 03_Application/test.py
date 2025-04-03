import time, pickle
import vehicle
import pandas as pd

# Example ISO 8601 timestamp
iso_timestamp = "2024-03-30T017:00:00Z"

# Convert to Unix timestamp
unix_timestamp = vehicle.Vehicle.iso2unix(iso_timestamp)

print(unix_timestamp)

with open("models/ml_extra_trees.pickle", "rb") as file:
	model = pickle.load(file)


sample = pd.DataFrame([[50.026882 ,14.508024 , "154/Strašnická", unix_timestamp]], columns=["latitude", "longitude", "line", "start_timestamp"])

print(model.predict(sample))