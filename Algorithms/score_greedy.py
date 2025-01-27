import random

from datetime import datetime

from Classes.Kaart import Kaart

from Classes.Trein import Trein

from score import score_bereken

from Helpers import schrijf_output

def score_greedy_algorithm(spel: Kaart) -> None:
    spel.load_connecties("Data/connecties_nederland.csv")

    aantal_gereden_connecties = 0
    totale_reistijd = 0
    schrijf_output_verbindingen = []
    schrijf_output_trajecten = []

    r = random.Random(random.seed(datetime.now().timestamp()))
    aantal_treinen = r.randint(9,12)

    for i in range(aantal_treinen):

        traject, verbindingen, reistijd, temp_aantal_gereden_connecties = genereer_lijnvoering(spel, aantal_gereden_connecties, totale_reistijd, aantal_treinen)

        #Sla de verbindingen & trajecten op per trein
        schrijf_output_trajecten.append(traject)
        schrijf_output_verbindingen.append(verbindingen)

        totale_reistijd = reistijd
        aantal_gereden_connecties = temp_aantal_gereden_connecties

    #Bereken een score
    score = score_bereken(aantal_treinen, totale_reistijd, aantal_gereden_connecties)

    #Maak een csv
    schrijf_output(schrijf_output_verbindingen, schrijf_output_trajecten, aantal_treinen, totale_reistijd, aantal_gereden_connecties, score)


def genereer_lijnvoering(spel: Kaart, aantal_gereden_connecties, totale_reistijd, aantal_treinen):
    
    r = random.Random(random.seed(datetime.now().timestamp()))
    begin_station_naam = r.choice(list(spel.stations))
    begin_station_object = spel.stations[begin_station_naam]
    
    trein1 = Trein(begin_station_object)

    trein1.traject_history.push(trein1.current_station.name)
    trein1.current_station.set_visited()

    time_to_drive = r.randint(60,180)
    while trein1.time_driven <= time_to_drive and aantal_gereden_connecties < 89:

        te_rijden_connectie = None
        maximale_score = -1000000

        mogelijke_stations = list(trein1.current_station.connections)
        r.shuffle(mogelijke_stations)

        for connectie in mogelijke_stations:
            station_item, reisduur, connection_visited = trein1.current_station.connections[connectie]
            if not connection_visited:
                tussentijdse_score = score_bereken(aantal_treinen, totale_reistijd + reisduur, aantal_gereden_connecties + 1)
            else:
                tussentijdse_score = score_bereken(aantal_treinen, totale_reistijd + reisduur, aantal_gereden_connecties)
            if tussentijdse_score > maximale_score and trein1.time_driven + reisduur < time_to_drive:
                maximale_score = tussentijdse_score
                te_rijden_connectie = connectie

        if not te_rijden_connectie is None:
            volgend_station, reisduur, connection_visited = trein1.current_station.connections[te_rijden_connectie]
        else:
            break

        if not connection_visited:
            aantal_gereden_connecties += 1

        if trein1.time_driven + reisduur <= time_to_drive:
                
            # zorg dat de connection op visited gaat, tussen het huidige station en het volgende station, en het omgekeerde
            trein1.current_station.set_connection_visited(volgend_station, reisduur)
            volgend_station.set_connection_visited(trein1.current_station, reisduur)

            #Zet de connectie in de history
            huidige_connectie = (trein1.current_station.name, volgend_station.name, reisduur)
            huidige_connectie_2 = (volgend_station.name, trein1.current_station.name, reisduur)

            trein1.traject_history.push_connectie(huidige_connectie)
            trein1.traject_history.push_connectie(huidige_connectie_2)

            # voeg tijd toe en verander het huidige station 
            totale_reistijd += reisduur
            trein1.time_driven += reisduur 
            trein1.current_station = volgend_station

            trein1.traject_history.push(trein1.current_station.name)
            trein1.current_station.set_visited()
        else: 
            break

    return(trein1.traject_history._data, trein1.traject_history._data_connectie, totale_reistijd, aantal_gereden_connecties)