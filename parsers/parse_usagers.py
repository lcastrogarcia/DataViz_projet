fichier = open('/home/lucia/Desktop/Master2/DV/projet/usagers_2016.csv', 'r')

prepared_usagers_total = open('/home/lucia/Desktop/Master2/DV/projet/prepared_usagers_total', 'w')
prepared_usagers_femmes = open('/home/lucia/Desktop/Master2/DV/projet/prepared_usagers_femmes', 'w')
prepared_usagers_hommes = open('/home/lucia/Desktop/Master2/DV/projet/prepared_usagers_hommes', 'w')

prepared_usagers_total.write("age,valeur")
prepared_usagers_total.write("\n")
prepared_usagers_femmes.write("age,valeur")
prepared_usagers_femmes.write("\n")
prepared_usagers_hommes.write("age,valeur")
prepared_usagers_hommes.write("\n")

hommes_25 = 0
femmes_25 = 0
hommes_25_45 = 0
femmes_25_45 = 0
hommes_45_70 = 0
femmes_45_70 = 0
hommes_70 = 0
femmes_70 = 0


content = fichier.readlines()
content = [x.strip().split(",") for x in content] 
for i in range(1,len(content)):
	conducteur = content[i][2]
	if conducteur == '1':
		try:
			nais = int(content[i][10])
			age = 2016 - nais
			sexe = content[i][4]

			if sexe == '1':
				
				if age < 25:
					hommes_25 +=1
				if age >= 25 and age <=45:
					hommes_25_45 +=1
				if age >= 46 and age <=70:
					hommes_45_70 +=1
				if age > 70:
					hommes_70 +=1


			if sexe == '2':
				if age < 25:
					femmes_25 +=1
				if age >= 25 and age <=45:
					femmes_25_45 +=1
				if age >= 46 and age <=70:
					femmes_45_70 +=1
				if age > 70:
					femmes_70 +=1

		except ValueError:
			pass

def percentage(n1,n2,tot):
	return round(((n1+n2)/tot)*100,2)
	

total_general = hommes_25 + hommes_70 + hommes_25_45 + hommes_45_70 + femmes_25 + femmes_70 + femmes_25_45 + femmes_45_70
per_25 = percentage(hommes_25,femmes_25,total_general)
per_25_45 = percentage(hommes_25_45,femmes_25_45,total_general)
per_45_70 = percentage(hommes_45_70,femmes_45_70,total_general)
per_70 = percentage(hommes_70,femmes_70,total_general)

total_femmes = femmes_25 + femmes_25_45 + femmes_45_70 + femmes_70
total_hommes = hommes_25 + hommes_25_45 + hommes_45_70 + hommes_70

per_femmes_25 = percentage(femmes_25,0,total_femmes)
per_femmes_25_45 = percentage(femmes_25_45,0,total_femmes)
per_femmes_45_70 = percentage(femmes_45_70,0,total_femmes)
per_femmes_70 = percentage(femmes_70,0,total_femmes)


per_hommes_25 = percentage(hommes_25,0,total_hommes)
per_hommes_25_45 = percentage(hommes_25_45,0,total_hommes)
per_hommes_45_70 = percentage(hommes_45_70,0,total_hommes)
per_hommes_70 = percentage(hommes_70,0,total_hommes)

prepared_usagers_total.write("moins_25," + str(per_25)+"\n")

prepared_usagers_total.write("entre_25_45," + str(per_25_45)+"\n")

prepared_usagers_total.write("entre_45_70," + str(per_45_70)+"\n")

prepared_usagers_total.write("plus_70," + str(per_70)+"\n")


prepared_usagers_hommes.write("moins_25," + str(per_hommes_25)+"\n")

prepared_usagers_hommes.write("entre_25_45," + str(per_hommes_25_45)+"\n")

prepared_usagers_hommes.write("entre_45_70," + str(per_hommes_45_70)+"\n")

prepared_usagers_hommes.write("plus_70," + str(per_hommes_70)+"\n")



prepared_usagers_femmes.write("moins_25," + str(per_femmes_25)+"\n")

prepared_usagers_femmes.write("entre_25_45," + str(per_femmes_25_45)+"\n")

prepared_usagers_femmes.write("entre_45_70," + str(per_femmes_45_70)+"\n")

prepared_usagers_femmes.write("plus_70," + str(per_femmes_70)+"\n")

