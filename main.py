from Classes.Kaart import Kaart

from Algorithms.connection_driven_greedy import connection_driven_greedy_algoritme

from Algorithms.semi_random_algorithm import semi_random_algoritme

from Algorithms.random_algorithm import random_algoritme

from Algorithms.Random_algorithm_2 import roep_functie_aan

from Helpers import bereken_max

from Visualisation.kaart_maken import kaart_maken_csv

from Algorithms.score_greedy import score_greedy_algorithm

import sys

if __name__ == "__main__":


    #als je command lines wil gebruiken kan je dit gebruiken, anders eruit commenten

    # spel = Kaart(sys.argv[5])
    # algoritme = globals()[sys.argv[6]]

    # for i in range(int(sys.argv[6])):
    #     random_algoritme(spel, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])


    #als je het wil kunnen invullen kan je dit gebruiken, anders eruit commenten
    trein_min = input("Hoeveel treinen wil je dat er minimaal per iteration rijden: ")
    while not trein_min.isdigit() or int(trein_min) < 1 or int(trein_min) > 20:
        trein_min = input("Hoeveel treinen wil je dat er minimaal per iteration rijden: ")

    trein_max = input("Hoeveel treinen wil je dat er maximaal per iteration rijden: ")
    while not trein_max.isdigit() or int(trein_max) < int(trein_min) or int(trein_max) < 1 or int(trein_max) > 20:
        trein_max = input("Hoeveel treinen wil je dat er maximaal per iteration rijden: ")
    
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

    ALGORITMES = ["random_algoritme", "score_greedy_algorithm","connection_driven_greedy_algoritme"]
    algoritme = input("Welk algortme wil je gebruiken (random_algoritme/score_greedy_algoritme/connection_driven_greedy_algoritme): ")
    while algoritme not in ALGORITMES:
        algoritme = input("Welk algortme wil je gebruiken (random_algoritme/score_greedy_algoritme/connection_driven_greedy_algoritme): ")

    algoritme = globals()[algoritme]

    spel = Kaart(kaart)

    for i in range(int(iterations)):
        algoritme(spel, int(trein_min), int(trein_max), int(minuten_min), int(minuten_max), kaart)