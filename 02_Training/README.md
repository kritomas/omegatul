# Training

Trainer for the ML model.

# Installation

Install dependencies: `python3`

Install Python libraries: `pandas`, `scikit-learn`

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