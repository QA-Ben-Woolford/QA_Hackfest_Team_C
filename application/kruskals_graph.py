from random import randint 
from itertools import combinations

class WeightedGraph():

    def __init__(self, addresses, mst = False):
        self.addresses = {i:address for i, address in enumerate(addresses)}
        self.nodes = []

        for i in self.addresses.keys():
            self.nodes.append(i)
        
        if mst:
            self.edges = []
        else:
            self.edges = [(p[0], p[1], randint(1,100)) for p in combinations(self.nodes, 2)]


    def get_edges(self):
        return self.edges

    def get_nodes(self):
        return self.nodes
        
    def add_node(self, node):
        self.nodes.append(node)
    
    def add_edge(self, node1, node2, weight):
        self.edges.append((node1,node2,weight))

# union-find implementation - these are the functions used to implement the union-find method within the Kruskals algo
    def find(self, root, i):
        if root[i] == i:
            return i
        return self.find(root, root[i])
    
    def union(self, root, rank, x, y):
        xroot = self.find(root, x)
        yroot = self.find(root, y)
        if rank[xroot] < rank[yroot]:
            root[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            root[yroot] = xroot
        else:
            root[yroot] = xroot
            rank[xroot] += 1

    # Kruskals implementation example. Note that you will need to adapt this based on your implementation of graphs, if you plan to use this:
    def kruskals(self):
        mst = WeightedGraph(self.addresses, True)
        edges = self.get_edges()
        edges.sort(key = lambda t: t[2])
        root, rank = self.get_nodes(), [0 for _ in self.get_nodes()]
        for node1, node2, weight in edges:
            x = self.find(root, node1)
            y = self.find(root, node2)
            if x != y:
                mst.add_node(node1)
                mst.add_node(node2)
                mst.add_edge(node1, node2, weight)
                self.union(root, rank, x, y)
        return mst