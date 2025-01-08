from stations import Station

from trein import Trein

import random

from history import History

class Kaart():

    def __init__(self):

        #verbinding station en ID
        self.stations: dict[str, Station] = {}

        #Laad de stations in
        self.load_stations("stations.csv")

        self.load_connecties("connecties.csv")

    def load_stations(self, filename: str) -> None:

        id = 1

        #open document
        with open(filename) as f:
            #Sla de eerste rij over
            line = f.readline()
            line = f.readline()
            
            #Maak stations
            while line != "":
                #Split de data op in een lijst
                station_data = line.split(',')
                nieuw_station = Station(id, station_data[0], station_data[1], station_data[2])
                self.stations[station_data[0]] = nieuw_station
                id += 1
                line = f.readline()
    
    def load_connecties(self, filename: str) -> None:
        #open document
        with open(filename) as f:
            #Sla de eerste rij over
            line = f.readline()
            line = f.readline()
        
            while line != "":
                #Split de data op in een lijst
                connection_data = line.split(',')
                #              Naam                             Naam                 object - Station                       tijdsduur
                self.stations[connection_data[0]].add_connection(connection_data[0], self.stations[connection_data[1]], int(connection_data[2]))
                #Volgende lijn
                line = f.readline()

    #Kijk of de station er goed in staat           
    def print_stations(self) -> None:
        lijst_stations = []
        
        for x in self.stations:
            lijst_stations.append(self.stations[x].name)
        
        print(lijst_stations)

    def print_conecties(self, station_geven: str) -> None:
        lijst_conections = []

        station = self.stations[station_geven]
        for x in station.connections:
            lijst_conections.append(station.connections[x].name)
        
        print(lijst_conections)

from datetime import datetime


def genereer_lijnvoering(spel: Kaart) -> History:

    # random seed generator 
    random.seed(datetime.now().timestamp())

    # pak een random station uit de lijst met stations en maak een trein op die plek 
    key, val = random.choice(list(spel.stations.items()))
    trein1 = Trein(spel.stations[key])

    # check
    print(trein1.current_station.name)

    # trein mag 2 uur rijden, dus =< 120
    while trein1.time_driven =< 120:
        trein1.traject_history.push(trein1.current_station)
        volgend_station = random.choice(list(trein1.current_station.connections.items()))


        trein1.current_station.connections[volgend_station]
        while trein1.time_driven + random.choice(list(trein1.current_station.connections.items()))
        volgend_station = random.choice(list(trein1.current_station.connections.items()))


if __name__ == "__main__":
    spel = Kaart()
    print("je bent begonnen")
    # spel.print_stations()
    spel.print_conecties("Alkmaar")
    genereer_lijnvoering(spel)
