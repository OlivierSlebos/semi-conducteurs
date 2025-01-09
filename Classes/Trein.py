from Station import Station

from History import History

class Trein():
    def __init__(self, station):
        self.current_station = station
        self.time_driven = 0
        self.traject_history = History()

    def change_station(self, station: Station) -> None:
        self.current_station = station