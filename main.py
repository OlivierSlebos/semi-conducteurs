from Classes.Kaart import Kaart

from Algorithms.connection_driven_greedy import connection_driven_greedy_algoritme

from Algorithms.semi_random_algorithm import semi_random_algoritme

from Algorithms.random_algorithm import random_algoritme

if __name__ == "__main__":
    spel = Kaart()

    #  NAAM VAN HET ALGORITME, SPEL, AANTAL TREINEN
    for i in range(1000000):
        random_algoritme(spel)
    