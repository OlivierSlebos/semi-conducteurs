from Classes.Kaart import Kaart

from kaart_maken import kaart_maken, station_uit_csv, verbinding_uit_csv

from Algorithms.random_algorithm import genereer_lijnvoering

if __name__ == "__main__":
    spel = Kaart()
    
    lijst_stations_gereden = []
    lijst_connecties_gerenden = []

    for i in range(7):
        antwoord = genereer_lijnvoering(spel)
        lijst_stations_gereden.extend(antwoord[0])
        lijst_connecties_gerenden.extend(antwoord[1])

    stations = station_uit_csv("stations.csv")
    verbindingen = verbinding_uit_csv("connecties.csv")
    kaart_maken(stations, verbindingen, lijst_stations_gereden, lijst_connecties_gerenden)