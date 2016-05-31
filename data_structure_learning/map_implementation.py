class Map:
    def __init__(self):
        self.size = 50
        self.map = [[] for i in range(50)]

    def hash(self, element, size):
        assert(type(element) == int or type(element) == str)
        if type(element) == int:
            return element % size

        else:
            i = 0
            for char in element:
                i += ord(char)
            return i % size

    def __len__(self):
        i = 0
        for element in self.map:
            if len(element) != 0:
                i += 1
        return i

    def __contains__(self, key):
        index = self.hash(key, self.size)
        for l in self.map[index]:
            assert (len(l) == 2)
            if key == l[0]:
                return True
        return False

    def __eq__(self, other):
        if len(self) == len(other):
            for element in self.map:
                try:
                    if element[0] in other:
                        pass
                    else:
                        return False
                except:
                    pass
            return True
        return False

    def __add__(self, other):
        new_map = Map()
        for element in self.map:
            for l in element:
                new_map.add(l)
        for element in other.map:
            for l in element:
                if l[0] not in new_map:
                    new_map.add(l)
        return new_map

    def add(self, sub_list):
        assert(len(sub_list)==2)
        assert(sub_list[0] != None and sub_list[1] != None)
        index = self.hash(sub_list[0], self.size)
        self.map[index].append(sub_list)

    def clear(self):
        self.map = []

    def get(self, key):
        index = self.hash(key, self.size)
        mini_list = self.map[index]
        for element in mini_list:
            if element[0] == key:
                return element[1]
        raise KeyError

    def has_key(self, key):
        for element in self.map:
            for l in element:
                if key == l[0]:
                    return True
        return False

    def items(self):
        items = []
        for element in self.map:
            for l in element:
                items.append(l[1])
        return items

    def keys(self):
        keys = []
        for element in self.map:
            for l in element:
                keys.append(l[0])
        return keys

    def remove(self, key):
        for element in self.map:
            for l in element:
                if l[0] == key:
                    element.remove(l)

    def __str__(self):
        return str(self.map)

    def __repr__(self):
        return self.__str__()
'''        
    def rehash(self, oldhash, size):
        return (oldhash = oldhash + 1) % size
'''
