from Classes.Kaart import Kaart

from Algorithms.connection_driven_greedy import connection_driven_greedy_algoritme

from Algorithms.semi_random_algorithm import semi_random_algoritme

from Algorithms.random_algorithm import random_algoritme

from Algorithms.Random_algorithm_2 import roep_functie_aan

from Helpers import bereken_max

from Visualisation.kaart_maken import kaart_maken_csv

from Algorithms.Hill_climber_random import hill_climber

from Algorithms.Hill_climber_heuristiek import hill_climber_2

if __name__ == "__main__":
    spel = Kaart()

    #  NAAM VAN HET ALGORITME, SPEL, AANTAL TREINEN
    # for i in range(1000000):
    #     random_algoritme(spel)
    
    # for i in range(100):
    #     roep_functie_aan(spel)
    #     if i % 100000 == 0:
    #         print(i)

    # hill_climber_2(spel)

    # kaart_maken_csv("run_8797.0_4521439157.csv")

    hill_climber_2(spel)

    # bereken_max("Data/connecties_nederland.csv")

    #9219 is de maximale score