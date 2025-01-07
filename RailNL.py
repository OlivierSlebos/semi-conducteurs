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

    def load_stations(self, filename: str) -> None:

        id = 1
        print("stap_1")
        #open document
        with open(filename) as f:
            line = f.readline()
            line = f.readline()
            
            #Maak stations
            while line != "":
                station_data = line.split(',')
                nieuw_station = Station(id, station_data[0], station_data[1], station_data[2])
                self.stations[station_data[0]] = nieuw_station
                id += 1
                line = f.readline()
    
    def print_stations(self) -> None:
        lijst_stations = []
        
        for x in self.stations:
            lijst_stations.append(self.stations[x].name)
        
        print(lijst_stations)

def genereer_lijnvoering(spel: Kaart) -> History:

    key, val = random.choice(list(spel.stations.items()))
    trein1 = Trein(val)
    print(trein1)


if __name__ == "__main__":
    spel = Kaart()
    print("je bent begonnen")
    spel.print_stations()