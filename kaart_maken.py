import folium

# Stations en hun coördinaten (naam, latitude, longitude)
stations = [
    ("Alkmaar", 52.63777924, 4.739722252),
    ("Alphen a/d Rijn", 52.12444305, 4.657777786),
    ("Amsterdam Amstel", 52.34666824, 4.917778015),
    ("Amsterdam Centraal", 52.37888718, 4.900277615),
    ("Amsterdam Sloterdijk", 52.38888931, 4.837777615),
    ("Amsterdam Zuid", 52.338889, 4.872356),
    ("Beverwijk", 52.47833252, 4.656666756),
    ("Castricum", 52.54583359, 4.658611298),
    ("Delft", 52.00666809, 4.356389046),
    ("Den Haag Centraal", 52.08027649, 4.324999809),
    ("Den Helder", 52.95527649, 4.761111259),
    ("Dordrecht", 51.80722046, 4.66833353),
    ("Gouda", 52.01750183, 4.704444408),
    ("Haarlem", 52.38777924, 4.638333321),
    ("Heemstede-Aerdenhout", 52.35916519, 4.606666565),
    ("Hoorn", 52.64472198, 5.055555344),
    ("Leiden Centraal", 52.16611099, 4.481666565),
    ("Rotterdam Alexander", 51.95194626, 4.553611279),
    ("Rotterdam Centraal", 51.92499924, 4.46888876),
    ("Schiedam Centrum", 51.92124381, 4.408993721),
    ("Schiphol Airport", 52.30944443, 4.761944294),
    ("Zaandam", 52.43888855, 4.813611031)
]

# Verbindingen tussen stations (start_station, eind_station, reistijd)
verbindingen = [
    ("Alkmaar", "Hoorn", 24),
    ("Alkmaar", "Den Helder", 36),
    ("Amsterdam Amstel", "Amsterdam Zuid", 10),
    ("Amsterdam Amstel", "Amsterdam Centraal", 8),
    ("Amsterdam Centraal", "Amsterdam Sloterdijk", 6),
    ("Amsterdam Sloterdijk", "Haarlem", 11),
    ("Amsterdam Sloterdijk", "Zaandam", 6),
    ("Amsterdam Zuid", "Amsterdam Sloterdijk", 16),
    ("Amsterdam Zuid", "Schiphol Airport", 6),
    ("Beverwijk", "Castricum", 13),
    ("Castricum", "Alkmaar", 9),
    ("Delft", "Den Haag Centraal", 13),
    ("Den Haag Centraal", "Gouda", 18),
    ("Den Haag Centraal", "Leiden Centraal", 12),
    ("Dordrecht", "Rotterdam Centraal", 17),
    ("Gouda", "Alphen a/d Rijn", 19),
    ("Haarlem", "Beverwijk", 16),
    ("Heemstede-Aerdenhout", "Haarlem", 6),
    ("Leiden Centraal", "Heemstede-Aerdenhout", 13),
    ("Leiden Centraal", "Alphen a/d Rijn", 14),
    ("Leiden Centraal", "Schiphol Airport", 15),
    ("Rotterdam Alexander", "Gouda", 10),
    ("Rotterdam Centraal", "Schiedam Centrum", 5),
    ("Rotterdam Centraal", "Rotterdam Alexander", 8),
    ("Schiedam Centrum", "Delft", 7),
    ("Zaandam", "Castricum", 12),
    ("Zaandam", "Beverwijk", 25),
    ("Zaandam", "Hoorn", 26)
]

# Maak een basismap van Nederland (centraal punt)
m = folium.Map(location=[52.3794, 4.9009], zoom_start=8)

# Voeg stations toe als markers
station_dict = {name: (lat, lon) for name, lat, lon in stations}
for naam, (lat, lon) in station_dict.items():
    folium.Marker([lat, lon], popup=naam).add_to(m)

# Voeg verbindingen toe als lijnen tussen stations
for start, eind, reistijd in verbindingen:
    start_lat, start_lon = station_dict[start]
    eind_lat, eind_lon = station_dict[eind]
    folium.PolyLine([(start_lat, start_lon), (eind_lat, eind_lon)], color="blue", weight=2.5, opacity=0.8).add_to(m)

# Bewaar de kaart in een HTML bestand
m.save("stations_verbindingen.html")
