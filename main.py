from Classes.Kaart import Kaart

from Visualisation.kaart_maken import kaart_maken

from Algorithms.random_algorithm import genereer_lijnvoering

from Helpers import genereer_output, run_algoritme, schrijf_output

if __name__ == "__main__":
    spel = Kaart()

    #  NAAM VAN HET ALGORITME, SPEL, AANTAL TREINEN
    run_algoritme(genereer_lijnvoering, spel, 7)

    schrijf_output([['Amsterdam', 'Alkmaar'], ['Kosmos', 'New York']], [('verbinding','Den Helder', 'Schieddam'), ('verbinding','Gorichem', 'Kaapstad')], 5, 65, 12)

    
    
    
    
    #In alg stop je het spel
    #Uitkomt moet een Tuple (list[stations], list[verbindingen]) zijn uit history

    # lijst_stations_gereden = []
    # lijst_connecties_gerenden = []

    # for i in range(7):
    #     #Voer het algoritme uit
    #     antwoord = genereer_lijnvoering(spel)

    #     #Sla de uitkomsten van de 
    #     lijst_stations_gereden.extend(antwoord[0])
    #     lijst_connecties_gerenden.extend(antwoord[1])
    #     genereer_output(antwoord[0], antwoord[1], i)

    # kaart_maken(lijst_stations_gereden, lijst_connecties_gerenden)

    
