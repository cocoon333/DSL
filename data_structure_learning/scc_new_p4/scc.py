import datetime
import sys

sys.setrecursionlimit(15000)

class SCC(object):
    def __init__(self):
        self.finish_time = 0

    def scc(self, data):
        # data = [[1], [2], [0]], represents 0 -> 1, 1 -> 2, 2 -> 0
        # return [[0, 1, 2]]
        data_r = self.reverse(data)
        finish_time_map = {} # {finish_time : node}
        leader_map = {} # {leader node: [node, ...]}
        visited_nodes = set()
        self.finish_time = 0
        for i in range(len(data_r)-1, -1, -1):
            self.dfs_ft(data_r, i, visited_nodes, finish_time_map)
            if i % 1000 == 0:
                print 'datetime.datetime.now()' + "the finish_time is %d" % self.finish_time
        assert(self.finish_time == len(data))
        visited_nodes = set()
        for i in range(len(data)-1, -1, -1):
            self.dfs_cl(data, finish_time_map[i], visited_nodes, finish_time_map[i], leader_map)
            if i % 1000 == 0:
                print 'datetime.datetime.now()' + "the new leader entry is %s" % str(leader_map[i])

        return leader_map

    def reverse(self, data):
        res = []
        for i in range(len(data)):
            res.append([])
        for i in range(len(data)):
            for d in data[i]:
                res[d].append(i)
        return res

    def dfs_ft(self, data, node, visited_nodes, finish_time_map):
        assert (node >= 0 and node < len(data))
        if node in visited_nodes:
            return
        visited_nodes.add(node)
        for n in data[node]:
            self.dfs_ft(data, n, visited_nodes, finish_time_map)
        assert (self.finish_time not in finish_time_map)
        assert (self.finish_time >= 0 and self.finish_time < len(data))
        finish_time_map[self.finish_time] = node
        self.finish_time += 1

    def dfs_cl(self, data, node, visited_nodes, leader, leader_map):
        assert (node >= 0 and node < len(data))
        assert (leader >= 0 and leader < len(data))
        if node in visited_nodes:
            return
        visited_nodes.add(node)
        if leader in leader_map:
            leader_map[leader].append(node)
        else:
            leader_map[leader] = [node]
        for n in data[node]:
            self.dfs_cl(data, n, visited_nodes, leader, leader_map)
