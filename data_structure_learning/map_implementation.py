class Map(object):
    def __init__(self):
        self.size = 50
        self.map = [[] for i in range(50)]

    def hash(self, element):
        if type(element) == int:
            return element % self.size
        else:
            i = 0
            type_of_char = type(element[0])
            if type_of_char == int:
                for char in element:
                    assert(type(char) == type_of_char)
                    i += char
            else:
                for char in element:
                    assert(type(char) == type_of_char)
                    i += ord(char)
            return i % self.size

    def __len__(self):
        i = 0
        for sublist in self.map:
            for element in sublist:
                i += 1
        return i

    def __contains__(self, key):
        index = self.hash(key)
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
                new_map[l[0]] = l[1]
        for element in other.map:
            for l in element:
                if l[0] not in new_map:
                    new_map[l[0]] = l[1]
        return new_map

    def __setitem__(self, key, value):
        assert(key != None and value != None)
        if type(key) == list or type(key) == str or type(key) == tuple:
            index = self.hash(key)
        else:
            assert(type(key) is int)
            index = self.hash(key)
        if key not in self:
            self.map[index].append([key, value])
        else:
            for element in self.map[index]:
                if element[0] == key[0]:
                    element[1] = value
                    break

    def clear(self):
        self.__init__()

    def __getitem__(self, key):
        index = self.hash(key)
        mini_list = self.map[index]
        for element in mini_list:
            if element[0] == key:
                return element[1]
        raise KeyError

    def items(self):
        items = []
        for element in self.map:
            for l in element:
                items.append((l[0], l[1]))
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
        elements = []
        for sublist in self.map:
            for element in sublist:
                elements.append(element)
        return str(elements)

    def __repr__(self):
        return self.__str__()
'''        
    def rehash(self, oldhash, size):
        return (oldhash = oldhash + 1) % size
'''
