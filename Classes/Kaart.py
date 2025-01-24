from Classes.Station import Station

class Kaart():

    def __init__(self):

        #verbinding station en ID
        self.stations: dict[str, Station] = {}

        #Laad de stations in
        self.load_stations("Data/stations.csv")

        #Laad de conecties in
        self.load_connecties("Data/connecties.csv")

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

    def reset_kaart(self):
        # Reset de staat van stations en connecties
        self.load_stations("Data/stations.csv")
        self.load_connecties("Data/connecties.csv")