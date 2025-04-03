import pickle
from sklearn.pipeline import Pipeline
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