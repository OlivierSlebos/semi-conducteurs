from Classes.Kaart import Kaart

from Visualisation.kaart_maken import kaart_maken

from Algorithms.random_algorithm import random_algoritme

from Helpers import genereer_output, run_algoritme, schrijf_output

from score import score_bereken_csv

from Visualisation.kaart_maken import kaart_maken_csv

if __name__ == "__main__":
    spel = Kaart()

    #  NAAM VAN HET ALGORITME, SPEL, AANTAL TREINEN
    for i in range(1000):
        random_algoritme(spel)
    
    kaart_maken_csv('run_4180.571428571429_5314932241.csv')
    