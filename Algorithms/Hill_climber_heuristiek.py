from Algorithms.Random_algorithm_2 import roep_functie_aan, laat_trein_rijden

from Classes.Kaart import Kaart

import random

from score import score_bereken

import copy

from Helpers import schrijf_output

import matplotlib.pyplot as plt

from Algorithms.connection_driven_greedy import genereer_lijnvoering

def maak_grafiek(score: list, runs: list):
    # Maak een getrapte grafiek
    plt.step(runs, score, where='post', label='Score per run', color='blue')

    # Voeg labels en titel toe
    plt.xlabel('Aantal Runs')
    plt.ylabel('Score')
    plt.title('Getrapte Grafiek: Score per Run')

    plt.ylim(7000,9300)

    # Toon de grafiek
    plt.legend()
    plt.grid(True)
    plt.savefig("Hill_Climber_grafiek.png")

def hill_climber_2(spel: Kaart):

    #Neem een random oplossing
    oplossing_1 = roep_functie_aan(spel)
    
    oplossing_tijdelijke = {}
    
    #schrijf de uitkomsten naar een dict
    oplossing_tijdelijke["verbindingen"] = oplossing_1[0]
    oplossing_tijdelijke["trajecten"] = oplossing_1[1]
    oplossing_tijdelijke["aantal_treinen"] = oplossing_1[2]
    oplossing_tijdelijke["tijd_gereden"] = oplossing_1[3]
    oplossing_tijdelijke["aantal_conecties"] = oplossing_1[4]
    oplossing_tijdelijke["score"] = oplossing_1[5]

    oplossing_huidig = {}

    oplossing_huidig["verbindingen"] = oplossing_1[0]
    oplossing_huidig["trajecten"] = oplossing_1[1]
    oplossing_huidig["aantal_treinen"] = oplossing_1[2]
    oplossing_huidig["tijd_gereden"] = oplossing_1[3]
    oplossing_huidig["aantal_conecties"] = oplossing_1[4]
    oplossing_huidig["score"] = oplossing_1[5]

    k = 0
    runs = 0
    graph_score = []
    graph_runs = []

    verbeterd = False

    print(f"Begin Score = {oplossing_huidig['score']}")

    #Run nog een x aantal keer als hij nog geen beter score heeft gevonden
    while k < 100000:

        if verbeterd:
            k = 0
            print("verbeterd")
            verbeterd = False

        #Kies een random aantal oplossingen die je verwijdert
        max_verwijderen = (oplossing_tijdelijke["aantal_treinen"] - 1)
        aantal_verwijderen = random.randint(0, max_verwijderen)

        oplossing_tijdelijke["aantal_treinen"] -= aantal_verwijderen
        
        #Verwijder de trajecten
        for i in range(aantal_verwijderen):
            
            #Bereken een random conectie die je gaat verwijderen
            index = random.randint(0, len(oplossing_tijdelijke["verbindingen"]))
            tijd_gereden = 0

            if index != 0:
                index -= 1

            if len(oplossing_tijdelijke["verbindingen"]) != 0:
                #Bereken de tijd die die verbinding kost
                for g in oplossing_tijdelijke["verbindingen"][index]:
                    tijd_gereden += g[2]
                tijd_gereden_nieuw = int(tijd_gereden / 2)

                #Verwijder de tijd, connecties & traject van deze trein
                oplossing_tijdelijke["tijd_gereden"] -= tijd_gereden_nieuw
                oplossing_tijdelijke["verbindingen"].pop(index)
                oplossing_tijdelijke["trajecten"].pop(index)

        #Voeg een random aantal oplossingen toe (Totaal max 7)
        max_toevoegen = 7 - oplossing_tijdelijke["aantal_treinen"]
        aantal_toevoegen = random.randint(0, max_toevoegen)
        oplossing_tijdelijke["aantal_treinen"] += aantal_toevoegen

        #Voeg de nieuwe verbindingen toe
        for m in range(aantal_toevoegen):
            spel.load_connecties
            spel.load_stations
            nieuwe_oplossing = genereer_lijnvoering(spel)
            oplossing_tijdelijke["tijd_gereden"] += nieuwe_oplossing[2]
            oplossing_tijdelijke["trajecten"].append(nieuwe_oplossing[0])
            oplossing_tijdelijke["verbindingen"].append(nieuwe_oplossing[1])

        #Haal dubbele conecties weg (Eerst lijst met tupples door dan elke tuple door)
        nieuwe_lijst_connecties_gereden = []
        for x in oplossing_tijdelijke["verbindingen"]:
            for connectie in x:
                if connectie not in nieuwe_lijst_connecties_gereden:
                    nieuwe_lijst_connecties_gereden.append(connectie)
        aantal_connecties_gereden: int = len(nieuwe_lijst_connecties_gereden)/2

        oplossing_tijdelijke["aantal_conecties"] = aantal_connecties_gereden

        #Bereken de score
        oplossing_tijdelijke["score"] = score_bereken(oplossing_tijdelijke["aantal_treinen"], oplossing_tijdelijke["tijd_gereden"], oplossing_tijdelijke["aantal_conecties"])

        #Kijk welke hoger is
        if oplossing_huidig["score"] >= oplossing_tijdelijke["score"]:
            oplossing_tijdelijke = copy.deepcopy(oplossing_huidig)

        elif oplossing_tijdelijke["score"] > oplossing_huidig["score"]:
            oplossing_huidig = copy.deepcopy(oplossing_tijdelijke)          
            verbeterd = True
        k += 1
        runs += 1

        graph_score.append(oplossing_tijdelijke["score"])
        graph_runs.append(runs)

        if runs % 1000 == 0:
            print(oplossing_huidig["score"])
        
    print(f"Eind Score = {oplossing_huidig["score"]}")

    schrijf_output(oplossing_huidig["verbindingen"], oplossing_huidig["trajecten"], oplossing_huidig["aantal_treinen"], oplossing_huidig["tijd_gereden"],oplossing_huidig["aantal_conecties"], oplossing_huidig["score"])
    maak_grafiek(graph_score, graph_runs)