import sqlite3, pickle, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import config

with sqlite3.connect(config.conf["db"]["db_path"]) as conn:
	data = pd.read_sql("select line_name, direction, unixepoch(start_timestamp) as start_timestamp, (unixepoch(timestamp) - unixepoch(start_timestamp)) as duration, latitude, longitude from Vehicle;", conn)

categorical_cols = ["line_name", "direction"]
column_trans = ColumnTransformer([
   ('ohe', OneHotEncoder(categories='auto'),['line_name', 'direction']),
], remainder='passthrough')

input_attr = ["line_name", "direction", "start_timestamp", "duration"]
output_attr = ["latitude", "longitude"]

X_train, X_test, y_train, y_test = train_test_split(data[input_attr], data[output_attr], test_size=0.25)

model = Pipeline([("trans", column_trans), ("rfr", RandomForestRegressor(n_jobs=-1))])
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred, squared=False)

print(mae)
print(mse)
with open("model.pickle", "wb") as file:
	pickle.dump(model, file)