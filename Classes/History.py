from Station import Station

class History:
    def __init__(self):

        #List van station al geweest
        self._data: list[str] = list()

        #List van geweeste conecties
        self._data_connectie: list[tuple[str,str,int]] = []

    # add element to top of stack
    def push(self, element: str) -> None:
        self._data.append(element)

    # remove and return element from top of stack
    def pop(self) -> Station:
        assert len(self._data) > 0
        return self._data.pop()
    
    #Zet een connectie in de lijst
    def push_connectie(self, element: tuple[str,str,int]) -> None:
        self._data_connectie.append(element)