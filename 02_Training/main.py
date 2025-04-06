import sys

try:
	import pandas
except Exception as error:
	print("Error: Module `pandas` not installed")
	sys.exit(-1)
try:
	import sklearn
except Exception as error:
	print("Error: Module `scikit-learn` not installed")
	sys.exit(-1)
try:
	import tensorflow
except Exception as error:
	print("Error: Module `tensorflow` not installed")
	sys.exit(-1)

try:
	import config
except Exception as error:
	print("Config loading failed:", error)
	sys.exit(-1)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, ExtraTreesRegressor, BaggingRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from model import trainModel, trainNeurons
import dataloader

# Linear
trainModel(LinearRegression(n_jobs=-1), "linear")

# Forest
trainModel(RandomForestRegressor(n_jobs=-1, max_depth=config.conf["ml"]["max_tree_depth"], n_estimators=config.conf["ml"]["tree_count"]), "random_forest")
trainModel(AdaBoostRegressor(learning_rate=config.conf["ml"]["learning_rate"]), "ada_boost")
trainModel(GradientBoostingRegressor(n_estimators=config.conf["ml"]["gradient_boosts"], max_depth=config.conf["ml"]["max_tree_depth"], learning_rate=config.conf["ml"]["learning_rate"]), "gradient_boosting")
trainModel(ExtraTreesRegressor(n_jobs=-1, n_estimators=config.conf["ml"]["tree_count"], max_depth=config.conf["ml"]["max_tree_depth"]), "extra_trees")
trainModel(BaggingRegressor(n_jobs=-1, max_samples=config.conf["ml"]["max_samples"], n_estimators=config.conf["ml"]["estimators"]), "bagging")
trainModel(DecisionTreeRegressor(max_depth=config.conf["ml"]["max_tree_depth"]), "decision_tree")
trainModel(ExtraTreeRegressor(max_depth=config.conf["ml"]["max_tree_depth"]), "extra_tree")

# Neurons
neuro = Sequential()
neuro.add(Dense(config.conf["ml"]["density"], input_shape=(dataloader.X_train_trans.shape[1], ), activation="relu"))
neuro.add(Dropout(0.2))
for l in range(config.conf["ml"]["hidden_layers"]):
	neuro.add(Dense(config.conf["ml"]["density"], activation="relu"))
	neuro.add(Dropout(0.2))
neuro.add(Dense(1, activation="linear"))
neuro.compile(loss='mean_squared_error',
optimizer='adam',
metrics=['mae'])
trainNeurons(neuro, "neuro")