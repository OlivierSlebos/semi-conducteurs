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
    
    spel = Kaart(sys.argv[5])

    for i in range(int(sys.argv[6])):
        random_algoritme(spel, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])