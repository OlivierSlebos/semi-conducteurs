from stations import Station

from history import History

class Trein():
    def __init__(self):
        self.current_station = Station
        self.time_driven = 0
        self.traject_history = History()

    def change_station(self, station: Station) -> None:
        self.current_station = station