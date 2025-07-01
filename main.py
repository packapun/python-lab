from collections import defaultdict 
from stack import Stack

class Graph(object):
    def __init__(self, directed=False):
        self._graph = defaultdict(list)
        self._directed = directed


    def addConnections(self, connections):
        for v1,v2,weight in connections:
            self.add(v1,v2,weight)

    def add(self, v1,v2,weight):
        self._graph[v1].append((v2,weight))
        if not self._directed:
            self._graph[v2].append((v1,weight))

    def showGraph(self):
        for item in self._graph.items():
            print(item)


    def performDFS(self):
        """Perform basic DFS search"""
        s = Stack() 
        op = []
        s.push('A')
        self._dfs(s,op)

    def _dfs(self, S:Stack, op):
        if not S:
            return 
        current = S.peek()
        for v in self._graph[current]:
            if v[0] not in op and v[0] not in S._items:
                S.push(v[0])
                self._dfs(S,op)
        e = S.pop()
        print(e, end=" => ")
        op.append(e)

    

def testGraph():
    graph_connections = [('A', 'B', 4), ('A', 'C', 1), ('A', 'E', 5), ('B', 'A', 4), ('B', 'D', 1),
                         ('C', 'A', 1), ('C', 'D', 1), ('C', 'F', 2), ('D', 'B', 1), ('D', 'C', 1),
                         ('E', 'A', 4), ('E', 'F', 1), ('F', 'C', 2), ('F', 'E', 1)]
    g = Graph(True)
    g.addConnections(graph_connections)
    g.showGraph()
    g.performDFS()

testGraph()