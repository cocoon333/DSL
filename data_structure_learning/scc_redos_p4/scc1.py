class SCC(object):
    def __init__(self):
        self.finish_time = 0

    def scc(self, data):
        #data is [[node1, node2], [node2, node3], [node3, node1]] eg: [[0, 1], [1, 2], [2, 0]]
        data_r = self.reverse(data) # [[node2], [node3], [node1]] eg: [[2], [0], [1]]
        finish_time_dictionary = {}# {finishing_time_of_node:node} eg: {0:1, 1:0}
        leader_map = {} # {leader: nodes in this scc} eg: {2:[2, 1, 0]}
        visited_nodes = set()
        self.finish_time = 0
        for i in range(len(data_r)-1, -1, -1):
            self.dfs_cf(data_r, i, visited_nodes, finish_time_dictionary)

        visited_nodes = set()
        for i in range(len(data)-1, -1, -1):
            self.dfs_cl(data, finish_time_dictionary[i], visited_nodes, finish_time_dictionary[i], leader_map)

        return leader_map

    def reverse(self, data):
        r_data = []
        for i in range(len(data)):
            r_data.append([])
        i = 0
        for node in data:
            for connection in node:
                r_data[connection].append(i)
            i += 1
        return r_data

    def dfs_cf(self, data, node, visited_nodes, finish_time_dictionary):
        if node not in visited_nodes:
            visited_nodes.add(node)
            for n in data[node]:
                self.dfs_cf(data, n, visited_nodes, finish_time_dictionary)
            assert (self.finish_time not in finish_time_dictionary)
            finish_time_dictionary[self.finish_time] = node
            self.finish_time += 1

    def dfs_cl(self, data, node, visited_nodes, leader, leader_map):
        if node not in visited_nodes:
            visited_nodes.add(node)
            if leader in leader_map:
                leader_map[leader].append(node)
            else:
                leader_map[leader] = [node]
            for n in data[node]:
                self.dfs_cl(data, n, visited_nodes, leader, leader_map)
