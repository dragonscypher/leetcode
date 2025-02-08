from sortedcontainers import SortedList

class NumberContainers:
    def __init__(self):
        self._d = {}
        self._indexes = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        old_number = self._d.get(index, None)
        if old_number is not None:
            self._indexes[old_number].remove(index)
        
        self._d[index] = number
        self._indexes[number].add(index)

    def find(self, number: int) -> int:
        sl = self._indexes[number]
        if len(sl) == 0:
            return -1
        return sl[0]
