import matplotlib.pyplot as plt
import csv
from collections import defaultdict

from uitlezen_boxplot import scores_boxplot_csv

def maak_boxplot(data_csv, output_image):

    scores_boxplot_csv()

    try:
        # Data inlezen en groeperen op aantal treinen
        data = defaultdict(list)
        with open(data_csv, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Header overslaan
            for row in reader:
                if len(row) == 2:
                    trein = int(row[0])
                    score = float(row[1])
                    data[trein].append(score)
        
        # Data voorbereiden voor boxplot
        treinen = sorted(data.keys())  # Sorteer trein-nummers
        scores = [data[trein] for trein in treinen]
        
        # Boxplot maken
        plt.figure(figsize=(10, 6))
        plt.ylim(0, 10000)
        plt.boxplot(scores, labels=treinen, patch_artist=True, boxprops=dict(facecolor='skyblue', color='black'), )
        plt.title("Boxplot van Scores per Trein", fontsize=16)
        plt.xlabel("Aantal treinen (n)", fontsize=14)
        plt.ylabel("Kwaliteitsscore (K)", fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Opslaan als afbeelding
        plt.savefig(output_image)
        print(f"Boxplot opgeslagen als {output_image}")
        plt.show()
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

if __name__ == "__main__":


    data_csv = "Docs/scores_boxplot.csv"  # Vervang dit door je CSV-bestand
    output_image = "boxplot_treinen_scores.png"

    # Boxplot maken
    maak_boxplot(data_csv, output_image)
