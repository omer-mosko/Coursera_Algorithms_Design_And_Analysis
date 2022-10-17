
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
    def dijkstra(self, src):
        visited = [False for _ in range(len|(1))]
        dist = [np.Inf for _ in range(n)]
        #while sum(visited) < self.V:
            #for v in
G = Graph('test1.txt')
G.add_edge(1, 6, 20)
print("dd", G.get_neighbours(1))
G.print_graph()