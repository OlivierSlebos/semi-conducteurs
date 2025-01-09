from typing_extensions import Self

class Station:

    def __init__(self, station_id: int, station_name: str, station_coordinate_x: str, station_coordinate_y: str) -> None:
        self.station_id: int = station_id
        self.name: str = station_name
        self.coordinates_x: str = station_coordinate_x
        self.coordinates_y: str = station_coordinate_y
        self.visited = False
        self.connections: dict[str, tuple[Self, int, bool]] = {}
        self.connection_amount = 0

    def add_connection(self, other_station: Self, reisduur: int) -> None:
        # Key = de naam van het doel staion     tuple(Object van het doel station, reisduur)
        self.connections[other_station.name] = (other_station, reisduur, False)

    # hij zet hier de connectie tussen de stations op bereden, dit zie je aan de true statement in de tuple, ook connectie amount met -1
    def set_connection_visited(self, other_station: Self, reisduur) -> None:
        self.connections[other_station.name] = (other_station, reisduur, True)
        self.connection_amount -= 1

    # check of de connectie is bereden, wordt uit de tuple gelezen 
    def is_connection_visited(self, other_station: Self) -> bool:
        return self.connections[other_station.name][2]

    def has_connection(self, direction: str) -> bool:
        if direction in self.connections:
            return True 
        else:
            return False

    def get_connection(self, direction: str) -> Self:
        return self.connections.get(direction)

    def set_visited(self) -> None:
        self.visited = True

    def is_visited(self) -> bool:
        return self.visited
    
    # is nodig om aan het begin 1 keer te bepalen met hoeveel connecties een station begint
    def set_connection_amount(self) -> None:
        self.connection_amount = len(self.connections)
    