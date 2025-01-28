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

# implementatie

## random algoritme



