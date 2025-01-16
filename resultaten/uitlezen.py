import csv
import os

def scores_csv() -> None:

    bestandsnaam = 'scores.csv'
    
    # Lijst van bestanden in de map ophalen
    bestanden = os.listdir("resultaten")
    
    # Alleen bestanden selecteren, geen mappen
    bestanden = [bestand for bestand in bestanden if os.path.isfile(os.path.join("resultaten", bestand))]
    
    # CSV schrijven
    with open(fr"Docs/{bestandsnaam}", mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Koprij toevoegen (optioneel)
        writer.writerow(['Run', 'Score'])
        
        # Bestandnamen en nummers schrijven
        for i, bestand in enumerate(bestanden):
            if bestand == "uitlezen.py":
                continue
            score = bestand.split('_')
            writer.writerow([i, score[1]])


if __name__ == "__main__":
    scores_csv()