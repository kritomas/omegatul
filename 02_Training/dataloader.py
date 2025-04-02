import sqlite3, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import config

with sqlite3.connect(config.conf["db"]["db_path"]) as conn:
	data = pd.read_sql("select concat(line_name, '/', direction) as line, unixepoch(start_timestamp) as start_timestamp, (unixepoch(timestamp) - unixepoch(start_timestamp)) as duration, latitude, longitude from Vehicle where position_state in ('at_stop', 'on_track');", conn)
	#print(data.head())

categorical_cols = ["line"]
column_trans = ColumnTransformer([
   ('ohe', OneHotEncoder(categories='auto'), categorical_cols),
], remainder='passthrough')

input_attr = ["latitude", "longitude", "line", "start_timestamp"]
output_attr = "duration"

X = data[input_attr]
y = data[output_attr]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config.conf["ml"]["test_size"])