from datetime import datetime

import random

from Classes.Kaart import Kaart

from Classes.Trein import Trein

from Visualisation.kaart_maken import kaart_maken

from Helpers import schrijf_output

from score import score_bereken

def semi_random_algoritme(spel: Kaart) -> None:

    lijst_stations_gereden = []
    lijst_connecties_gereden = []
    tijd_gereden = 0

    schrijf_output_verbindingen = []
    schrijf_output_trajecten = []

    r = random.Random(random.seed(datetime.now().timestamp()))
    aantal_treinen = 7

    for i in range(aantal_treinen):

        #Voer het algoritme uit
        traject, verbindingen, reistijd = genereer_lijnvoering(spel)

        #Sla de uitkomsten van de history op
        lijst_stations_gereden.extend(traject)
        lijst_connecties_gereden.extend(verbindingen)
        tijd_gereden += reistijd

        #Sla op zodat schrijf_output werkt
        schrijf_output_trajecten.append(traject)
        schrijf_output_verbindingen.append(verbindingen)

        #Genereer output in een csv
        # genereer_output(traject, verbindingen, i)
    
    nieuwe_lijst_connecties_gereden = []
    for connectie in lijst_connecties_gereden:
        if connectie not in nieuwe_lijst_connecties_gereden:
            nieuwe_lijst_connecties_gereden.append(connectie)

    aantal_connecties_gereden: int = len(nieuwe_lijst_connecties_gereden)/2
    

    # kaart_maken(lijst_stations_gereden, lijst_connecties_gereden)

    score = score_bereken(aantal_connecties_gereden, tijd_gereden, aantal_connecties_gereden)

    schrijf_output(schrijf_output_verbindingen, schrijf_output_trajecten, aantal_treinen, tijd_gereden, aantal_connecties_gereden, score)

def genereer_lijnvoering(spel: Kaart) -> tuple[list, list, int]:
    # random seed generator 
    r = random.Random(random.seed(datetime.now().timestamp()))

    # pak een random station uit de lijst met stations en maak een trein op die plek, mag niet een plek zijn die nog maar 0 connecties over heeft
    station, station_item = r.choice(list(spel.stations.items()))
    trein1 = Trein(spel.stations[station])

    trein1.traject_history.push(trein1.current_station.name)

    time_to_drive = 120
    while trein1.time_driven <= time_to_drive:
        
        counter = 0
        # voeg het huidige station toe aan het traject dat is gereden en zet hem op visited (outdated, visited wordt nu niet gebruikt)

        volgende_stations = list(trein1.current_station.connections)
        r.shuffle(list(volgende_stations))
        max = len(volgende_stations)
        
        # pak een random volgend station uit de lijst connecties van het huidige station
        # pak de onderdelen van de tuple van de connectie
        volgend_station = volgende_stations[counter]
        station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]

        while trein1.time_driven + reisduur > time_to_drive and counter < max:
            # pak ander station en onderdelen 
            volgend_station = volgende_stations[counter]
            station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]
            counter += 1

        # voeg de tijd toe en verander het huidige station
        if counter < max:
            #Zet de connectie in de history
            huidige_connectie = (trein1.current_station.name, station.name, reisduur)
            huidige_connectie_2 = (station.name, trein1.current_station.name, reisduur)

            trein1.traject_history.push_connectie(huidige_connectie)
            trein1.traject_history.push_connectie(huidige_connectie_2)

            # voeg tijd toe en verander het huidige station 
            trein1.time_driven += reisduur 
            trein1.current_station = station

            trein1.traject_history.push(trein1.current_station.name)
        else:
            break

    #Print het traject
    # print(trein1.traject_history._data)

    #Print de connecties
    # print(trein1.traject_history._data_connectie)

    return (trein1.traject_history._data, trein1.traject_history._data_connectie, trein1.time_driven)