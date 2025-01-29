import csv

from Visualisation.kaart_maken import kaart_maken

import random

import matplotlib.pyplot as plt

def genereer_output(traject, verbindingen, trein_nummer):
    with open('Output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if trein_nummer == 0:
            writer.writerow(['NIEUWE DIENSTREGELING'])
            writer.writerow([])

        #Voeg trein nummer toe
        writer.writerow([f'Trein nummer {trein_nummer}'])

        #Voeg de conectie toe aan de csv
        writer.writerow(traject)

        #Voeg een lege rij toe
        writer.writerow([])

        #Voeg de verbindingen toe
        writer.writerow(verbindingen)

        #Voeg een lege rij toe
        writer.writerow([])

def run_algoritme(algoritme, spel, aantal_treinen: int):

    lijst_stations_gereden = []
    lijst_connecties_gerenden = []

    for i in range(aantal_treinen):

        #Voer het algoritme uit
        antwoord = algoritme(spel)

        #Sla de uitkomsten van de history op
        lijst_stations_gereden.extend(antwoord[0])
        lijst_connecties_gerenden.extend(antwoord[1])

        #Genereer output in een csv
        genereer_output(antwoord[0], antwoord[1], i)

    #Maak een kaart
    kaart_maken(lijst_stations_gereden, lijst_connecties_gerenden)

# def score_bereken(lijst_connecties, )

def schrijf_output(verbindingen: list[list], trajecten: list, treinen: int, minuten: int, verbinding_aantal: int, score: int):
    
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
    
    with open(filename) as f:
        line = f.readline()
        som = 0
        for line in f:
            som += int(float(line.split(',')[-1]))
    
    uitslag = (1 * 10000) - (9 * 100 + som)
    print(uitslag)

def maak_grafiek(score: list, runs: list):
    # Maak een getrapte grafiek
    plt.step(runs, score, where='post', label='Score per run', color='blue')

    # Voeg labels en titel toe
    plt.xlabel('Aantal Runs')
    plt.ylabel('Score')
    plt.title('Getrapte Grafiek: Score per Run')

    plt.ylim(5000, 7600)

    # Toon de grafiek
    plt.legend()
    plt.grid(True)
    plt.savefig("Hill_Climber_grafiek.png")

def controleer_reistijd(filename):
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
    # Verwijder alles behalve cijfers uit de string
    clean_string = ''.join(filter(str.isdigit, s))
    return int(clean_string)  # Zet de schone string om naar een integer


if __name__ == "__main__":
    controleer_reistijd("resultaten/run_11_7202.0_2217.csv")
