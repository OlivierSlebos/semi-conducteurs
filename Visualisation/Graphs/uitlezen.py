import csv
import os

#script voor het uitlezen van de resultaten folder om laten een staafdiagram van te kunnen maken 
def scores_csv() -> None:

    #hoe moet de output heten
    bestandsnaam = 'scores.csv'
    
    #lijst van bestanden in de map maken
    bestanden = os.listdir("Resultaten")
    
    #alleen bestanden selecteren, geen mappen
    bestanden = [bestand for bestand in bestanden if os.path.isfile(os.path.join("Resultaten", bestand))]
    
    #csv schrijven
    with open(fr"Docs/{bestandsnaam}", mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        #eerst het runnummer (onbelangrijk, vooral voor het onderscheiden van runs) en dan de score opschrijven 
        for i, bestand in enumerate(bestanden):
            score = bestand.split('_')
            writer.writerow([i, score[2]])


if __name__ == "__main__":
    scores_csv()