import sys
sys.setrecursionlimit(8000000)

class SCC(object):
    def __init__(self):
        self.finishing_time = 0

    def scc(self, data):
        r_data = self.reverse(data)
        finishing_time_dictionary = {}
        leader_map = {}
        self.finishing_time = 0
        visited_nodes = set()

        for i in xrange(len(data)-1, -1, -1):
            self.dfs_cf(r_data, i, visited_nodes, finishing_time_dictionary)
        visited_nodes = set()

        for i in xrange(len(data)-1, -1, -1):
            self.dfs_cl(data, finishing_time_dictionary[i], visited_nodes, finishing_time_dictionary[i], leader_map)

        return leader_map

    def reverse(self, data):
        r_data = []
        for i in xrange(len(data)):
            r_data.append([])
        
        for i in xrange(len(data)):
            for connection in data[i]:
                r_data[connection].append(i)
        return r_data

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
