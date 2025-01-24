import csv
import os

def scores_boxplot_csv() -> None:

    bestandsnaam = 'scores_boxplot.csv'
    
    # Lijst van bestanden in de map ophalen
    bestanden = os.listdir("resultaten")
    
    # Alleen bestanden selecteren, geen mappen
    bestanden = [bestand for bestand in bestanden if os.path.isfile(os.path.join("resultaten", bestand))]
    
    # CSV schrijven
    with open(fr"Docs/{bestandsnaam}", mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        
        # Bestandnamen en nummers schrijven
        for i, bestand in enumerate(bestanden):
            score = bestand.split('_')
            writer.writerow([score[1], score[2]])

if __name__ == "__main__":
    scores_boxplot_csv()