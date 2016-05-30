class Map:
    def __init__(self):
        self.size = 50
        self.map = [[None, None]] * self.size

    def hash(self, element, size):
        if type(element) == int:
            return element % size

        else:
            i = 0
            for char in element:
                i += ord(char)
                return i % size

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        index = key % self.size
        if key == self.map[index][0]:
            return True
        else:
            for element in self.map[index+1:]:
                if key == element[0]:
                    return True
            return False

    def __eq__(self, other):
        if len(self) == len(other):
            for element in self.map:
                if element in other:
                    pass
                else:
                    return False
            return True

    def __add__(self, other):
        new_map = Map()
        for element in self.map:
            new_map.add(element)
        for element in other.map:
            new_map.add(element)
        return new_map

    def add(self, sub_list):
        self.map.append(sub_list)

    def clear(self):
        self.map = []

    def get(self, key):
        for element in self.map:
            if key in element:
                return element[1]
        raise KeyError

    def has_key(self, key):
        for element in self.map:
            if key in element:
                return True
        return False

    def items(self):
        items = []
        for element in self.map:
            items.append(element[1])
        return items

    def keys(self):
        keys = []
        for element in self.map:
            keys.append(element[0])
        return keys

    def remove(self, key):
        for element in self.map:
            if element[0] == key:
                index = self.map.index(element)
                del self.map[index]

    def __str__(self):
        return str(self.map)

    def __repr__(self):
        return self.__str__()
'''        
    def rehash(self, oldhash, size):
        return (oldhash = oldhash + 1) % size
'''
