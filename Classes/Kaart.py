from Classes.Station import Station

class Kaart():
    """
    De Kaart class is de overkoepelende class. Deze zorgt ervoor dat er een speelveld of kaart ontstaat
    waarbinnen (of waaronder) de trein- en station-objecten bestaan.
    """

    def __init__(self, kaart: str):
        """
        Initialiseert een kaart met de naam van de data-kaart die je wil gebruiken

        kaart: String, in dit geval 'holland' of 'nederland'
        """
        #verbinding station en ID
        self.stations: dict[str, Station] = {}
        
        
        #Laad de stations in
        self.load_stations(f"Data/stations_{kaart}.csv") #AANGEPAST NAAR HEEL NEDERLAND

        #Laad de conecties in
        self.load_connecties(f"Data/connecties_{kaart}.csv") #AANGEPAST NAAR HEEL NEDERLAND

    def load_stations(self, filename: str) -> None:
        """
        Laad de stations in de dict self.stations, deze is gekoppeld aan de kaart.

        Wordt geladen vanuit Data/
        filename: str met de naam van de data-file (holland/ nederland)
        """
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
        """
        Laad de connecties in de dict van de twee object-station's waar de connectie tussen zit.

        Door middel van object-station functie add_connection aan. 
        Wordt geladen vanuit Data/
        filename: str met de naam van de data-file (holland/ nederland)
        """
        
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
                self.stations[connection_data[0]].add_connection(self.stations[connection_data[1]], int(float(connection_data[2].strip())))
                
                #Voeg de connectie de andere kant op toe
                self.stations[connection_data[1]].add_connection(self.stations[connection_data[0]], int(float(connection_data[2])))
                
                #Volgende lijn
                line = f.readline()
    
        # bepaal aan het einde van het laden hoeveel connecties elk station heeft
        for station in self.stations:
            self.stations[station].set_connection_amount()

    #Kijk of de stations er goed in staan          
    def print_stations(self) -> None:
        """
        Controle functie: print een lijst van alles stations in de dict self.stations
        """
        lijst_stations = []
        
        for x in self.stations:
            lijst_stations.append(self.stations[x].name)
        print(lijst_stations)

    #Kijk of de connecties er goed in staan
    def print_conecties(self, station_geven: str) -> None:
        """
        Controle functie: print een lijst van alles connecties in de dict's van de station-objecten
        """
        lijst_conections = []

        station = self.stations[station_geven]
        for x in station.connections:
            lijst_conections.append(station.connections[x][0].name)
        print(lijst_conections)

    def reset_kaart(self):
        """
        Herlaad de stations en connecties, zodat alles weer op "niet-bezocht" staat.
        """
        # Reset de staat van stations en connecties
        self.load_stations("Data/stations_nederland.csv")
        self.load_connecties("Data/connecties_nederland.csv")