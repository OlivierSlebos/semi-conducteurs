def score_bereken(treinen, minuten, verbindingen) -> float:

    # fractie gereden verbindingen, 28 verbindingen totaal
    p = verbindingen / 28
    score = p * 10000 - ((treinen * 100) + minuten)
    return score


def score_bereken_csv(filename: str) -> int:

    with open(f"resultaten/{filename}") as f:
        line = f.readline()

        #gevens splitsen
        gegevens = line.strip().split(',')
        
        aantal_treinen = int(gegevens[0])
        aantal_minuten = int(gegevens[1])
        aantal_verbindingen = float(gegevens[2])
        # fractie gereden verbindingen, 28 verbindingen totaal
        p = aantal_verbindingen / 28
        score = p * 10000 - ((aantal_treinen * 100) + aantal_minuten)
            
    return score