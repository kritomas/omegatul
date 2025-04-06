# Training

Trainer for the ML model.

# Installation

Install dependencies: `python3`

Install Python modules: `pandas`, `scikit-learn`, `tensorflow`

# Configuration

Create file `config.json`, with the following format:

```json
{
	"ml":
	{
		"test_size": [Amount of testing data compared to training data],
		"max_tree_depth": [Maximum depth of tree based models],
		"tree_count": [Amount of trees of forest based models],
		"estimators": [Amount of estimators of meta-estimator models],
		"gradient_boosts": [The amount of boosts of gradient boost regression],
		"learning_rate": [The amount of of boosting models],
		"max_samples": [The amount of samples to train each estimator of estimator models],
		"epochs": [Training iterations of neural networks],
		"batch_size": [Amount of scenarios to train neural networks on at a time],
		"density": [Amount of neurons in a hidden layer],
		"hidden_layers": [Amount of hidden layers in a neural network]
	}
}
```

# Usage

First, place the whole SQLite3 DB created by the crawler inside `data`.

Then run `main.py`. The trainer will use the whole CPU (if possible). The resulting models will be pickled and placed inside `models`.

# Output

The trainer runs through all the models uncommented in `main.py`, and writes their mean squared error (lower is better), and mse deviation (lower is better / less overfitting).

# The Process

This is the second step in this whole ordeal. We got the database from step one, and cleaned it. The cleaning was straightforward thanks to the wonders of SQL, just run this query:

```sql
select concat(line_name, '/', direction) as line, unixepoch(start_timestamp) as start_timestamp, (unixepoch(timestamp) - unixepoch(start_timestamp)) as duration, latitude, longitude from Vehicle where position_state in ('at_stop', 'on_track');
```

The output of this query is then passed into the training cinemagics. The resulting model we got by fiddling with the numbers a while, until we landed at this config:

```json
{
	"ml":
	{
		"test_size": 0.25,
		"max_tree_depth": 15,
		"tree_count": 15,
		"estimators": 15,
		"max_samples": 0.8,
		"epochs": 80,
		"batch_size": 64,
		"density": 64,
		"hidden_layers": 10
	}
}
```

The best results we got were with the Bagging Regression, with a mse of around 320 and mse deviation of around 32.