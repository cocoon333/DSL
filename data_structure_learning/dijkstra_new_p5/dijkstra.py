import heapq

class Heap(object):
    def __init__(self):
        self.INVALID_NODE = -1
        self.h = []
        self.node_entry = {} # {node: entry}

    def push(self, distance, node):
        entry = [distance, node]
        self.node_entry[node] = entry
        heapq.heappush(self.h, entry)

    def pop(self):
        (d, n) = (None, None)
        while True:
            (d, n) = heapq.heappop(self.h)
            if n != self.INVALID_NODE:
               break
        del self.node_entry[n]
        return (d, n)

    def delete(self, node):
        assert (node in self.node_entry)
        entry = self.node_entry[node]
        entry[1] = self.INVALID_NODE
        del self.node_entry[node]

    def __len__(self):
        return len(self.node_entry)

    def __contains__(self, node):
        return node in self.node_entry


    def __getitem__(self, node):
        assert (node in self.node_entry)
        return self.node_entry[node]
        

class Dijkstra(object):
    def __init__(self):
        self.MAX_DISTANCE = 1000000
           
    def dijkstra(self, data):
        # data: [[connected node1,distance1, connected node2,distance2]] eg. [[1,2, 2,3], [0,2], [0,3]]
        # returns {node1:distance to node1, node2: distance to node2, node3: distance to node3}
        unvisited_heap = Heap() #  item: [distance to 0, node1]
        visited_map = {} #  {node1:distance to node1, node2: distance to node2, node3: distance to node3}

        unvisited_heap.push(0, 0)
        for i in range(1, len(data)):
            unvisited_heap.push(self.MAX_DISTANCE, i)

        while len(unvisited_heap) > 0:
            (d0w, w) = unvisited_heap.pop()
            visited_map[w] = d0w
            for (v, dwv) in zip(data[w][::2], data[w][1::2]):
                if v in unvisited_heap:
                    d0v = unvisited_heap[v]
                    unvisited_heap.delete(v)
                    d0v = min(d0v[0], d0w+dwv)
                    unvisited_heap.push(d0v, v)

        return visited_map
