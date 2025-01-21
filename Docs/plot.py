import matplotlib.pyplot as plt
import csv
import numpy as np

from uitlezen import scores_csv

from boxplot import maak_boxplot

def maak_binned_bargraph(data_csv, output_image, bin_size):

    maak_boxplot("Docs/scores_boxplot.csv", "boxplot_treinen_scores.png")

    scores_csv()

    try:
        # Data inlezen uit CSV-bestand
        scores = []
        with open(data_csv, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Header overslaan
            for row in reader:
                # Controleer op lege rijen of onvolledige data
                if len(row) == 2 and row[1].strip().replace('.', '', 1).isdigit():
                    scores.append(float(row[1]))
        
        # Bins maken
        min_score = int(min(scores) // bin_size) * bin_size
        max_score = int(max(scores) // bin_size + 1) * bin_size
        bins = np.arange(min_score, max_score + bin_size, bin_size)
        
        # Frequenties berekenen
        frequencies, bin_edges = np.histogram(scores, bins=bins)
        total = sum(frequencies)  # Totale aantal scores
        fractions = frequencies / total  # Fractie berekenen
        
        # Bar graph maken
        plt.figure(figsize=(12, 6))
        plt.bar(bin_edges[:-1], fractions, width=bin_size, color='skyblue', edgecolor='black', align='edge')
        plt.xlim(0, 10000)
        plt.title("Binned Scores (Fraction)", fontsize=16)
        plt.xlabel(f"Scores per (bin size = {bin_size})", fontsize=14)
        plt.ylabel("Fraction", fontsize=14)
        plt.xticks(bin_edges, rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Opslaan als afbeelding
        plt.savefig(output_image)
        print(f"Bargraph opgeslagen als {output_image}")
        plt.show()
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")


if __name__ == "__main__":

    # CSV-bestand met data
    data_csv = "Docs/scores.csv"  # Vervang dit door je CSV-bestand
    output_image = "binned_bargraph_fraction.png"
    bin_size = 300  # Pas de bin-grootte aan naar wens

    # Bargraph maken
    maak_binned_bargraph(data_csv, output_image, bin_size)
