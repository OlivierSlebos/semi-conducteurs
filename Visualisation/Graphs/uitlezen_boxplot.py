import csv
import os

#script voor het uitlezen van de resultaten folder om later een boxplot van te kunnen maken 
def scores_boxplot_csv() -> None:
    """
    Deze functie wordt gebruik door "maak_boxplot()" om een csv te maken in het juiste format. Het leest de 
    resultaten uit de resultaten/Runs folder en zet in de eerste kolom het aantal treinen en in de tweede kolom de score. 

    De functie maakt een csv genaamd "scores_boxplot.csv" in de folder resultaten/Combined_Runs. 
    """

    #hoe moet de output heten 
    bestandsnaam = 'scores_boxplot.csv'
    
    #lijst van bestanden in de map maken
    bestanden = os.listdir("resultaten/Runs")
    
    #alleen bestanden selecteren, geen mappen
    bestanden = [bestand for bestand in bestanden if os.path.isfile(os.path.join("resultaten/Runs", bestand))]
    
    #csv schrijven
    with open(fr"resultaten/Combined_Runs/{bestandsnaam}", mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        #aantal treinen en bijbehorende score opschrijven
        for i, bestand in enumerate(bestanden):
            score = bestand.split('_')
            writer.writerow([score[1], score[2]])

if __name__ == "__main__":
    scores_boxplot_csv()