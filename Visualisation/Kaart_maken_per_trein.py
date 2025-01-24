import folium

import ast

from kaart_maken import station_uit_csv, verbinding_uit_csv

def kaart_maken_csv(filename):
    
    is_visited = []
    verbindingen_geweest_2 = []

    with open(f'resultaten/{filename}') as f:
        #Sla de eerste rij over
        line = f.readline()

        while line != 'EOF':
            line = f.readline()
            if line == "EOF\n":
                break
            # print(F"1: {line}") #trein nummer
            line = f.readline()
            # print(F"2: {line}") #Verbindingen

            #Voeg verbindingen toe
            result = ast.literal_eval(line)
            verbindingen_geweest_2.append(result)
            # print(verbindingen_geweest_2)

            #Pak de lijst met stations en voeg die toe
            line = f.readline()
            # print(F"3: {line}")
            result = line.strip().split(',')
            # print(F"4: {result}")
            is_visited.append(result)

            # #Volgende line
            line = f.readline()
            # print(line)
    kaart_maken_voor_csv(is_visited, verbindingen_geweest_2)

def kaart_maken_voor_csv(is_visited, verbindingen_geweest):
    
    stations = station_uit_csv("Data/stations.csv")
    verbindingen = verbinding_uit_csv("Data/connecties.csv")
    
    # Maak een basismap van Nederland (centraal punt)
    m = folium.Map(location=[52.3794, 4.9009], zoom_start=8, tiles='CartoDB Positron')

    # Voeg stations toe als markers
    station_dict = {name: [lat, lon] for name, lat, lon in stations}

    # for g in station_dict:
    #     station_dict[g].append([])

    for naam, (lat, lon) in station_dict.items():
        if naam in is_visited: color = 'blue'
        else: color = 'red'
        folium.Marker([lat, lon], popup=naam, icon=folium.Icon(color=color)).add_to(m)

    #Voeg verbindingen toe als lijnen tussen stations
    colors = [
    'yellow',
    'orange',
    'green',
    'blue',
    'purple',
    'blue',
    'black'
    ]
    i = 0
    #FOR-LOOP per trein toevoegen
    for g in verbindingen_geweest:
        color = colors[i]
        schuiven = 0.0001 + (i / 1000)
        i += 1
        for s in g:
            #Uit de lijst van verbindingen halen
            if eval(s) in verbindingen:
                plaats = verbindingen.index(eval(s))
                verbindingen.pop(plaats)
            start, eind, reistijd = eval(s)
            start_lat, start_lon = station_dict[start]
            eind_lat, eind_lon = station_dict[eind]
            folium.PolyLine([(start_lat + schuiven, start_lon + schuiven), (eind_lat + schuiven, eind_lon + schuiven)], color=color, weight=4, opacity=0.5).add_to(m)
    
    #Alleen als verbinding al is gereden stukje opschuiven

    #Alles wat over is rood maken
    for start, eind, reistijd in verbindingen:
        start_lat, start_lon = station_dict[start]
        eind_lat, eind_lon = station_dict[eind]
        color = 'red'
        folium.PolyLine([(start_lat, start_lon), (eind_lat, eind_lon)], color=color, weight=2.5, opacity=0.8).add_to(m)

    # Bewaar de kaart in een HTML bestand
    m.save("Visualisation/resultaten_kaart.html")

if __name__ == "__main__":
    kaart_maken_csv("OEPS.csv")