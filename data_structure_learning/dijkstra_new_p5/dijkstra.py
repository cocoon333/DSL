import heapq

class Heap(object):
    def __init__(self):
        self.h = []
        self.item_set = set()

    def push(self, item):
        self.item_set.add(item)
        heapq.heappush(self.h, item)

    def pop(self):
        while True:
            item= heapq.heappop(self.h)
            if item in self.item_set:
               break
        self.item_set.remove(item)
        return item

    def delete(self, item):
        assert (item in self.item_set)
        self.item_set.remove(item)
        

class Dijkstra(object):
    def __init__(self, data): 
        self.data = data

    def dijkstra(self):
        # data: [[connected node1,distance1, connected node2,distance2]] [[1,2, 2,3], [0,2], [0,3]]
        # returns {node1:distance to node1, node2: distance to node2, node3: distance to node3}
        unvisited_heap = []
        #  [[distance to 0, node1], [distance to 0, node2]]
        visited_list = []
        #  [[distance to 0, node1], [distance to 0, node2]]
        visited_set = set()
        entry_finder = {}

        visited_list.append([0, 0])
        visited_set.add(0)
        for i in xrange(1, len(self.data)):
            distance = self.calculate_distance(visited_list, self.data[i])
            entry = [distance, i]
            entry_finder[i] = entry
            heapq.heappush(unvisited_heap, entry)
        assert(len(unvisited_heap) == len(self.data)-1)

        while len(unvisited_heap) > 0:
            while True:
                w = heapq.heappop(unvisited_heap)
                if w[1] != -1:
                    break
                assert (w[1] not in entry_finder)
            del entry_finder[w[1]]
            assert (w[0] > 0)
            assert (w[1] < len(self.data))
            visited_list.append(w)
            visited_set.add(w[1])
            for v in self.data[w[1]][::2]:
                if v not in visited_set:
                    assert v in entry_finder
                    entry_finder[v][-1] = -1
                    del entry_finder[v]
                    distance = self.calculate_distance(visited_list, self.data[v])
                    entry = [distance, v]
                    heapq.heappush(unvisited_heap, entry)
                    entry_finder[v] = entry
        return visited_list

    def calculate_distance(self, visited_list, edge_list):
        #  visit_list: [[distance to 0, node1], [distance to 0, node2]]
        #  edge_list:  [connected node1,distance1, connected node2,distance2]
        # return distance from 0 to node, 1000000 means no connection
        possible_distances = []
        for visited_node in visited_list:
            if visited_node[1] in node:
                i = node.index(visited_node[0])
                possible_distances.append(visited_node[1] + node[i+1])
        if possible_distances:
            return min(possible_distances)

        return 1000000
