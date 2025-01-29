import csv

from Visualisation.kaart_maken import kaart_maken

import random

import matplotlib.pyplot as plt

def schrijf_output(verbindingen: list[list], trajecten: list, treinen: int, minuten: int, verbinding_aantal: int, score: int):
    """
    Zet de resultaten van één lijnvoering in een CSV bestand. 

    Deze functie zet de resultaten van één lijnvoering in een CSV bestand. 
    Per trein is het mogelijk om in te zien welk traject er is afgelegd. 
    Dit CSV bestand is zo gemaakt dat het kan worden uitgelezen door verschillende functies
    """ 
    # if score < 0:
    #     return None

    getal = random.randint(1, 9999)
    bestandsnaam = f'run_{treinen}_{score}_{getal}.csv'
    
    # Open het bestand in schrijfmodus ('w'), waardoor het bestand wordt aangemaakt als het nog niet bestaat
    with open(fr'Resultaten/{bestandsnaam}', mode='w', newline='') as bestand:
        # Maak een CSV writer object aan
        writer = csv.writer(bestand)
        
        trein = 0

        writer.writerow([treinen, minuten, verbinding_aantal])

        for x, y in zip(trajecten, verbindingen):
            trein += 1
            #Voeg het trein nummer toe
            writer.writerow([f'Trein nummer {trein}'])
            #Voeg traject toe
            writer.writerow(y)
            #Voeg de conectie toe in de csv
            writer.writerow(x)
            #Voeg een lege rij toe
            writer.writerow([])
        
        writer.writerow(['EOF'])

def bereken_max(filename):
    """
    Deze ondersteunden functie berekend de theoretisch maximale score die een stations-kaart kan hebben. 
    Met de kwaliteit formule -> K = p * 10.000 - (T * 100 - minuten)
    """

    with open(filename) as f:
        line = f.readline()
        som = 0
        for line in f:
            som += int(float(line.split(',')[-1]))
    
    uitslag = (1 * 10000) - (9 * 100 + som)
    print(uitslag)

def maak_grafiek(score: list, runs: list, kaart):
    """
    Deze functie maakt een grafiek voor de Hill-Climber. 
    Dit gebeurt op basis van de scores (y-as) en het aantal keer dat de functie is gerunt (x-as). 
    """
    
    # Maak een getrapte grafiek
    plt.step(runs, score, where='post', label='Score per run', color='blue')

    # Voeg labels en titel toe
    plt.xlabel('Aantal Runs')
    plt.ylabel('Score')
    plt.title('Getrapte Grafiek: Score per Run')

    if kaart == 'nederland':
        plt.ylim(5000, 7600)
    else:
        plt.ylim(7000, 9300)

    # Toon de grafiek
    plt.legend()
    plt.grid(True)
    plt.savefig("Visualisation/Graphs/Hill_Climber_grafiek.png")

def controleer_reistijd(filename):
    """
    Deze functie controleert een CSV bestand, 
    is de optel som van de conecties van elke trein even hoog als de totale reistijd die de CSV laat zien. 
    Is dit het geval dan print de functie (GELUKT). 
    """
    
    with open (filename) as f:
        # Geef line een waarde
        line = f.readline()
        reistijd = int(line.split(',')[1])
        controle_reistijd = 0
        print(reistijd)
        for i, line in enumerate(f, start=1):
            if i % 2 == 0:
                resultaat = line.split("\",\"")
                # print(resultaat)
                for x in resultaat:
                    cijfer = x.split(",")
                    if len(cijfer) > 1:
                        controle_reistijd += convert_to_int(cijfer[2])
                        print(convert_to_int(cijfer[2]))
                        print(controle_reistijd)
    
    print(reistijd)
    print(controle_reistijd/2)
    if reistijd == (controle_reistijd/2):
        print("GELUKT!")
    else: print("OEI DIT IS GROTE PROBLEMEN")

def convert_to_int(s):
    """
    Deze functie convert de string s naar een int
    """
    # Verwijder alles behalve cijfers uit de string
    clean_string = ''.join(filter(str.isdigit, s))
    return int(clean_string)  # Zet de schone string om naar een integer

def score_bereken(treinen, minuten, verbindingen, kaart) -> float:
    """
    Bereken de score van één lijnvoering.

    Deze functie berekend de score van één lijnvoering. 
    Dit gebeurd op basis van het aantal treinen/trajecten, 
    het totaal aantal minunten van elle trajecten binnen één lijnvoering samen 
    en het aantal unieke verbindingen van één lijnvoering. Welke formule wordt uitgevoerd hangt af van welke kaart er is gebruikt. 
    """

    if kaart == "nederland":
        # fractie gereden verbindingen, 89 verbindingen totaal
        p = verbindingen / 89
        score = p * 10000 - ((treinen * 100) + minuten)
        return score
    elif kaart == "holland":
        # fractie gereden verbindingen, 28 verbindingen totaal
        p = verbindingen / 28
        score = p * 10000 - ((treinen * 100) + minuten)
        return score
    else:
        print("Geen goede kaart meegegeven")
        return None


def score_bereken_csv(filename: str) -> int:
    """
    Bereken een score vanuit een CSV bestand.

    Deze functie berekend de score van één lijnvoering. 
    Dit gebeurd op basis van het aantal treinen/trajecten, 
    het totaal aantal minunten van elle trajecten binnen één lijnvoering samen 
    en het aantal unieke verbindingen van één lijnvoering.
    """
    with open(f"resultaten/{filename}") as f:
        line = f.readline()

        #gevens splitsen
        gegevens = line.strip().split(',')
        
        aantal_treinen = int(gegevens[0])
        aantal_minuten = int(gegevens[1])
        aantal_verbindingen = float(gegevens[2])
        # fractie gereden verbindingen, 28 verbindingen totaal
        p = aantal_verbindingen / 28
        score = p * 10000 - ((aantal_treinen * 100) + aantal_minuten)
            
    return score

def station_uit_csv(filename: str) -> list:
    """
    Laad de stations in vanuit de DATA-csv om er een kaart van te maken
    """
    stations = []
    #open document
    with open(filename) as f:
        #Sla de eerste rij over
        line = f.readline()
        line = f.readline()

        while line != "":
            #Split de data op in een lijst
            connection_data = line.split(',')
            #Zet het in een tuple
            verbinding = (connection_data[0], float(connection_data[1]), float(connection_data[2].strip()))
            #Voeg het toe aan de lijst
            stations.append(verbinding)
            #Volgende line
            line = f.readline()
    return stations

def verbinding_uit_csv(filename: str) -> list:
    """
    Laad de connecties in vanuit de DATA-csv om er een kaart van te maken
    """
    verbindingen = []
    #open document
    with open(filename) as f:
        #Sla de eerste rij over
        line = f.readline()
        line = f.readline()

        while line != "":
            #Split de data op in een lijst
            connection_data = line.split(',')
            #Zet het in een tuple
            verbinding = (connection_data[0], connection_data[1], int(float(connection_data[2])))
            #Voeg het toe aan de lijst
            verbindingen.append(verbinding)
            #Volgende line
            line = f.readline()
    return verbindingen