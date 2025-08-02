from collections import deque, defaultdict
from typing import List, Dict, Set, Optional 

class Graph:
    def __init__(self, directed:bool = False):
        """
        Initialize graph with adjacency list representation
        Args:
            directed: True for directed graph, False for undirected
        """
        self.adj_list = defaultdict(list)
        self.directed = directed 

    def addEdge(self,u,v):
        self.adj_list[u].append(v)
        if self.directed:
            self.adj_list[v].append(u) 

    def addVertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def getVertices(self) -> List:
        return list(self.adj_list.keys())

    def getNeighbours(self, vertex) -> List:
        return self.adj_list[vertex]

    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")

    def bfs(self, start_vertex) -> List:
        bfs_order = []
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        
        while queue:
            current = queue.popleft()
            bfs_order.append(current)
            for n in self.getNeighbours(current):
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return bfs_order

    def dfs(self, start_vertex):
        if start_vertex not in self.adj_list:
            return []
        
        visited = set()
        order = []

        def dfs_helper(start_vertex):
            visited.add(start_vertex)
            for n in self.getNeighbours(start_vertex):
                if n not in visited:
                    dfs_helper(n)
            order.append(start_vertex)
        
        dfs_helper(start_vertex)
        return order 

    
# Create an undirected graph
print("=== Undirected Graph Example ===")
g = Graph(directed=False)

# Add edges
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
for u, v in edges:
    g.addEdge(u, v)

print("Graph adjacency list:")
g.display()

print(f"\nBFS traversal starting from vertex 0: {g.bfs(0)}")
print(f"\DFS traversal starting from vertex 0: {g.dfs(0)}")



