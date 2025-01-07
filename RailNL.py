from stations import Station

class Kaart():

    def __init__(self):

        #verbinding station en ID
        self.stations: dict[int, Station]

        #Laad de stations in
        self.load_stations("station.csv")

    def load_rooms(self, filename: str) -> None:

        #open document
        with open(filename) as f:
            line = f.readline()
            
            #Maak stations
            while line != '\n':
                room_data = line.strip().split("\t")
                new_room = Room(int(room_data[0]), room_data[1], room_data[2])
                self.rooms[int(room_data[0])] = new_room
                line = f.readline()