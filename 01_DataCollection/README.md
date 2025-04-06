# Data Collection

Crawler for bus data, collecting from the [Golemio API](https://api.golemio.cz/pid/docs/openapi/). The API has a rate limit of 20 requests per 8 seconds. This data will be placed inside `raw/data.db`.

Stop information has been downloaded from [Prague's Public Transport Opendata](https://opendata.praha.eu/datasets/https%3A%2F%2Fapi.opendata.praha.eu%2Flod%2Fcatalog%2F9a6a1d8e-45b9-41de-b9ae-0bcec7126876), and placed inside `raw/stops.csv`. Note that this is just for user convenience, and is not used to train the ML model.

# Installation

Install dependencies: `python3`

Install Python modules: `requests`

# Configuration

Go to [Golemio Key Management](https://api.golemio.cz/api-keys/), create an account and an API key. The crawler will not work without one.

Next, create file `config.json`, with the following format:

```json
{
	"api": {
		"token": "[API Token]",
		"refresh_interval": [Delay between queries, in minutes],
		"lines": [List of lines to fetch]
	},
	"db": {
		"total_records": [The maximum amount of records in DB]
	}
}
```

# Usage

Just run `main.py`.

The crawler will periodically download bus information, as per `schema.sql`. It will do this every `api.refresh_interval` minutes.

`api.lines` can be left out, in that case the crawler will crawl *all* lines.

The crawler will stop once the DB reaches `db.total_records` records.

**The crawler runs in realtime, we advise running it nonstop for weeks straight.**