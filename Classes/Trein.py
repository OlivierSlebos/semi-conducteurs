from Classes.Station import Station

from Classes.History import History

class Trein():
    def __init__(self, station):
        """
        Initialiseert een trein op een gegeven startstation.

        station (Station): Het station waar de trein begint.
        """
        self.current_station = station
        self.time_driven = 0
        self.traject_history = History()

    def change_station(self, station: Station) -> None:
        """
        Verandert het huidige station van de trein.

        station (Station): Het nieuwe station waar de trein naartoe gaat.
        """
        self.current_station = station