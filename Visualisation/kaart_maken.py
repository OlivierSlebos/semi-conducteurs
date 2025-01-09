import folium

def station_uit_csv(filename: str) -> list:
    stations = []
    #open document
    with open(filename) as f:
        #Sla de eerste rij over
        line = f.readline()
        line = f.readline()

        while line != "":
            #Split de data op in een lijst
            connection_data = line.split(',')
            #Zet het in een tuple
            verbinding = (connection_data[0], float(connection_data[1]), float(connection_data[2].strip()))
            #Voeg het toe aan de lijst
            stations.append(verbinding)
            #Volgende line
            line = f.readline()
    return stations

def verbinding_uit_csv(filename: str) -> list:
    verbindingen = []
    #open document
    with open(filename) as f:
        #Sla de eerste rij over
        line = f.readline()
        line = f.readline()

        while line != "":
            #Split de data op in een lijst
            connection_data = line.split(',')
            #Zet het in een tuple
            verbinding = (connection_data[0], connection_data[1], int(connection_data[2]))
            #Voeg het toe aan de lijst
            verbindingen.append(verbinding)
            #Volgende line
            line = f.readline()
    return verbindingen


def kaart_maken(is_visited, verbindingen_geweest):
    
    stations = station_uit_csv("Data/stations.csv")
    verbindingen = verbinding_uit_csv("Data/connecties.csv")
    
    # Maak een basismap van Nederland (centraal punt)
    m = folium.Map(location=[52.3794, 4.9009], zoom_start=8)

    # Voeg stations toe als markers
    station_dict = {name: (lat, lon) for name, lat, lon in stations}
    
    for naam, (lat, lon) in station_dict.items():
        if naam in is_visited: color = 'green'
        else: color = 'red'
        folium.Marker([lat, lon], popup=naam, icon=folium.Icon(color=color)).add_to(m)

    # Voeg verbindingen toe als lijnen tussen stations
    for start, eind, reistijd in verbindingen:
        start_lat, start_lon = station_dict[start]
        eind_lat, eind_lon = station_dict[eind]
        if (start, eind, reistijd) in verbindingen_geweest:
            color = 'green'
        else: color = 'red'
        folium.PolyLine([(start_lat, start_lon), (eind_lat, eind_lon)], color=color, weight=2.5, opacity=0.8).add_to(m)

    # Bewaar de kaart in een HTML bestand
    m.save("Visualisation/resultaten_kaart.html")

if __name__ == "__main__":
    stations = station_uit_csv("stations.csv")
    verbindingen = verbinding_uit_csv("connecties.csv")
    stations_geweest = ['Alkmaar', 'Den Helder', 'Rotterdam Centraal', 'Hoorn']
    verbindingen_geweest = [('Amsterdam Amstel' , 'Amsterdam Zuid' , int(10)),('Amsterdam Amstel' , 'Amsterdam Centraal' , int(8)),('Amsterdam Centraal' , 'Amsterdam Sloterdijk' , int(6)) ,('Amsterdam Sloterdijk' , 'Haarlem' , int(11)), ('Alkmaar','Den Helder',int(36))]
    kaart_maken(stations, verbindingen, stations_geweest, verbindingen_geweest)