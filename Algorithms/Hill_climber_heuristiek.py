from Algorithms.Random_algorithm_2 import roep_functie_aan, laat_trein_rijden

from Classes.Kaart import Kaart

import random

import copy

from Helpers import schrijf_output, maak_grafiek, score_bereken

from Algorithms.connectie_algoritme import genereer_traject

def hill_climber_nederland_heuristiek(spel: Kaart, minimale_treinen: int, maximale_treinen: int, min_minuten: int, max_minuten: int, iterations: int, kaart: str):
    """
    Deze functie past steeds enkele trajecten aan om de hoogst mogelijk score te vinden, de hoogste score wordt bewaard.

    Om een nieuw traject te leggen maakt de functie gebruik van het Heuristiek algoritme (File: connectie_algoritme), 
    dat algoritme maakt een traject dat de voorkeur geeft aan een nog niet bereden connectie. Dat algoritme blijft rijden tot de meegegeven tijd verstreken is. 
    Als het nieuwe traject een betere score oplevert, wordt de dit de nieuwe oplossing waarmee wordt vergeleken, de vorrige wordt verwijderd. 
    """
    #Neem een random eerste oplossing
    oplossing_1 = roep_functie_aan(spel, minimale_treinen, maximale_treinen, min_minuten, max_minuten, kaart)
    
    oplossing_tijdelijke = {}
    
    #schrijf de uitkomsten naar een dict deze ga je steeds veranderen
    oplossing_tijdelijke["verbindingen"] = oplossing_1[0]
    oplossing_tijdelijke["trajecten"] = oplossing_1[1]
    oplossing_tijdelijke["aantal_treinen"] = oplossing_1[2]
    oplossing_tijdelijke["tijd_gereden"] = oplossing_1[3]
    oplossing_tijdelijke["aantal_conecties"] = oplossing_1[4]
    oplossing_tijdelijke["score"] = oplossing_1[5]

    oplossing_huidig = {}

    #Deze dict is steeds de 'beste' oplossing
    oplossing_huidig["verbindingen"] = oplossing_1[0]
    oplossing_huidig["trajecten"] = oplossing_1[1]
    oplossing_huidig["aantal_treinen"] = oplossing_1[2]
    oplossing_huidig["tijd_gereden"] = oplossing_1[3]
    oplossing_huidig["aantal_conecties"] = oplossing_1[4]
    oplossing_huidig["score"] = oplossing_1[5]

    #Zet alle info op start positie + Sla dingen op voor de grafiek
    k = 0
    runs = 0
    graph_score = []
    graph_runs = []
    verbeterd = False

    #Laat zien wat de start score is
    print(f"Begin Score = {oplossing_huidig['score']}")

    #Run nog een k aantal keer als hij nog geen beter score heeft gevonden
    while k < iterations:

        #Als hij is verbeterd wordt K weer nul
        if verbeterd:
            k = 0
            print("verbeterd")
            verbeterd = False

        #Kies een random aantal oplossingen die je verwijdert, altijd 1 minder dan het maximale
        max_verwijderen = (oplossing_tijdelijke["aantal_treinen"] - 1)
        aantal_verwijderen = random.randint(0, max_verwijderen)
        oplossing_tijdelijke["aantal_treinen"] -= aantal_verwijderen

        #Verwijder dat aantal trajecten
        for i in range(aantal_verwijderen):
            
            #Pak een random conectie die je gaat verwijderen
            index = random.randint(0, len(oplossing_tijdelijke["verbindingen"]))
            tijd_gereden = 0

            #Pas op dat index niet onder nul komt.
            if index != 0:
                index -= 1

            #Controleer of de lijsten niet leeg zijn, er zijn dan geen treinen meer
            if len(oplossing_tijdelijke["verbindingen"]) != 0:
                
                #Bereken de tijd die deze trein gereden heeft (BEGIN DATA STRUCTUUR FOUT, KOST TIJD)
                for g in oplossing_tijdelijke["verbindingen"][index]:
                    tijd_gereden += g[2]
                tijd_gereden_nieuw = int(tijd_gereden / 2)

                #Verwijder de tijd, connecties & traject van deze trein uit de tijdelijke dict
                oplossing_tijdelijke["tijd_gereden"] -= tijd_gereden_nieuw
                oplossing_tijdelijke["verbindingen"].pop(index)
                oplossing_tijdelijke["trajecten"].pop(index)

        #Vind een random aantal treinen om toe tevoegen (Totaal mag niet meer dan zeven zijn)
        max_toevoegen = maximale_treinen - oplossing_tijdelijke["aantal_treinen"] #Bepaal hier het maximum van het aantal treinen
        minimaal_toevoegen = minimale_treinen - oplossing_tijdelijke["aantal_treinen"] #Bepaal hier het minimale van het aantal treinen
        if minimaal_toevoegen < 0:
            minimaal_toevoegen = 0
        aantal_toevoegen = random.randint(minimaal_toevoegen, max_toevoegen)
        oplossing_tijdelijke["aantal_treinen"] += aantal_toevoegen

        #Je werkt met een heuristiek, je moet de kaart reseten anders werkt de heuristiek niet
        spel.load_connecties(f"Data/connecties_{kaart}.csv")
                    
        #Zorg er voor dat de verbindingen opnieuw worden aangezet van de treinen die niet zijn verwijdert
        for q in oplossing_tijdelijke["verbindingen"]:
            for l in q:
                huidige_station = spel.stations[l[0]]
                other_station = spel.stations[l[1]]
                huidige_station.set_connection_visited(other_station, int(l[2]))

        #Voeg de nieuwe verbindingen toe
        for m in range(aantal_toevoegen):

            #Vind een nieuwe oplossing voor 1 trein & voeg dit toe
            nieuwe_oplossing = genereer_traject(spel, min_minuten, max_minuten)
            oplossing_tijdelijke["tijd_gereden"] += nieuwe_oplossing[2]
            oplossing_tijdelijke["trajecten"].append(nieuwe_oplossing[0])
            oplossing_tijdelijke["verbindingen"].append(nieuwe_oplossing[1])  

        #Bereken het nieuwe aantal conecties dat totaal wordt gereden, zonder dubbelingen
        nieuwe_lijst_connecties_gereden = []
        for x in oplossing_tijdelijke["verbindingen"]:
            for connectie in x:
                if connectie not in nieuwe_lijst_connecties_gereden:
                    nieuwe_lijst_connecties_gereden.append(connectie)
        aantal_connecties_gereden: int = len(nieuwe_lijst_connecties_gereden)/2

        #Voeg het aantal connectie toe aan de tijdelijke oplossing
        oplossing_tijdelijke["aantal_conecties"] = aantal_connecties_gereden

        #Bereken de nieuwe score
        oplossing_tijdelijke["score"] = score_bereken(oplossing_tijdelijke["aantal_treinen"], oplossing_tijdelijke["tijd_gereden"], oplossing_tijdelijke["aantal_conecties"], kaart)

        #Kijk welke score hoger is, nieuw of oud & behoud de hoogste
        if oplossing_huidig["score"] >= oplossing_tijdelijke["score"]:
            oplossing_tijdelijke = copy.deepcopy(oplossing_huidig)

        elif oplossing_tijdelijke["score"] > oplossing_huidig["score"]:
            oplossing_huidig = copy.deepcopy(oplossing_tijdelijke)          
            verbeterd = True
        
        #Pas k & aantal runs aan
        k += 1
        runs += 1

        #Sla de informatie voor de grafiek op
        graph_score.append(oplossing_tijdelijke["score"])
        graph_runs.append(runs)

        #Print elke x keer zodat je iets van informatie krijgt
        if runs % 1000 == 0:
            print(oplossing_huidig["score"])
            # print(f"Treinen = {oplossing_huidig["aantal_treinen"]}")
    
    #Tot slot, print de eind score
    print(f"Eind Score = {oplossing_huidig['score']}")

    #Maak een csv met de best gevonden oplossing
    schrijf_output(oplossing_huidig["verbindingen"], oplossing_huidig["trajecten"], oplossing_huidig["aantal_treinen"], oplossing_huidig["tijd_gereden"],oplossing_huidig["aantal_conecties"], oplossing_huidig["score"])
    
    #Maak een grafiek
    maak_grafiek(graph_score, graph_runs, kaart)

if __name__ == "__main__":
    spel = Kaart('nederland')
    hill_climber_nederland_heuristiek(spel, 10, 10, 180, 180, 20000, 'nederland')
    