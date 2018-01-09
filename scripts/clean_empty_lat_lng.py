import csv
with open('../data/caracteristiques_2016.csv', newline='', encoding='latin-1') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		print(row[13])
