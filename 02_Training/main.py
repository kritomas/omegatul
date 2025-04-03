import config
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, ExtraTreesRegressor, BaggingRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from model import trainModel

# Linear
#trainModel(LinearRegression(n_jobs=-1), "linear")

# Forest
#trainModel(RandomForestRegressor(n_jobs=-1, max_depth=config.conf["ml"]["max_tree_depth"], n_estimators=config.conf["ml"]["tree_count"]), "random_forest")
#trainModel(AdaBoostRegressor(learning_rate=config.conf["ml"]["learning_rate"]), "ada_boost")
#trainModel(GradientBoostingRegressor(n_estimators=config.conf["ml"]["gradient_boosts"], max_depth=config.conf["ml"]["max_tree_depth"], learning_rate=config.conf["ml"]["learning_rate"]), "gradient_boosting")
trainModel(ExtraTreesRegressor(n_jobs=-1, n_estimators=config.conf["ml"]["tree_count"], max_depth=config.conf["ml"]["max_tree_depth"]), "extra_trees")
#trainModel(BaggingRegressor(n_jobs=-1), "bagging")
#trainModel(DecisionTreeRegressor(max_depth=config.conf["ml"]["max_tree_depth"]), "decision_tree")
#trainModel(ExtraTreeRegressor(max_depth=config.conf["ml"]["max_tree_depth"]), "extra_tree")