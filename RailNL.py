from stations import Station

class Kaart():

    def __init__(self):

        #verbinding station en ID
        self.stations: dict[str, Station] = {}

        #Laad de stations in
        self.load_stations("station.csv")

    def load_stations(self, filename: str) -> None:

        id = 1

        #open document
        with open(filename) as f:
            line = f.readline()
            
            #Maak stations
            while line != "":
                station_data = line.split(',')
                nieuw_station = Station(id, station_data[0], station_data[1], station_data[2])
                self.stations[station_data[0]] = nieuw_station
                id += 1
                line = f.readline()