from list import *

class SparseMatrix():
    def __init__(self, elements):
        self.value_list = List()
        for sublist in elements:
            self.value_list.append(sublist)

    def transpose(self):
        for sub_list in self.value_list:
            i = sub_list[1][0]
            j = sub_list[1][1]
            sub_list[1] = [j, i]

    def __getitem__(self, index):
        for sub_list in self.value_list:
            if sub_list[1][0] == index[0]:
                if sub_list[1][1] == index[1]:
                    return sub_list[0]
        return 0

    def __setitem__(self, index, value):
        self.value_list.remove([self.__getitem__(index), list(index)])
        self.value_list.append([value, list(index)])

    def subtract(self, other):
        for sub_list in other:
            status = False
            for list in self.value_list:
                if sub_list[1][0] == list[1][0]:
                    if sub_list[1][1] == list[1][1]:
                        i = list[0] - sub_list[0]
                        self.__setitem__(list[1], i)
                        status = True
            if not status:
                l = sub_list
                l[0] = 0 - sub_list[0]
                self.value_list.append(l)

    def multiplay(self, other):
        for sub_list in self.value_list:
            row = sub_list[1][0]
            col = sub_list[1][1]
            row_values = []
            col_values = []
            for sub_list1 in self.value_list:
                if row == sub_list1[1][0]:
                    row_values.append(sub_list1)
            for sub_list2 in other:
                if col == sub_list2[1][1]:
                    col_values.append(sub_list2)
            value = 0
            for i in xrange(len(row_values)):
                value += row_values[i][0]*col_values[i][0]
            self.__setitem__([row, col], value)

    def add(self, other):
        for sub_list in other:
            status = False
            for list in self.value_list:
                if sub_list[1][0] == list[1][0]:
                    if sub_list[1][1] == list[1][1]:
                        i = list[0] + sub_list[0]
                        self.__setitem__(list[1], i)
                        status = True
            if not status:
                l = sub_list
                l[0] = 0 + sub_list[0]
                self.value_list.append(l)

