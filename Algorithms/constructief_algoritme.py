from Classes.Kaart import Kaart
from Classes.Trein import Trein 
import random
from score import score_bereken

def constructief_algoritme(spel: Kaart) -> None:
    # maak lege lijsten voor output
    lijst_trajecten = []
    unieke_connecties_gereden = set()
    tijd_gereden = 0

    # max treinen en tijd
    max_tijd_per_traject = 120
    max_aantal_trajecten = 7

    for i in range(max_aantal_trajecten):
        # start nieuw traject en sla op
        traject, traject_connecties, traject_tijd = bouw_traject(spel, max_tijd_per_traject)

        # voeg trajectdata toe aan lijsten
        lijst_trajecten.append(traject)
        for connectie in traject_connecties:
            unieke_connecties_gereden.add(tuple(sorted(connectie)))
        tijd_gereden += traject_tijd

        if len(unieke_connecties_gereden) == sum(station.connection_amount for station in spel.stations.values()) / 2:
            break
    
    aantal_treinen = len(lijst_trajecten)
    aantal_connecties_gereden = len(unieke_connecties_gereden)
    score = score_bereken(aantal_treinen, tijd_gereden, aantal_connecties_gereden)

    # Print resultaten
    print(f"Trajecten: {lijst_trajecten}")
    print(f"Tijd gereden: {tijd_gereden}")
    print(f"Aantal connecties bereden: {len(unieke_connecties_gereden)}")
    print(f"Score: {score}")
    
def bouw_traject(spel: Kaart, max_tijd: int):
    # willekeurig station
    start_station = random.choice(list(spel.stations.items()))

    #Plaats trein op een plek
    trein = Trein(start_station[1])

    # Zet het start station in je geschiedenis
    trein.traject_history.push(start_station[1].name)
    
    # Traject-informatie
    traject = [start_station[1].name]
    traject_connecties = set()
    traject_tijd = 0

    # Zolang de tijd niet voorbij is
    while trein.time_driven < max_tijd:
        # Kies een mogelijke connectie: niet-bereden verbindingen en binnen tijdslimiet
        mogelijke_connecties = [
            (doel_station, reistijd)
            for doel_station, (station, reistijd, bezocht) in trein.current_station.connections.items()
            if not bezocht and trein.time_driven + reistijd <= max_tijd
        ]

        # Stop als er geen verdere connecties mogelijk zijn
        if not mogelijke_connecties:
            break

        # Vind de kortste connectie
        kortste_connectie = mogelijke_connecties[0]
        for connectie in mogelijke_connecties:
            if connectie[1] < kortste_connectie[1]:
                kortste_connectie = connectie

        volgende_station, reistijd = kortste_connectie

        # Update de tijd en voeg verbindingen toe aan de geschiedenis
        trein.time_driven += reistijd
        traject_tijd += reistijd
        traject_connecties.add((trein.current_station.name, volgende_station))
        traject_connecties.add((volgende_station, trein.current_station.name))
        traject.append(volgende_station)

        # Markeer de verbinding als bereden
        trein.current_station.set_connection_visited(spel.stations[volgende_station], reistijd)

        # Verander het huidige station van de trein
        trein.change_station(spel.stations[volgende_station])

    # Retourneer het traject, connecties, en de tijd
    return traject, traject_connecties, traject_tijd