import csv

from Visualisation.kaart_maken import kaart_maken

def genereer_output(traject, verbindingen, trein_nummer):
    with open('Output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
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

def run_algoritme(algorimte, spel, aantal_treinen: int):
    
    lijst_stations_gereden = []
    lijst_connecties_gerenden = []

    for i in range(aantal_treinen):
        
        #Voer het algoritme uit
        antwoord = algorimte(spel)

        #Sla de uitkomsten van de 
        lijst_stations_gereden.extend(antwoord[0])
        lijst_connecties_gerenden.extend(antwoord[1])
        genereer_output(antwoord[0], antwoord[1], i)
    
    kaart_maken(lijst_stations_gereden, lijst_connecties_gerenden)