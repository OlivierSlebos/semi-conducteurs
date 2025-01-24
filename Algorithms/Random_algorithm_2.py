from Classes.Kaart import Kaart

from Classes.Trein import Trein

from Helpers import schrijf_output

from score import score_bereken

import random

def roep_functie_aan(spel: Kaart):

    #Maak lege lijsten voor output
    schrijf_output_verbindingen = []
    schrijf_output_trajecten = []

    #Zet tijd_gereden op 0 & aantal treinen op random
    tijd_gereden = 0
    aantal_treinen = random.randint(4, 7)

    #Laat random treinen rijden
    for i in range(aantal_treinen):
        
        #Krijg de resultaten
        traject, verbindingen, reistijd = laat_trein_rijden(spel)

        #Sla de verbindingen & trajecten op per trein
        schrijf_output_trajecten.append(traject)
        schrijf_output_verbindingen.append(verbindingen)  

        #Sla de gereden tijd op
        tijd_gereden += reistijd

    #Haal dubbele conecties weg (Eerst lijst met tupples door dan elke tuple door)
    nieuwe_lijst_connecties_gereden = []
    for x in schrijf_output_verbindingen:
        for connectie in x:
            if connectie not in nieuwe_lijst_connecties_gereden:
                nieuwe_lijst_connecties_gereden.append(connectie)
    aantal_connecties_gereden: int = len(nieuwe_lijst_connecties_gereden)/2

    #Bereken een score
    score = score_bereken(aantal_treinen, tijd_gereden, aantal_connecties_gereden)

    #Maak een csv
    schrijf_output(schrijf_output_verbindingen, schrijf_output_trajecten, aantal_treinen, tijd_gereden, aantal_connecties_gereden, score)

    return (schrijf_output_verbindingen, schrijf_output_trajecten, aantal_treinen, tijd_gereden, aantal_connecties_gereden, score)

def laat_trein_rijden(spel: Kaart):

    #Kies een random station
    start_station = random.choice(list(spel.stations.items()))
    
    #Plaats trein op een plek
    trein = Trein(start_station[1])

    #Zet het start station in je geschiedenis
    trein.traject_history.push(start_station[1].name)
    
    #Maak een random tijd per trein
    tijd = random.randint(50, 120)

    #Zolang de tijd niet voorbij is
    while trein.time_driven <= tijd:

        #Kies een random volgende conectie
        volgende_station = random.choice(list(trein.current_station.connections.items()))

        #Update de tijd
        trein.time_driven += int(volgende_station[1][1])

        #Controleer of hij niet voorbijde 120 minuten gaat door deze conectie
        if trein.time_driven > tijd:
            #Als dat zo is stop en verwijder laatst gereden tijd
            trein.time_driven -= volgende_station[1][1]
            break
        else:
            #Voeg de gereden connectie & nieuwe stationtoe aan de geschiedenis
            gereden_conectie = (trein.current_station.name, volgende_station[0], volgende_station[1][1])
            gereden_conectie_2 = ( volgende_station[0], trein.current_station.name,volgende_station[1][1])
            trein.traject_history.push_connectie(gereden_conectie)
            trein.traject_history.push_connectie(gereden_conectie_2)
            trein.traject_history.push(volgende_station[0])

            #Verander het huidige station
            trein.current_station = volgende_station[1][0]

    return (trein.traject_history._data, trein.traject_history._data_connectie, trein.time_driven)