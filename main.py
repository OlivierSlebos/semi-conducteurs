from Classes.Kaart import Kaart

from Algorithms.connection_driven_greedy import connection_driven_greedy_algoritme

from Algorithms.semi_random_algorithm import semi_random_algoritme

from Algorithms.random_algorithm import random_algoritme

from Algorithms.Random_algorithm_2 import roep_functie_aan

from Helpers import bereken_max

from Visualisation.kaart_maken import kaart_maken_csv

from Algorithms.score_greedy import score_greedy_algorithm

from Algorithms.Hill_climber_heuristiek import hill_climber_nederland_heuristiek

from Algorithms.Hill_climber_random import hill_climber_random

import sys

if __name__ == "__main__":
    #als je het wil kunnen invullen kan je dit gebruiken, anders eruit commenten
    trein_min = input("Hoeveel treinen wil je dat er minimaal per iteration rijden: ")
    while not trein_min.isdigit() or int(trein_min) < 1 or int(trein_min) > 20:
        trein_min = input("Hoeveel treinen wil je dat er minimaal per iteration rijden: ")

    trein_max = input("Hoeveel treinen wil je dat er maximaal per iteration rijden: ")
    while not trein_max.isdigit() or int(trein_max) < int(trein_min) or int(trein_max) < 1 or int(trein_max) > 20:
        trein_max = input("Hoeveel treinen wil je dat er maximaal per iteration rijden: ")
    
    #Aanpassen als Holland max is 180 als Nederland max is 120
    minuten_min = input("Hoeveel minuten wil je dat een trein minimaal rijdt: ")
    while not minuten_min.isdigit() or int(minuten_min) < 1 or int(minuten_min) > 180:
        minuten_min = input("Hoeveel minuten wil je dat een trein minimaal rijdt: ")

    minuten_max = input("Hoeveel minuten wil je dat een trein maximaal rijdt: ")
    while not minuten_max.isdigit() or int(minuten_max) < int(minuten_min) or int(minuten_max) < 1 or int(minuten_max) > 180:
        minuten_max = input("Hoeveel minuten wil je dat een trein maximaal rijdt: ")

    kaart = input("Met welke kaart wil je werken (holland/nederland): ")
    while not kaart in ["holland", "nederland"]:
        kaart = input("Met welke kaart wil je werken (holland/nederland): ")

    iterations = input("Hoeveel iterations wil je doen: ")
    while not iterations.isdigit() or int(iterations) < 1:
        iterations = input("Hoeveel iterations wil je doen: ")

    ALGORITMES = ["random_algoritme", "score_greedy_algorithm","connection_driven_greedy_algoritme","hill_climber_heuristiek", "hill_climber_random"]
    algoritme = input("Welk algortme wil je gebruiken (random_algoritme/score_greedy_algoritme/connection_driven_greedy_algoritme/hill_climber_heuristiek/hill_climber_random): ")
    while algoritme not in ALGORITMES:
        algoritme = input("Welk algortme wil je gebruiken (random_algoritme/score_greedy_algoritme/connection_driven_greedy_algoritme): ")

    #Zet de kaart aan
    spel = Kaart(kaart)

    #Als het Hill climber is, werkt het anders dus pak dan een ander algoritme systeem
    if algoritme == "hill_climber_heuristiek" or algoritme == " hill_climber_heuristiek":
        algoritme = globals()['hill_climber_nederland_heuristiek']
        algoritme(spel, int(trein_min), int(trein_max), int(minuten_min), int(minuten_max), int(iterations), kaart)    
    elif algoritme == "hill_climber_random" or algoritme == " hill_climber_random":
        algoritme = globals()['hill_climber_random']
        algoritme(spel, int(trein_min), int(trein_max), int(minuten_min), int(minuten_max), int(iterations), kaart)
    #Anders gebruik het normale systeem
    else:
        algoritme = globals()[algoritme]
        for i in range(int(iterations)):
            algoritme(spel, int(trein_min), int(trein_max), int(minuten_min), int(minuten_max), kaart)