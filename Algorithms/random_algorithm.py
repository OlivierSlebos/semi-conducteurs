from datetime import datetime

import random

from Classes.Kaart import Kaart

from Classes.Trein import Trein

from Helpers import genereer_output

def random_algoritme(spel: Kaart) -> None:


    lijst_stations_gereden = []
    lijst_connecties_gerenden = []

    r = random.Random(random.seed(datetime.now().timestamp()))
    aantal_treinen = r.randrange(1,8)

    for i in range(aantal_treinen):

        #Voer het algoritme uit
        traject, verbindingen = genereer_lijnvoering(spel)

        #Sla de uitkomsten van de history op
        lijst_stations_gereden.extend(traject)
        lijst_connecties_gerenden.extend(verbindingen)

        #Genereer output in een csv
        genereer_output(traject, verbindingen, i)


def genereer_lijnvoering(spel: Kaart) -> tuple[list, list]:
    # random seed generator 
    r = random.Random(random.seed(datetime.now().timestamp()))

    # pak een random station uit de lijst met stations en maak een trein op die plek, mag niet een plek zijn die nog maar 0 connecties over heeft
    station, station_item = r.choice(list(spel.stations.items()))
    while station_item.connection_amount <= 0:
        station, station_item = r.choice(list(spel.stations.items()))
    trein1 = Trein(spel.stations[station])

    # trein mag 2 uur rijden, dus <= 120
    counter = 0
    while trein1.time_driven <= 120 and counter < 10:
        # voeg het huidige station toe aan het traject dat is gereden en zet hem op visited (outdated, visited wordt nu niet gebruikt)
        trein1.current_station.set_visited()
        trein1.traject_history.push(trein1.current_station.name)
        
        # pak een random volgend station uit de lijst connecties van het huidige station
        volgend_station, value = r.choice(list(trein1.current_station.connections.items()))

        # pak de onderdelen van de tuple van de connectie
        station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]
        
        # als de reisduur boven de 2 uur wordt met het huidige station of het traject is al gereden, pakt hij een andere, dit checkt hij 4 keer
        # probleem: het is nog random, dus werkt niet altijd 
        while trein1.time_driven + reisduur > 120 or trein1.current_station.is_connection_visited(station):

            # counter voor checks 
            if counter > 10:
                break

            # pak ander station en onderdelen 
            volgend_station, val = r.choice(list(trein1.current_station.connections.items()))
            station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]
            counter += 1

        # voeg de tijd toe en verander het huidige station
        if counter < 10 and not trein1.current_station.is_connection_visited(station):
            
            # zorg dat de connection op visited gaat, tussen het huidige station en het volgende station, en het omgekeerde
            trein1.current_station.set_connection_visited(station, reisduur)
            station.set_connection_visited(trein1.current_station, reisduur)

            #Zet de connectie in de history
            huidige_connectie = (trein1.current_station.name, station.name, reisduur)
            huidige_connectie_2 = (station.name, trein1.current_station.name, reisduur)

            trein1.traject_history.push_connectie(huidige_connectie)
            trein1.traject_history.push_connectie(huidige_connectie_2)

            # voeg tijd toe en verander het huidige station 
            trein1.time_driven += reisduur 
            trein1.current_station = station

    #Print het traject
    print(trein1.traject_history._data)

    #Print de connecties
    # print(trein1.traject_history._data_connectie)

    return (trein1.traject_history._data, trein1.traject_history._data_connectie)