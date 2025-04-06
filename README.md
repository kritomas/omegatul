# Pragabus

An ML model for predicting Prague's bus arrival times.

# Contents

A list of components making the whole thing tick. See Readme for each individual directory:

+	`01_DataCollection`: Crawler for downloading bus information. Stores it in a SQLite3 DB.
+	`02_Training`: Trains models on the data collected by `01_DataCollection`.
+	`03_Application`: The application doing the prediction.

# The Process

1.	Data Collection: See `01_DataCollection/README.md`.
2.	Training: See `02_Training/README.md`.
3.	Application: See `03_Application/README.md`.

# Credits

## Created by kritomas

With the help of classmates, our principal, ChatGPT, confused frantic googling that happened so mechanically that I forgot about it since then.

Source Code: https://github.com/kritomas/pragabus