from Classes.Station import Station

class History:
    """
    De History-klasse houdt een geschiedenis bij van de stations en verbindingen die door een trein zijn bereden.
    Dit wordt gebruikt om het afgelegde traject bij te houden.
    """
    def __init__(self):

        #List van station al geweest
        self._data: list[str] = list()

        #List van geweeste conecties
        self._data_connectie: list[tuple[str,str,int]] = []

    def push(self, element: str) -> None:
        """
        Voegt een station toe aan de bezochte geschiedenis.

        element: De naam van het station dat is bezocht.
        """
        self._data.append(element)

    def pop(self) -> Station:
        # remove and return element from top of stack
        assert len(self._data) > 0
        return self._data.pop()
    
    #Zet een connectie in de lijst
    def push_connectie(self, element: tuple[str,str,int]) -> None:
        """
        Voegt een bereden verbinding toe aan de geschiedenis.
        """
        self._data_connectie.append(element)