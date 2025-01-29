from typing_extensions import Self

class Station:

    def __init__(self, station_id: int, station_name: str, station_coordinate_x: str, station_coordinate_y: str) -> None:
        """
        Initialiseert een station met een uniek ID, naam en coördinaten.

        station_id: ID van station.
        station_name: Naam van station.
        station_coordinate_x: X-coördinaat van het station.
        station_coordinate_y: Y-coördinaat van het station.
        """
        self.station_id: int = station_id
        self.name: str = station_name
        self.coordinates_x: str = station_coordinate_x
        self.coordinates_y: str = station_coordinate_y
        self.visited = False
        self.connections: dict[str, tuple[Self, int, bool]] = {}
        self.connection_amount = 0

    def add_connection(self, other_station: Self, reisduur: int) -> None:
        """
        Voegt een verbinding toe tussen dit station en een ander station.

        other_station: Het station waarmee een verbinding wordt gelegd.
        reisduur: De reistijd in minuten tussen de stations.
        """
        # Key = de naam van het doel staion     tuple(Object van het doel station, reisduur)
        self.connections[other_station.name] = (other_station, reisduur, False)

    def set_connection_visited(self, other_station: Self, reisduur) -> None:
        """
        Markeert een verbinding als bereden en verlaag het aantal niet-bereden verbindingen.
        """
        self.connections[other_station.name] = (other_station, reisduur, True)
        self.connection_amount -= 1

    def verwijder_connection_visited(self, other_station: Self, reisduur) -> None:
        """
        Zet een eerder bereden verbinding naar de oorspronkelijke status.
        """
        if other_station.name in self.connections:
            self.connections[other_station.name] = (other_station, reisduur, False)
            self.connection_amount += 1
 
    def is_connection_visited(self, other_station: Self) -> bool:
        """
        checkt of de connectie is bereden, wordt uit de tuple gelezen

        Returt True als de verbinding is bereden, anders False.
        """
        return self.connections[other_station.name][2]

    def has_connection(self, direction: str) -> bool:
        """
        Controleert of er een verbinding is met een ander station.

        direction: De naam van het andere station.

        Returnt True als de verbinding bestaat, anders False.
        """
        if direction in self.connections:
            return True 
        else:
            return False

    def get_connection(self, direction: str) -> Self:
        """
        Haalt de verbinding met een ander station op.

        Returnt een tuple met het andere station, reistijd en status van de verbinding, of None als de verbinding niet bestaat.
        """
        return self.connections.get(direction)

    def set_visited(self) -> None:
        """
        Markeert het station als bezocht.
        """
        self.visited = True

    def is_visited(self) -> bool:
        """
        Controleert of het station bezocht is.

        Returnt True als het station bezocht is, anders False.
        """
        return self.visited
    
    def set_connection_amount(self) -> None:
        """
        Bepaalt en stelt het aantal verbindingen in die dit station heeft.
        Dit wordt één keer uitgevoerd nadat alle verbindingen geladen zijn.
        """
        self.connection_amount = len(self.connections)
    