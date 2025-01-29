import random

from datetime import datetime

from Classes.Kaart import Kaart

from Classes.Trein import Trein

from Helpers import score_bereken, schrijf_output

def score_greedy_algorithm(spel: Kaart, trein_min, trein_max, minuten_min, minuten_max, kaart) -> None:

    #zorg dat de connecties herladen worden, zodat de connecties niet op bezocht blijven staan
    spel.load_connecties(f"Data/connecties_{kaart}.csv")

    #belangrijke variabelen om bij te houden 
    aantal_gereden_connecties = 0
    totale_reistijd = 0
    schrijf_output_verbindingen = []
    schrijf_output_trajecten = []

    #bepaal een random seed en kies een random aantal treinen 
    r = random.Random(random.seed(datetime.now().timestamp()))
    aantal_treinen = r.randint(trein_min,trein_max)

    #ga de loop door voor het aantal treinen 
    for i in range(aantal_treinen):

        #genereer een traject per trein en update de nodige variabelen 
        traject, verbindingen, reistijd, temp_aantal_gereden_connecties = genereer_traject(spel, aantal_gereden_connecties, totale_reistijd, aantal_treinen, minuten_min, minuten_max, kaart)

        #Sla de verbindingen & trajecten op per trein
        schrijf_output_trajecten.append(traject)
        schrijf_output_verbindingen.append(verbindingen)

        totale_reistijd = reistijd
        aantal_gereden_connecties = temp_aantal_gereden_connecties

    #bereken een score
    score = score_bereken(aantal_treinen, totale_reistijd, aantal_gereden_connecties, kaart)

    #maak een csv van de run 
    schrijf_output(schrijf_output_verbindingen, schrijf_output_trajecten, aantal_treinen, totale_reistijd, aantal_gereden_connecties, score)


def genereer_traject(spel: Kaart, aantal_gereden_connecties, totale_reistijd, aantal_treinen, minuten_min, minuten_max, kaart):
    
    #zet een random seed en kies een random begin station 
    r = random.Random(random.seed(datetime.now().timestamp()))
    begin_station_naam = r.choice(list(spel.stations))
    begin_station_object = spel.stations[begin_station_naam]
    trein1 = Trein(begin_station_object)

    #zet het station in de history en zet hem op bezocht
    trein1.traject_history.push(trein1.current_station.name)
    trein1.current_station.set_visited()

    #bepaal hoe lang de trein mag rijden 
    time_to_drive = r.randint(minuten_min,minuten_max)
    while trein1.time_driven <= time_to_drive and aantal_gereden_connecties < 89:

        te_rijden_connectie = None
        maximale_score = -10000

        #een geshuffelde lijst maken van de opties waar de trein heen kan 
        mogelijke_stations = list(trein1.current_station.connections)
        r.shuffle(mogelijke_stations)

        #kijk welke connectie de hoogste score geeft en niet boven de mogelijke reisduur gaat 
        for connectie in mogelijke_stations:
            station_item, reisduur, connection_visited = trein1.current_station.connections[connectie]
            if not connection_visited:
                tussentijdse_score = score_bereken(aantal_treinen, totale_reistijd + reisduur, aantal_gereden_connecties + 1, kaart)
            else:
                tussentijdse_score = score_bereken(aantal_treinen, totale_reistijd + reisduur, aantal_gereden_connecties, kaart)
            if tussentijdse_score > maximale_score and trein1.time_driven + reisduur < time_to_drive:
                maximale_score = tussentijdse_score
                te_rijden_connectie = connectie

        #als er een goed station is gevonden dan laadt hij de juiste variabelen eruit, anders is het traject klaar 
        if not te_rijden_connectie is None:
            volgend_station, reisduur, connection_visited = trein1.current_station.connections[te_rijden_connectie]
        else:
            break

        #als de connectie nog niet gereden was is er nu 1 extra connectie gereden 
        if not connection_visited:
            aantal_gereden_connecties += 1

        #als de connectie niet over de maximale reistijd heen gaat update hij de variabelen
        if trein1.time_driven + reisduur <= time_to_drive:
                
            #zorg dat de connection op visited gaat, tussen het huidige station en het volgende station, en het omgekeerde
            trein1.current_station.set_connection_visited(volgend_station, reisduur)
            volgend_station.set_connection_visited(trein1.current_station, reisduur)

            #zet de connectie in de history
            huidige_connectie = (trein1.current_station.name, volgend_station.name, reisduur)
            huidige_connectie_2 = (volgend_station.name, trein1.current_station.name, reisduur)

            trein1.traject_history.push_connectie(huidige_connectie)
            trein1.traject_history.push_connectie(huidige_connectie_2)

            #voeg tijd toe en verander het huidige station 
            totale_reistijd += reisduur
            trein1.time_driven += reisduur 
            trein1.current_station = volgend_station

            #zet het station in de history en op bezocht 
            trein1.traject_history.push(trein1.current_station.name)
            trein1.current_station.set_visited()
        else: 
            break

    return(trein1.traject_history._data, trein1.traject_history._data_connectie, totale_reistijd, aantal_gereden_connecties)