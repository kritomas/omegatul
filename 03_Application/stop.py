import csv

lookup_name2id = {}
lookup_id2name = {}

with open("stops.csv", newline="") as file:
	reader = csv.reader(file, delimiter=',', quotechar='"')
	for row in reader:
		lookup_id2name[row[0]] = row[1]
		lookup_id2name[row[1]] = row[0]