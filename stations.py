from typing_extensions import Self

class Station:

    def __init__(self, station_id: int, station_name: str, station_coordinate_x: str, station_coordinate_y: str) -> None:
        self.station_id: int = station_id
        self.name: str = station_name
        self.coordinates_x: str = station_coordinate_x
        self.coordinates_y: str = station_coordinate_y
        self.visited = False
        self.connections: dict[str, Station] = {}

    def add_connection(self, other_station: Self, reisduur: int) -> None:
        self.connections[other_station.name] = (other_station, reisduur)

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
