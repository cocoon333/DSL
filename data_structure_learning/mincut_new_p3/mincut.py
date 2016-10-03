import random
import math
import copy
import datetime

class MinCut(object):
    def __init__(self):
        random.seed(0)
        self.replace_vertice_table = {}

    def mincut(self, data):
        # data = {v: list of vertex}, where v is a vertice, list of vertex is list of connected vertex to v
        # for example, {v1: [v2, v3], v2: [v1, v3]}, v1 is connected to v2, v3, v2 is connected v1, v3
        assert(data)
        assert (self.is_connected_graph(data))
        key_len = len(data.keys())
        if key_len == 1:
            return 0
        res = 'a'
        for i in xrange(key_len**2+int(math.log(key_len, 2))):
            d = copy.deepcopy(data)
            self.replace_vertice_table = {}
            possible_res = self._mincut_rec(d)
            if possible_res < res:
                res = possible_res
            if (i%1000 == 0):
                print ("[%s]: tried time is %d, current min cut is %d, current cut is %d" % (datetime.datetime.now().time(), i, res, possible_res))
        return res

    def is_connected_graph(self, data):
        return True

    def replace_vertices(self, data, n):
        for i in xrange(len(data[n])):
            while data[n][i] in self.replace_vertice_table:
                data[n][i] = self.replace_vertice_table[data[n][i]]

    def _mincut_rec(self, data):
        if len(data.keys()) == 2:
            return len(data[data.keys()[0]])
        assert(len(data.keys())>2)
        n1 = data.keys()[random.randint(0, len(data.keys())-1)]
        self.replace_vertices(data, n1)
        assert (n1)
        n2 = data[n1][random.randint(0, len(data[n1])-1)]
        self.replace_vertices(data, n2)
        assert (n1 in data)
        assert (n2 in data)
        to_delete = []
        for i in xrange(len(data[n1])):
            if data[n1][i] == n2:
                to_delete.append(n2)
        for i in to_delete:
            data[n1].remove(i)
        for connected_vertice in data[n2]:
            assert (connected_vertice not in self.replace_vertice_table)
            if connected_vertice != n1:
                data[n1].append(connected_vertice)
        assert (n2 not in data[n1])
        self.replace_vertice_table[n2] = n1
        del data[n2]
        return self._mincut_rec(data)
