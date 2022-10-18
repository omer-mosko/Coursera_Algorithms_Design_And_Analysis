
from collections import defaultdict
import numpy as np

class Graph():
    def __init__(self, filename):
        self.V = 0
        self.adjlist = defaultdict(list)
        with open(filename, 'r') as f:
            for line in f:
                splitline = line.split()
                for i in splitline[1:]:
                    print(int(splitline[0]), ",", int(i.split(',')[0]), ",", int(i.split(',')[1]))
                    self.add_edge(int(splitline[0]), int(i.split(',')[0]), int(i.split(',')[1]))
    def add_edge(self, src, dst, weight):
        if src not in self.adjlist.keys():
            self.V += 1
        self.adjlist[src].append((dst, weight))
    def get_neighbours(self, v):
        return [u[0] for u in self.adjlist[v]]
    def print_graph(self):
        for src, dst in self.adjlist.items():
            print("From ", src, " to ", ', '.join(' weight '.join((str(elm) for elm in tup)) for tup in dst))
        # return
    def findMin(self, dist, visited):
        min = np.Inf
        for v in self.adjlist:
            if v not in visited and dist[v - 1] < min:
                min = dist[v - 1]
                minV = v
        return minV
    def dijkstra(self, src, printV):
        visited = set()
        dist = [np.Inf for _ in range(self.V)]
        dist[src] = 0
        while len(visited) < self.V:
            # for v in self.adjlist:
            u = self.findMin(dist, visited)
            visited.add(u)
            for vertex, weight in self.adjlist[u]:
                if vertex not in visited and dist[vertex - 1] > dist[u - 1] + weight:
                    dist[vertex - 1] = dist[u - 1] + weight
        for i, v in enumerate(printV):
            print(dist[v - 1], end = "," if i != len(printV) - 1 else "")
G = Graph('DIjkstraData.txt')
# G = Graph('test1.txt')
# 7,37,59,82,99,115,133,165,188,197
# G.add_edge(1, 6, 20)
# print("dd", G.get_neighbours(1))
# G.print_graph()
G.dijkstra(0, [7,37,59,82,99,115,133,165,188,197])
# G.dijkstra(0, [6,7,8])

