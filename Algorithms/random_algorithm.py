from datetime import datetime

import random

from Classes.Kaart import Kaart

from Classes.Trein import Trein

from Helpers import schrijf_output, score_bereken

def random_algoritme(spel: Kaart, trein_min, trein_max, minuten_min, minuten_max, kaart) -> None:

    #hou belangrijke variabelen bij 
    lijst_stations_gereden = []
    lijst_connecties_gereden = []
    tijd_gereden = 0

    schrijf_output_verbindingen = []
    schrijf_output_trajecten = []

    #bepaal een random seed en bepaal een random aantal treinen 
    r = random.Random(random.seed(datetime.now().timestamp()))
    aantal_treinen = r.randint(trein_min, trein_max)

    #ga per trein de loop door 
    for i in range(aantal_treinen):

        #voer het algoritme uit en update variabelen 
        traject, verbindingen, reistijd = genereer_lijnvoering(spel, minuten_min, minuten_max)

        #sla de uitkomsten van de history op
        lijst_stations_gereden.extend(traject)
        lijst_connecties_gereden.extend(verbindingen)
        tijd_gereden += reistijd

        #sla op zodat schrijf_output werkt
        schrijf_output_trajecten.append(traject)
        schrijf_output_verbindingen.append(verbindingen)
    
    #bepaal hoeveel unieke connecties er gereden zijn 
    nieuwe_lijst_connecties_gereden = []
    for connectie in lijst_connecties_gereden:
        if connectie not in nieuwe_lijst_connecties_gereden:
            nieuwe_lijst_connecties_gereden.append(connectie)
    aantal_connecties_gereden: int = len(nieuwe_lijst_connecties_gereden)/2
    
    #bereken de behaalde score 
    score = score_bereken(aantal_treinen, tijd_gereden, aantal_connecties_gereden, kaart)

    #sla de run op in een csv 
    schrijf_output(schrijf_output_verbindingen, schrijf_output_trajecten, aantal_treinen, tijd_gereden, aantal_connecties_gereden, score)

def genereer_lijnvoering(spel: Kaart, minuten_min, minuten_max) -> tuple[list, list, int]:
    #random seed generator 
    r = random.Random(random.seed(datetime.now().timestamp()))

    #pak een random station uit de lijst met stations en maak een trein op die plek, mag niet een plek zijn die nog maar 0 connecties over heeft
    station, station_item = r.choice(list(spel.stations.items()))
    trein1 = Trein(spel.stations[station])

    trein1.traject_history.push(trein1.current_station.name)

    time_to_drive = r.randint(minuten_min, minuten_max)
    while trein1.time_driven <= time_to_drive:
        
        counter = 0
        #voeg het huidige station toe aan het traject dat is gereden en zet hem op visited (outdated, visited wordt nu niet gebruikt)

        volgende_stations = list(trein1.current_station.connections)
        r.shuffle(volgende_stations)
        max = len(volgende_stations)
        
        #pak een random volgend station uit de lijst connecties van het huidige station
        #pak de onderdelen van de tuple van de connectie
        volgend_station = volgende_stations[counter]
        station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]

        while trein1.time_driven + reisduur > time_to_drive and counter < max:
            #pak ander station en onderdelen 
            volgend_station = volgende_stations[counter]
            station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]
            counter += 1

        #voeg de tijd toe en verander het huidige station
        if counter < max:

            #zet de connectie in de history
            huidige_connectie = (trein1.current_station.name, station.name, reisduur)
            huidige_connectie_2 = (station.name, trein1.current_station.name, reisduur)

            trein1.traject_history.push_connectie(huidige_connectie)
            trein1.traject_history.push_connectie(huidige_connectie_2)

            #voeg tijd toe en verander het huidige station 
            trein1.time_driven += reisduur 
            trein1.current_station = station

            #zet de trein in de history 
            trein1.traject_history.push(trein1.current_station.name)
        else:
            break

    return (trein1.traject_history._data, trein1.traject_history._data_connectie, trein1.time_driven)