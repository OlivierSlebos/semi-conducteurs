from datetime import datetime

import random

from Classes.Kaart import Kaart

from Classes.Trein import Trein

from Helpers import schrijf_output, score_bereken

def connectie_algoritme(spel: Kaart, trein_min, trein_max, minuten_min, minuten_max, kaart) -> None:
    """
    Dit algoritme volgt bovenop het random algoritme 2 heuristieken. Het startstation is altijd een station
    waar nog onbereden connecties zijn, en het algoritme kiest als mogelijk op elk station een connectie die nog niet is gereden. Als er
    meerdere connecties onbereden zijn dan maakt het algoritme een random keuze. Als er geen connecties meer onbereden zijn op een station 
    dan maakt het algoritme ook een random keuze. De trein stopt wanneer alle connecties op een station de maximale reistijd overschreiden.

    Tijdens het runnen van het algoritme wordt de reistijd, de bezochte stations en de gereden connecties bijgehouden. 
    Op basis van deze variabelen wordt een score berekend en wordt een csv met de run aangemaakt. 
    """

    #zorg dat de connecties weer op hun baseline staan 
    spel.load_connecties(f"Data/connecties_{kaart}.csv")

    #hou belangrijke variabelen bij 
    lijst_stations_gereden = []
    lijst_connecties_gereden = []
    tijd_gereden = 0
    schrijf_output_verbindingen = []
    schrijf_output_trajecten = []

    #bepaal een random seed en bepaal een random aantal treinen 
    r = random.Random(random.seed(datetime.now().timestamp()))
    aantal_treinen = r.randint(trein_min, trein_max)

    #loop per trein de loop door 
    for i in range(aantal_treinen):

        #voer het algoritme uit per trein en update variabelen 
        traject, verbindingen, reistijd = genereer_traject(spel, minuten_min, minuten_max)

        #sla de uitkomsten van de history op
        lijst_stations_gereden.extend(traject)
        lijst_connecties_gereden.extend(verbindingen)
        tijd_gereden += reistijd

        #Sla op zodat schrijf_output werkt
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


def genereer_traject(spel: Kaart, minuten_min, minuten_max) -> tuple[list, list]:

    # random seed generator 
    r = random.Random(random.seed(datetime.now().timestamp()))

    # lijst met mogelijke begint stations 
    stations = list(spel.stations)
    r.shuffle(stations)
    max = len(stations)

    # pak een random station uit de lijst met stations en maak een trein op die plek, mag niet een plek zijn die nog maar 0 connecties over heeft
    counter = 0
    volgend_station = stations[counter]
    station_item = spel.stations[volgend_station]
    
    while station_item.connection_amount <= 0 and counter < max:
        volgend_station = stations[counter]
        station_item = spel.stations[volgend_station]
        counter += 1
    trein1 = Trein(station_item)

    trein1.traject_history.push(trein1.current_station.name)
    trein1.current_station.set_visited()

    # trein mag 2 uur rijden, dus <= 120

    time_to_drive = r.randint(minuten_min, minuten_max) #Verhoogd voor holland
    while trein1.time_driven <= time_to_drive:

        #counter om stations uit de lijst te indexeren en bij te houden of er nog stations over zijn 
        counter = 0

        #de lijst van stations random shuffelen, zodat de index random wordt 
        volgende_stations = list(trein1.current_station.connections)
        r.shuffle(volgende_stations)
        max = len(volgende_stations)

        # pak de onderdelen van de connectie 
        volgend_station = volgende_stations[counter]
        station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]
        
        #als de totale reisduur te hoog wordt of de connectie al bereden is dan pakt hij een andere
        while (trein1.time_driven + reisduur > time_to_drive or connection_visited) and counter < max:
            # pak ander station en onderdelen 
            volgend_station = volgende_stations[counter]
            station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]

            #als alle stations al bereden zijn of een te lange reistijd hebben stopt hij de loop 
            counter += 1

        #als alle connecties al bereden waren, maar de de tijd nog niet werd overschreden dan gaat hij nog door, anders is het traject klaar  
        if not trein1.time_driven + reisduur > time_to_drive:
            
            #zorg dat de connection op visited gaat, tussen het huidige station en het volgende station, en het omgekeerde
            trein1.current_station.set_connection_visited(station, reisduur)
            station.set_connection_visited(trein1.current_station, reisduur)

            #Zet de connectie in de history
            huidige_connectie = (trein1.current_station.name, station.name, reisduur)
            huidige_connectie_2 = (station.name, trein1.current_station.name, reisduur)

            trein1.traject_history.push_connectie(huidige_connectie)
            trein1.traject_history.push_connectie(huidige_connectie_2)

            #zorg dat de connection amounts minder worden 
            trein1.current_station.connection_amount -= 1
            station.connection_amount -= 1

            #voeg tijd toe en verander het huidige station 
            trein1.time_driven += reisduur 
            trein1.current_station = station

            #zet het station in de history en zet hem op bezocht 
            trein1.traject_history.push(trein1.current_station.name)
            trein1.current_station.set_visited()
        else:
            break

    return (trein1.traject_history._data, trein1.traject_history._data_connectie, trein1.time_driven)