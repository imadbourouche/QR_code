

import pandas as pd

#example of data : https://docs.google.com/spreadsheets/d/1_RGSL-m-p7IEn9K8_hZEZM8u7_BxAh32GIyZADwD0qk/edit?usp=sharing
#example of stat file : https://docs.google.com/spreadsheets/d/1ERQOn6dbSeKpLLMJ8n3uFPh4tWaxgCox89vO8S9v7xY/edit?usp=sharing
#calculate the statistics after the scan


def calculate_statistics(df) :
	nb_present = 0
	nb_anbsent=0
	#loop throught the data of the file to calculate the stat
	for x in range(1,len(df)+1):
		if(df.loc[x-1,DAY] == "non") :
			nb_anbsent+=1
		else:
			nb_present+=1
	return nb_present,nb_anbsent




def fill_file_stat(df,df_statistics):
	nb_present , nb_anbsent = calculate_statistics(df)

	pourcentage_presence = (nb_present/len(df))*100
	pourcentage_absence = (nb_anbsent/len(df))*100
	format_pourcentage_presence = "{:.2f}".format(pourcentage_presence)
	format_pourcentage_absence = "{:.2f}".format(pourcentage_absence)

	#check if the colom is filled or not to fill it
	if(df_statistics.loc[0,DAY] == "non") : df_statistics.loc[0,DAY] = str(nb_present)
	if(df_statistics.loc[1,DAY] == "non") : df_statistics.loc[1,DAY] = str(nb_anbsent)
	if(df_statistics.loc[2,DAY] == "non") : df_statistics.loc[2,DAY] = format_pourcentage_presence+" %"
	if(df_statistics.loc[3,DAY] == "non") : df_statistics.loc[3,DAY] = format_pourcentage_absence+" %"

	df_statistics.to_csv(PATH_statistics, index=False)


def show_the_stat(df):
	nb_present ,nb_anbsent =  calculate_statistics(df)

	pourcentage_presence = (nb_present/len(df))*100
	pourcentage_absence = (nb_anbsent/len(df))*100
	format_pourcentage_presence = "{:.2f}".format(pourcentage_presence)
	format_pourcentage_absence = "{:.2f}".format(pourcentage_absence)
	
	print("Nombre de presents = ",nb_present)
	print("nombre de absents = ",nb_anbsent)
	print("Pourcentage de presence = "+format_pourcentage_presence+" %")
	print("Pourcentage d'absence = "+format_pourcentage_absence+" %")





print("---------- STATISTICS ---------")

#global variable
PATH= "list.csv"
PATH_statistics = "statistics.csv"
DAY= str(input("Enter the day in the format dd/mm/yyyy : "))

#read the data from the csv files
df = pd.read_csv(PATH)
df_statistics = pd.read_csv(PATH_statistics)


while True:
	print("MENU\n1-SHOW STATISTICS\n2-FILL THE STAT FILE WITH STATISTICS\n0-EXIT\n")
	choix = int(input("ENTER YOUR CHOICE : "))

	if choix == 1 :
		print("------- SHOWING STATISTICS --------")
		show_the_stat(df)
		print("-----------------------\n")

	elif choix==2 :
		print("------ FILLING THE FILE WITH STAT -------")
		fill_file_stat(df,df_statistics)
		print("FILLING COMPLETED _/\n-----------------------\n")
	else :
		exit(0)