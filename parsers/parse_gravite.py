fichier = open('/home/lucia/Desktop/Master2/DV/projet/usagers_2016.csv', 'r')

prepared_gravite = open('/home/lucia/Desktop/Master2/DV/projet/prepared_gravite', 'w')


prepared_gravite.write("gravite" + "\t" + "quantite")
prepared_gravite.write("\n")


tues = 0
indemnes = 0
blesses_hosp = 0
blesses_leger = 0


content = fichier.readlines()
content = [x.strip().split(",") for x in content] 
for i in range(1,len(content)):
	try:
		gravite = content[i][3]
		if gravite == '1':
			indemnes += 1
		if gravite == '2':
			tues += 1
		if gravite == '3':
			blesses_hosp += 1
		if gravite == '4':
			blesses_leger += 1

	except ValueError:
		pass 
	
prepared_gravite.write("indemnes" + "\t" + str(indemnes)+"\n")

prepared_gravite.write("tues" + "\t" + str(tues)+"\n")

prepared_gravite.write("blesses_hosp" + "\t" + str(blesses_hosp)+"\n")

prepared_gravite.write("blesses_leger" + "\t" + str(blesses_leger)+"\n")


