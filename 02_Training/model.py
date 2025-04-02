import pickle
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, ExtraTreesRegressor, BaggingRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
import dataloader

def trainModel(model, model_name):
	model = Pipeline([("trans", dataloader.column_trans), ("model", model)])
	model.fit(dataloader.X_train, dataloader.y_train)
	y_pred = model.predict(dataloader.X_test)
	mse = root_mean_squared_error(dataloader.y_test, y_pred)
	print(model_name + " mean squared error: " + str(mse))
	with open("models/ml_" + model_name + ".pickle", "wb") as file:
		pickle.dump(model, file)

# Linear
trainModel(LinearRegression(n_jobs=-1), "linear")

# Forest
trainModel(RandomForestRegressor(n_jobs=-1), "random_forest")
trainModel(AdaBoostRegressor(), "ada_boost")
trainModel(GradientBoostingRegressor(), "gradient_boosting")
trainModel(ExtraTreesRegressor(n_jobs=-1), "extra_trees")
trainModel(BaggingRegressor(n_jobs=-1), "bagging")
trainModel(DecisionTreeRegressor(), "decision_tree")
trainModel(ExtraTreeRegressor(), "extra_tree")