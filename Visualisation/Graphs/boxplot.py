import matplotlib.pyplot as plt
import csv
from collections import defaultdict

from Graphs.uitlezen_boxplot import scores_boxplot_csv

def maak_boxplot(data_csv, output_image):

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

if __name__ == "__main__":


    data_csv = "Docs/scores_boxplot.csv"  #naam van csv 
    output_image = "boxplot_treinen_scores.png"

    # Boxplot maken
    maak_boxplot(data_csv, output_image)
