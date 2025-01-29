import csv
import os

#script voor het uitlezen van de resultaten folder om later een boxplot van te kunnen maken 
def scores_boxplot_csv() -> None:

    #hoe moet de output heten 
    bestandsnaam = 'scores_boxplot.csv'
    
    #lijst van bestanden in de map maken
    bestanden = os.listdir("resultaten/Runs")
    
    #alleen bestanden selecteren, geen mappen
    bestanden = [bestand for bestand in bestanden if os.path.isfile(os.path.join("resultaten/Runs", bestand))]
    
    #csv schrijven
    with open(fr"Visualisation/Graphs/{bestandsnaam}", mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        #aantal treinen en bijbehorende score opschrijven
        for i, bestand in enumerate(bestanden):
            score = bestand.split('_')
            writer.writerow([score[1], score[2]])

if __name__ == "__main__":
    scores_boxplot_csv()