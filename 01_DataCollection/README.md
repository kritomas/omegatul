# Data Collection

Public transport data has been collected from the [Golemio API](https://api.golemio.cz/pid/docs/openapi/). The API has a rate limit of 20 requests per 8 seconds.

Stop information has been taken out of the ZIP downloaded from [Prague's Public Transport Opendata](https://opendata.praha.eu/datasets/https%3A%2F%2Fapi.opendata.praha.eu%2Flod%2Fcatalog%2F9a6a1d8e-45b9-41de-b9ae-0bcec7126876) and placed inside `raw`. This CSV has then been imported into the crawled sqlite db and squashed with the collected data into a single table with:

```sql
select gtfs_trip_id, longitude, latitude, unixepoch(timestamp) as timestamp, unixepoch(start_timestamp) as start_timestamp,
last.stop_lon as last_stop_longitude, last.stop_lat as last_stop_latitue,
next.stop_lon as next_stop_longitude, next.stop_lat as next_stop_latitue
from Vehicle
inner join stops last on last_stop_id = last.stop_id
inner join stops next on next_stop_id = next.stop_id;
```