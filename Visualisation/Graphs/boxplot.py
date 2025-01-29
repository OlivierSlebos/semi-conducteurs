import matplotlib.pyplot as plt
import csv
from collections import defaultdict

from uitlezen_boxplot import scores_boxplot_csv

def maak_boxplot(data_csv, output_image):
    """
    Deze functie is geimplementeerd om een boxplot te maken van de verkregen resultaten. Hij werkt door eerst een csv te maken 
    van de behaalde scores met de functie "scores_boxplot_csv()". Deze zet in de eerste kolom het aantal treinen, en in de tweede de score.
    Dan maakt deze functie een boxplot van de scores. Het figuur komt in de folder Graphs. 

    Als de originele git structuur wordt aangehouden hoeft niks aangepast te worden om automatisch de plot te maken bij het roepen van 
    python3 Visualisation/Graphs/plot.py. Als er andere folders gebruikt moeten worden dan moet de invoer van de functies op een juiste
    wijze worden aangepast. 

    """

    #uitlezen in het format voor de boxplot 
    scores_boxplot_csv()

    #kijken of het uitlezen gelukt is 
    try:
        #data inlezen en groeperen op aantal treinen
        data = defaultdict(list)
        with open(data_csv, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  #header overslaan
            for row in reader:
                if len(row) == 2:
                    trein = int(row[0])
                    score = float(row[1])
                    data[trein].append(score)
        
        #data voorbereiden voor boxplot
        treinen = sorted(data.keys())  # Sorteer trein-nummers
        scores = [data[trein] for trein in treinen]
        
        #boxplot maken
        plt.figure(figsize=(10, 6))
        plt.ylim(0, 10000)
        plt.boxplot(scores, labels=treinen, patch_artist=True, boxprops=dict(facecolor='skyblue', color='black'), )
        plt.title("Boxplot van Scores per Trein", fontsize=16)
        plt.xlabel("Aantal treinen (n)", fontsize=14)
        plt.ylabel("Kwaliteitsscore (K)", fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        #opslaan als afbeelding
        plt.savefig(output_image)
        print(f"Boxplot opgeslagen als {output_image}")
        plt.show()
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")
