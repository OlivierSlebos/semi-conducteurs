from stations import Station

class History:
    def __init__(self):
        self._data: list[str] = list()

    # add element to top of stack
    def push(self, element: Station) -> None:
        self._data.append(element)

    # remove and return element from top of stack
    def pop(self) -> Station:
        assert len(self._data) > 0
        return self._data.pop()