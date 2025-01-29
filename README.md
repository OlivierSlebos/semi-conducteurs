# semi-conducteurs
## RailNL case
RailNL is gericht op het optimaliseren van de lijnvoering voor intercitytreinen in Nederland. De lijnvoering bepaalt welke trajecten treinen gedurende de dag heen en weer rijden binnen een hoe lang die trajecten mogen zijn. Dit project richtte zich in het eerste deel op de lijnvoering van noord- en zuid-holland, waarna het einddoel was om de meest efficiente lijnvoering voor nederland te ontwerpen.
Deze lijnvoering maken wordt gedaan aan de hand van verschillende algoritmen en heuristieken. 

De kwaliteit van een lijnvoering, bestaande uit meerdere trajecten, wordt gemeten door middel van een berekening: k = p\*10.000-(T\*100+min). 
* p is het fractie van de gereden connecties (aantal gereden connecties/totale aantal connectiens = maximaal 1).
* T is het aantal treinen die er gereden hebben, gelijk aan het aantal trajecten.
* min staat voor het aantal minuten dat er gereden is in alle trajecten samen: de lijnvoering. 

Voor het eerste deel zijn er in totaal 22 verbindingen in noord- en zuid-holland, waar een trein maximaal 120 minuten mag rijden met maximaal 7 treinen.

Voor heel nederland mogen er 20 trajceten in totaal rijden, waar er 89 verbindingen zijn en er maximaal 180 minuten per trein gereden wordt. 

# inplementatie
## korste_afstand_greedy.py
Het algoritme begint met het aanmaken van een aantal lege lijsten waarin de gereden trajecten, verbindingen en de totale rijtijd worden opgeslagen. Vervolgens wordt willekeurig bepaald hoeveel trajecten worden gegenereerd, dit wordt vanuit de main meegegeven aan de functie. Ook wordt er gekozen voor heel nederland of alleen noord- en zuid-holland.

Voor elk traject kiest het algoritme een willekeurig startstation, waarna de trein begint te rijden. De trein blijft rijden zolang er nog tijd over is binnen het traject. Bij iedere stap selecteert de trein de kortste beschikbare verbinding vanuit het huidige station naar een ander station. Wanneer alle verbindingen van het huidige station al bereden zijn, kiest de trein een willekeurige verbinding om vastlopen te voorkomen. Wanneer er naast onbereden verbinding, ook geen tijd meer is om een random verbinding te rijden, stopt het traject.

Aan het einde wordt er een csv bestand aangemaakt met de resultaten van ieder traject.

## resultaten reproduceren:
1. Ga naar de directory semi-conducteurs
2. Run python3 main.py, hier wordt er gevraagd naar:
* Hoeveel treinen je wilt dat er minimaal reiden
* hoeveel treinen je wilt dat er maximaal reiden
* De minimale aantal minuten per trein
* De maximale aantal minuten per trein
* Waar je het algorimte op wilt laten runnen, nederland of holland
* hoevaak je het algoritme wilt laten runnen
* welk algoritme je wilt laten runnen

3. De resultaten van alle runs zijn nu zichtbaar in de map resulaten/Runs
4. Run nu python3 Visualisation/Graphs/plot.py. De resultaten zijn nu zichtbaar in grafieken, in de files boxplot_treinen_scores.png en binned_bargraph_fraction.png.
* Wanneer hill-climber gerunt is, wordt er automatisch al een grafiek gemaakt. Deze is te vinden in de file Hill_Climber_grafiek.png
