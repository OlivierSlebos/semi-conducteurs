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
## Random algoritme
Dit algoritme maakt alle keuzes random. Hij kiest een random aantal treinen dat gaat rijden tussen trein_min en trein_max en 
kiest per trein een random aantal minuten om te reiden tussen minuten_min en minuten_max. De treinen beginnen op een random station 
en kiezen op elk station een random connectie om te rijden, totdat de trein op een station aankomt waar bij alle mogelijke opties de reistijd wordt overschreden. Dat is dan het eindstation. 

## korste_afstand_greedy.py
Het algoritme begint met het aanmaken van een aantal lege lijsten waarin de gereden trajecten, verbindingen en de totale rijtijd worden opgeslagen. Vervolgens wordt willekeurig bepaald hoeveel trajecten worden gegenereerd, dit wordt vanuit de main meegegeven aan de functie. Ook wordt er gekozen voor heel nederland of alleen noord- en zuid-holland.

Voor elk traject kiest het algoritme een willekeurig startstation, waarna de trein begint te rijden. De trein blijft rijden zolang er nog tijd over is binnen het traject. Bij iedere stap selecteert de trein de kortste beschikbare verbinding vanuit het huidige station naar een ander station. Wanneer alle verbindingen van het huidige station al bereden zijn, kiest de trein een willekeurige verbinding om vastlopen te voorkomen. Wanneer er naast onbereden verbinding, ook geen tijd meer is om een random verbinding te rijden, stopt het traject.

Aan het einde wordt er een csv bestand aangemaakt met de resultaten van ieder traject.

## Hill Climber Algoritme
Het algoritme begint met het aanmaken van een random oplossing met het algoritme Algorithms/Random_algorithm_2. De uitkomsten van deze eerste oplossing worden opgeslagen in 2 dicts. Dict 1 is de huidige oplossing, deze zal steeds een copy bevatten van de oplossing die de huidige hoogste score bevat. Dict 2 is een tijdelijke oplossing, de Hill Climber past deze telkens aan. Wanneer de aanpassingen in Dict 2 tot een hogere score lijden zal Dict 1 (huidig) doormiddel van een Deepcopy worden overschreven door Dict 2 (tijdelijk). Wanneer de aanpassingen tot een lagere score leiden zal Dict 2 (tijdelijk) worden overschreven door Dict 1 (huidig) doormiddel van een Deepcopy. In beide gevallen (beter of niet) zal het algoritme opnieuw Dict 2 (tijdelijk) aanpassen om tot een betere score te komen. 

Het aanpassen werkt Dict 2 (tijdelijk) werkt alsvolgt. 
Er wordt een aantal trajecten gekozen dat wordt verwijderder tussen 0 en het huidige aantal trajecten. 
Vervolgens wordt alle informatie van deze trajecten/ treinen verwijderd.
Daarna wordt er een aantal trajecten gekozen dat wordt toegevoegd. Dit aantal is altijd zo dat het nieuwe aantal treinen tussen het minimum en maximum aantal trajecten/ treinen komt dat vooraf is meegegeven. 
Deze nieuwe trajecten worden gegenereerd. 
Het genereren algoritme kan Rand

## Score greedy algoritme 
Dit algoritme zet een trein op een random beginstation. Dan gaat hij alle mogelijke connecties vanaf dat station langs en rijdt hij degene die in de hoogste score resulteert. Dit doet hij totdat er op een station geen opties zijn die de maximale reistijd niet overschreiden. Ook stopt hij wanneer alle unieke connecties zijn gereden. 

## Connectie algoritme 
Dit algoritme volgt bovenop het random algoritme 2 heuristieken. Het startstation is altijd een station
waar nog onbereden connecties zijn, en het algoritme kiest als mogelijk op elk station een connectie die nog niet is gereden. Als er
meerdere connecties onbereden zijn dan maakt het algoritme een random keuze. Als er geen connecties meer onbereden zijn op een station 
dan maakt het algoritme ook een random keuze. De trein stopt wanneer alle connecties op een station de maximale reistijd overschreiden.

## resultaten reproduceren:
1. Ga naar de directory semi-conducteurs
2. Run "python3 main.py", hier wordt er gevraagd naar:
* Hoeveel treinen je wilt dat er minimaal reiden
* hoeveel treinen je wilt dat er maximaal reiden
* De minimale aantal minuten per trein
* De maximale aantal minuten per trein
* Waar je het algorimte op wilt laten runnen, nederland of holland
* hoevaak je het algoritme wilt laten runnen
* welk algoritme je wilt laten runnen

3. De resultaten van alle runs zijn nu zichtbaar in de map resulaten/Runs
4. Run nu "python3 Visualisation/Graphs/plot.py". De resultaten zijn nu zichtbaar in grafieken, in de files boxplot_treinen_scores.png en binned_bargraph_fraction.png.
* Wanneer hill-climber gerunt is, wordt er automatisch al een grafiek gemaakt. Deze is te vinden in de file Visualisation/Graphs/Hill_Climber_grafiek.png

## Een kaart maken van je CSV resultaat
1. Ga naar de directory semi-conducteurs
2. Run python3 -m Visualisation.Map.Kaart_maken_per_trein
* Van welke file wil je een kaart maken?
* Welke kaart hoort bij deze dienstregeling? (holland/nederland):

De kaart zal worden geopend in je webbrowser & je zal een melding krijgen waar de kaart terug te vinden is. 
* De kaart is opgeslagen. Bekijk de kaart op: (...)/semi-conducteurs/Visualisation/Map/resultaten_kaart.html