import matplotlib.pyplot as plt
import csv
import numpy as np

from uitlezen import scores_csv

from boxplot import maak_boxplot


#script voor het maken van een plot, waarbij de functie voor het maken van de boxplot ook automatisch wordt uitgevoerd 
def maak_binned_bargraph(data_csv, output_image, bin_size):

    """
    Deze functie is geimplementeerd om een staafdiagram te maken van de behaalde scores. Hij werkt door eerst een csv te maken van
    de behaalde scores met de functie "scores_csv". Hierin staat een run nummer in de eerste kolom en de score op de tweede kolom. 
    Op basis daarvan maakt deze functie het staafdiagram. 

    Deze functie is gecombineerd met de "maak_boxplot()" functie. Hierdoor wordt door het aanroepen van alleen deze functie beide een 
    boxplot en een staafdiagram gemaakt. De grafieken komen met bijbehorende namen in de folder Graphs. 

    Als de originele git structuur wordt aangehouden hoeft niks aangepast te worden om automatisch de plots te maken bij het roepen van 
    python3 Visualisation/Graphs/plot.py. Als er andere folders gebruikt moeten worden dan moet de invoer van de functies op een juiste
    wijze worden aangepast. 

    """

    #boxplot maken met juiste input 
    maak_boxplot("resultaten/Combined_Runs/scores_boxplot.csv", "Visualisation/Graphs/boxplot_treinen_scores.png")

    #scores uitlezen in het format voor de staafdiagram 
    scores_csv()

    #kijken of het uitlezen goed is gegaan met try 
    try:
        #data inladen vanuit de csv
        scores = []
        with open(data_csv, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  #header overslaan
            for row in reader:
                #controleren of er legen rijen zijn of andere fouten in de data
                if len(row) == 2 and row[1].strip().replace('.', '', 1).isdigit():
                    scores.append(float(row[1]))
        
        #bins maken per 300
        min_score = int(min(scores) // bin_size) * bin_size
        max_score = int(max(scores) // bin_size + 1) * bin_size
        bins = np.arange(min_score, max_score + bin_size, bin_size)
        
        #frequenties berekenen
        frequencies, bin_edges = np.histogram(scores, bins=bins)
        total = sum(frequencies)  # Totale aantal scores
        fractions = frequencies / total  # Fractie berekenen
        
        #staafdiagramg maken
        plt.figure(figsize=(12, 8))
        plt.bar(bin_edges[:-1], fractions, width=bin_size, color='skyblue', edgecolor='black', align='edge')
        plt.xlim(0, 10000)
        plt.title("Binned Scores (Fraction)", fontsize=16)
        plt.xlabel(f"Scores (K) per (bin size = {bin_size})", fontsize=14)
        plt.ylabel("Fraction", fontsize=14)
        plt.xticks(bin_edges, rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.axvline(x=np.nanmean(scores), color="red")
        plt.legend([f"mean = {int(np.nanmean(scores))}"])

        #opslaan als afbeelding (overschrijft wel vorige afbeelding!)
        plt.savefig(output_image)
        print(f"Bargraph opgeslagen als {output_image}")
        plt.show()
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")


if __name__ == "__main__":
    maak_binned_bargraph("resultaten/Combined_Runs/scores.csv", "Visualisation/Graphs/binned_bargraph_fraction.png", 300)
