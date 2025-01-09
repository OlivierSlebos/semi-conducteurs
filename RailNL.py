from stations import Station

from trein import Trein

import random

from history import History

from kaart_maken import kaart_maken, station_uit_csv, verbinding_uit_csv

class Kaart():

    def __init__(self):

        #verbinding station en ID
        self.stations: dict[str, Station] = {}

        #Laad de stations in
        self.load_stations("stations.csv")

        #Laad de conecties in
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
                
                #Voeg de connectie de ene kant op toe
                #              Naam-huidig station                    doel - object - Station            tijdsduur
                self.stations[connection_data[0]].add_connection(self.stations[connection_data[1]], int(connection_data[2]))
                
                #Voeg de connectie de andere kant op toe
                self.stations[connection_data[1]].add_connection(self.stations[connection_data[0]], int(connection_data[2]))
                
                #Volgende lijn
                line = f.readline()
    
        # bepaal aan het einde van het laden hoeveel connecties elk station heeft
        for station in self.stations:
            self.stations[station].set_connection_amount()

    #Kijk of de stations er goed in staan          
    def print_stations(self) -> None:
        lijst_stations = []
        
        for x in self.stations:
            lijst_stations.append(self.stations[x].name)
        print(lijst_stations)

    #Kijk of de connecties er goed in staan
    def print_conecties(self, station_geven: str) -> None:
        lijst_conections = []

        station = self.stations[station_geven]
        for x in station.connections:
            lijst_conections.append(station.connections[x][0].name)
        print(lijst_conections)

from datetime import datetime

def genereer_lijnvoering(spel: Kaart) -> tuple[list, list]:
    # random seed generator 
    r = random.Random(random.seed(datetime.now().timestamp()))

    # pak een random station uit de lijst met stations en maak een trein op die plek, mag niet een plek zijn die nog maar 0 connecties over heeft
    station, station_item = r.choice(list(spel.stations.items()))
    while station_item.connection_amount <= 0:
        station, station_item = r.choice(list(spel.stations.items()))
    trein1 = Trein(spel.stations[station])

    # trein mag 2 uur rijden, dus <= 120
    counter = 0
    while trein1.time_driven <= 120 and counter < 10:
        # voeg het huidige station toe aan het traject dat is gereden en zet hem op visited (outdated, visited wordt nu niet gebruikt)
        trein1.current_station.set_visited()
        trein1.traject_history.push(trein1.current_station.name)
        
        # pak een random volgend station uit de lijst connecties van het huidige station
        volgend_station, value = r.choice(list(trein1.current_station.connections.items()))

        # pak de onderdelen van de tuple van de connectie
        station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]
        
        # als de reisduur boven de 2 uur wordt met het huidige station of het traject is al gereden, pakt hij een andere, dit checkt hij 4 keer
        # probleem: het is nog random, dus werkt niet altijd 
        while trein1.time_driven + reisduur > 120 or trein1.current_station.is_connection_visited(station):

            # counter voor checks 
            if counter > 10:
                break

            # pak ander station en onderdelen 
            volgend_station, val = r.choice(list(trein1.current_station.connections.items()))
            station, reisduur, connection_visited = trein1.current_station.connections[volgend_station]
            counter += 1

        # voeg de tijd toe en verander het huidige station
        if counter < 10 and not trein1.current_station.is_connection_visited(station):
            
            # zorg dat de connection op visited gaat, tussen het huidige station en het volgende station, en het omgekeerde
            trein1.current_station.set_connection_visited(station, reisduur)
            station.set_connection_visited(trein1.current_station, reisduur)

            #Zet de connectie in de history
            huidige_connectie = (trein1.current_station.name, station.name, reisduur)
            huidige_connectie_2 = (station.name, trein1.current_station.name, reisduur)

            trein1.traject_history.push_connectie(huidige_connectie)
            trein1.traject_history.push_connectie(huidige_connectie_2)

            # voeg tijd toe en verander het huidige station 
            trein1.time_driven += reisduur 
            trein1.current_station = station

    #Print het traject
    print(trein1.traject_history._data)

    #Print de connecties
    # print(trein1.traject_history._data_connectie)

    return (trein1.traject_history._data, trein1.traject_history._data_connectie)

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