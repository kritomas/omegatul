# Application

The application for the actual prediction.

# Installation

Install dependencies: `python3`

Install Python libraries: `pandas`, `python-dateutil`, `requests`, `scikit-learn`

# Configuration

Once again, you need a [Golemio API Key](https://api.golemio.cz/api-keys/).

Create file `config.json`, with the following format:

```json
{
	"api": {
		"token": "[API Token]"
	},
	"ml": {
		"model_path": "[Path to model]"
	}
}
```

# Usage

Make sure that `ml.model_path` points to one of the models generated by the trainer.

Just run `python3 main.py`.