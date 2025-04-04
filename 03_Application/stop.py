import csv

lookup_name2id = {}
lookup_id2name = {}
lookup_id2longitude = {}
lookup_id2latitude = {}

with open("stops.csv", newline="", encoding="utf-8") as file:
	reader = csv.reader(file, delimiter=',', quotechar='"')
	for row in reader:
		lookup_id2name[row[0]] = row[1]
		lookup_name2id[row[1]] = row[0]
		lookup_id2longitude[row[0]] = row[3]
		lookup_id2latitude[row[0]] = row[2]