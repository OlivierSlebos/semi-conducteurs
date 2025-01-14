def score_bereken(treinen, minuten, verbindingen) -> int:

    # fractie gereden verbindingen, 28 verbindingen totaal
    p = verbindingen / 28
    score = p * 1000 - ((treinen * 100) + minuten)
    return score


def score_bereken_csv(filename: str) -> int:

    with open(filename) as f:
        line = f.readline()

        #gevens splitsen
        gegevens = line.split(',')
        
        aantal_treinen = int(gegevens[0])
        aantal_minuten = int(gegevens[1])
        aantal_verbindingen = int(gegevens[2])
        # fractie gereden verbindingen, 28 verbindingen totaal
        p = aantal_verbindingen / 28
        score = p * 1000 - ((aantal_treinen * 100) + aantal_minuten)
            
    return score





