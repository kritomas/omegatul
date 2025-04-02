import pickle
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, ExtraTreesRegressor, BaggingRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score
import dataloader, config

def trainModel(model, model_name):
	model = Pipeline([("trans", dataloader.column_trans), ("model", model)])
	model.fit(dataloader.X_train, dataloader.y_train)
	y_pred = model.predict(dataloader.X_test)
	mse = root_mean_squared_error(dataloader.y_test, y_pred)
	print(model_name + " mean squared error: " + str(mse))
	print(model_name + " mse deviation:      " +  str(cross_val_score(model, dataloader.X, dataloader.y, n_jobs=-1, scoring="neg_root_mean_squared_error").std()))
	with open("models/ml_" + model_name + ".pickle", "wb") as file:
		pickle.dump(model, file)

# Linear
trainModel(LinearRegression(n_jobs=-1), "linear")

# Forest
#trainModel(RandomForestRegressor(n_jobs=-1, max_depth=config.conf["ml"]["max_tree_depth"], n_estimators=config.conf["ml"]["tree_count"]), "random_forest")
trainModel(AdaBoostRegressor(learning_rate=config.conf["ml"]["learning_rate"]), "ada_boost")
trainModel(GradientBoostingRegressor(n_estimators=config.conf["ml"]["gradient_boosts"], max_depth=config.conf["ml"]["max_tree_depth"], learning_rate=config.conf["ml"]["learning_rate"]), "gradient_boosting")
trainModel(ExtraTreesRegressor(n_jobs=-1, max_depth=config.conf["ml"]["max_tree_depth"]), "extra_trees")
#trainModel(BaggingRegressor(n_jobs=-1), "bagging")
trainModel(DecisionTreeRegressor(max_depth=config.conf["ml"]["max_tree_depth"]), "decision_tree")
trainModel(ExtraTreeRegressor(max_depth=config.conf["ml"]["max_tree_depth"]), "extra_tree")