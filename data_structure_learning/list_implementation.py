from pro9_chapt3_reverse_selection_sort import selectionSort
class List():
    def __init__(self):
        self.lyst = []

    def __len__(self):
        i = 0
        for element in self:
            i += 1
        return i

    def __contains__(self, element):
        for thing in self:
            if element == thing:
                return True
        return False

    def append(self, element):
        self.lyst.insert(self.__len__(), element)

    def remove(self, element):
        self.lyst.remove(element)

    def index(self, element):
        i = 0
        for thing in self:
            if element == thing:
                return i
            i += 1
        raise ValueError

    def count(self, element):
        count = 0
        for thing in self:
            if thing == element:
                count += 1
        return count

    def __iter__(self):
        return Iterator(self)

    def sort(self):
        return selectionSort(self.lyst)


class Iterator:
    def __init__(self, list):
        self.index = 0
        self.list = list.lyst

    def __iter__(self):
        return self

    def next(self):
        res = None
        if self.index< len(self.list):
            res = self.list[self.index]
            self.index += 1
            return res
        raise StopIteration
