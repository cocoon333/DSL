#from pro9_chapt3_reverse_selection_sort import selectionSort
class List():
    def __init__(self, elements=[]):
        self.lyst = []
        for element in elements:
            self.lyst.append(element)

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

    def __str__(self):
        return str(self.lyst)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, index):
        return self.lyst[index]

    def __setitem__(self, index, value):
        self.lyst[index] = value

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
