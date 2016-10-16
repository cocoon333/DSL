import sys

sys.setrecursionlimit(8000000)

class SCC(object):
    def __init__(self):
        self.finishing_time = 0

    def scc(self, data):
        data_r = self.reverse(data)
        self.finishing_time = 0
        finishing_time_dictionary = {}
        leader_map = {}
        visited_nodes = set()

        for i in xrange(len(data)-1, -1, -1):
            self.dfs_cf(data_r, i, visited_nodes, finishing_time_dictionary)

        visited_nodes = set()
        for i in xrange(len(data)-1, -1, -1):
           self.dfs_cl(data, finishing_time_dictionary[i], visited_nodes, finishing_time_dictionary[i], leader_map)

        return leader_map

    def reverse(self, data):
        data_r = []
        for i in xrange(len(data)):
            data_r.append([])

        for i in xrange(len(data)):
            for connection in data[i]:
                data_r[connection].append(i)
        return data_r

    def dfs_cf(self, data, node, visited_nodes, finishing_time_dictionary):
        if node not in visited_nodes:
            visited_nodes.add(node)
            for connection in data[node]:
                self.dfs_cf(data, connection, visited_nodes, finishing_time_dictionary)
            assert(self.finishing_time not in finishing_time_dictionary)
            finishing_time_dictionary[self.finishing_time] = node
            self.finishing_time += 1

    def dfs_cl(self, data, node, visited_nodes, leader, leader_map):
        if node not in visited_nodes:
            visited_nodes.add(node)
            if leader in leader_map:
                leader_map[leader].append(node)
            else:
                assert(leader not in leader_map)
                assert(node == leader)
                leader_map[leader] = [node]
            for connection in data[node]:
                self.dfs_cl(data, connection, visited_nodes, leader, leader_map)
