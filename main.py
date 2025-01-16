from Classes.Kaart import Kaart

from Algorithms.connection_driven_greedy import connection_driven_greedy_algoritme

from Algorithms.semi_random_algorithm import semi_random_algoritme

from Algorithms.random_algorithm import random_algoritme

from Algorithms.olivier_algorithm import roep_functie_aan

from Helpers import bereken_max

from Visualisation.kaart_maken import kaart_maken_csv

if __name__ == "__main__":
    spel = Kaart()

    #  NAAM VAN HET ALGORITME, SPEL, AANTAL TREINEN
    # for i in range(1000000):
    #     random_algoritme(spel)
    
    for i in range(100):
        roep_functie_aan(spel)

    # kaart_maken_csv("run_7657.571428571429_9761532319.csv")


    #9219 is de maximale score