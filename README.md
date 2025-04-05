# Pragabus

An ML model for predicting Prague's bus arrival times.

# Contents

A list of components making the whole thing tick. See Readme for each individual directory:

+	`01_DataCollection`: Crawler for downloading bus information. Stores it in a SQLite3 DB.
+	`02_Training`: Trains models on the data collected by `01_DataCollection`.
+	`03_Application`: The application doing the prediction.