import csv

from Visualisation.kaart_maken import kaart_maken

import random

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
    
    if score < 4000:
        return None

    getal = random.randint(1000000000, 9999999999)
    bestandsnaam = f'run_{score}_{getal}.csv'
    
    # Open het bestand in schrijfmodus ('w'), waardoor het bestand wordt aangemaakt als het nog niet bestaat
    with open(fr'resultaten/{bestandsnaam}', mode='w', newline='') as bestand:
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
            