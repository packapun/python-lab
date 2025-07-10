from collections import defaultdict, deque

class Graph:
    def __init__(self, directed: bool):
        self._graph = defaultdict(list)
        self._directed = directed
    
    def add_connections(self, connections):
        """Add multiple connections from a list of (v1, v2, weight) tuples"""
        for v1, v2, weight in connections:
            self.add(v1, v2, weight)

    def add(self, v1, v2, weight):
        """Add an edge between v1 and v2 with given weight"""
        self._graph[v1].append((v2, weight))
        if not self._directed: 
            self._graph[v2].append((v1, weight))

    def show_graph(self):
        """Display the graph structure"""
        for vertex, connections in self._graph.items():
            print(f"{vertex}: {connections}")

    def remove_vertex(self, v):
        """Remove a vertex and all edges connected to it"""
        # Remove all edges pointing to vertex v
        for vertex in self._graph:
            # Use list comprehension to filter out connections to v
            self._graph[vertex] = [
                (neighbor, weight) for neighbor, weight in self._graph[vertex] 
                if neighbor != v
            ]
        
        # Remove the vertex itself
        if v in self._graph:
            del self._graph[v]
        else:
            print(f"Warning: Vertex {v} not found in graph")

    def remove_edge(self, v1, v2):
        """Remove a specific edge between v1 and v2"""
        if v1 in self._graph:
            self._graph[v1] = [
                (neighbor, weight) for neighbor, weight in self._graph[v1] 
                if neighbor != v2
            ]
        
        if not self._directed and v2 in self._graph:
            self._graph[v2] = [
                (neighbor, weight) for neighbor, weight in self._graph[v2] 
                if neighbor != v1
            ]

    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex"""
        return self._graph.get(vertex, [])

    def has_edge(self, v1, v2):
        """Check if there's an edge between v1 and v2"""
        return any(neighbor == v2 for neighbor, _ in self._graph.get(v1, []))

    def get_vertices(self):
        """Get all vertices in the graph"""
        vertices = set(self._graph.keys())
        for connections in self._graph.values():
            for neighbor, _ in connections:
                vertices.add(neighbor)
        return list(vertices)

    def is_empty(self):
        """Check if the graph is empty"""
        return len(self._graph) == 0

    def __str__(self):
        """String representation for debugging"""
        return f'{self.__class__.__name__}({dict(self._graph)})'

    def __repr__(self):
        """Detailed representation"""
        return f'{self.__class__.__name__}(directed={self._directed}, vertices={len(self.get_vertices())})'

    def dfs(self, start_vertex, target=None):
        """
        Depth-First Search traversal
        
        Args:
            start_vertex: Starting vertex for traversal
            target: Optional target vertex to find
            
        Returns:
            List of vertices in DFS order, or path to target if target is specified
        """
        if start_vertex not in self._graph and start_vertex not in self.get_vertices():
            return []
        
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            if vertex in visited:
                return False
            
            visited.add(vertex)
            result.append(vertex)
            
            # If we're looking for a target and found it, return True
            if target and vertex == target:
                return True
            
            # Visit all neighbors
            for neighbor, _ in self._graph.get(vertex, []):
                if dfs_recursive(neighbor):
                    return True
            
            return False
        
        dfs_recursive(start_vertex)
        return result

    def dfs_iterative(self, start_vertex, target=None):
        """
        Iterative implementation of DFS using a stack
        
        Args:
            start_vertex: Starting vertex for traversal
            target: Optional target vertex to find
            
        Returns:
            List of vertices in DFS order, or path to target if target is specified
        """
        if start_vertex not in self._graph and start_vertex not in self.get_vertices():
            return []
        
        visited = set()
        stack = [start_vertex]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # If we found the target, return the path
                if target and vertex == target:
                    return result
                
                # Add neighbors to stack (in reverse order to maintain left-to-right traversal)
                neighbors = [neighbor for neighbor, _ in self._graph.get(vertex, [])]
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result

    def bfs(self, start_vertex, target=None):
        """
        Breadth-First Search traversal
        
        Args:
            start_vertex: Starting vertex for traversal
            target: Optional target vertex to find
            
        Returns:
            List of vertices in BFS order, or path to target if target is specified
        """
        if start_vertex not in self._graph and start_vertex not in self.get_vertices():
            return []
        
        visited = set()
        queue = deque([start_vertex])
        result = []
        
        while queue:
            vertex = queue.popleft()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # If we found the target, return the path
                if target and vertex == target:
                    return result
                
                # Add neighbors to queue
                for neighbor, _ in self._graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result

    def shortest_path_bfs(self, start_vertex, target_vertex):
        """
        Find shortest path between two vertices using BFS
        
        Args:
            start_vertex: Starting vertex
            target_vertex: Target vertex
            
        Returns:
            List representing the shortest path, or empty list if no path exists
        """
        if start_vertex == target_vertex:
            return [start_vertex]
        
        if (start_vertex not in self._graph and start_vertex not in self.get_vertices()) or \
           (target_vertex not in self._graph and target_vertex not in self.get_vertices()):
            return []
        
        visited = set()
        queue = deque([(start_vertex, [start_vertex])])
        
        while queue:
            vertex, path = queue.popleft()
            
            if vertex in visited:
                continue
            
            visited.add(vertex)
            
            for neighbor, _ in self._graph.get(vertex, []):
                if neighbor == target_vertex:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        
        return []  # No path found

    def is_connected(self):
        """
        Check if the graph is connected (for undirected graphs)
        or weakly connected (for directed graphs)
        """
        vertices = self.get_vertices()
        if not vertices:
            return True
        
        # Start DFS from first vertex
        visited = set()
        self._dfs_connected(vertices[0], visited)
        
        # Check if all vertices were visited
        return len(visited) == len(vertices)
    
    def _dfs_connected(self, vertex, visited):
        """Helper method for connectivity check"""
        visited.add(vertex)
        for neighbor, _ in self._graph.get(vertex, []):
            if neighbor not in visited:
                self._dfs_connected(neighbor, visited)

    def has_cycle(self):
        """
        Detect if the graph has a cycle using DFS
        
        Returns:
            True if cycle exists, False otherwise
        """
        vertices = self.get_vertices()
        visited = set()
        
        for vertex in vertices:
            if vertex not in visited:
                if self._has_cycle_dfs(vertex, visited, None):
                    return True
        return False
    
    def _has_cycle_dfs(self, vertex, visited, parent):
        """Helper method for cycle detection"""
        visited.add(vertex)
        
        for neighbor, _ in self._graph.get(vertex, []):
            if neighbor not in visited:
                if self._has_cycle_dfs(neighbor, visited, vertex):
                    return True
            elif neighbor != parent:  # For undirected graphs
                return True
        
        return False

    def get_all_paths(self, start_vertex, target_vertex):
        """
        Find all paths between two vertices using DFS
        
        Args:
            start_vertex: Starting vertex
            target_vertex: Target vertex
            
        Returns:
            List of all paths (each path is a list of vertices)
        """
        if start_vertex == target_vertex:
            return [[start_vertex]]
        
        all_paths = []
        visited = set()
        
        def dfs_all_paths(vertex, path):
            if vertex == target_vertex:
                all_paths.append(path[:])
                return
            
            visited.add(vertex)
            
            for neighbor, _ in self._graph.get(vertex, []):
                if neighbor not in visited:
                    path.append(neighbor)
                    dfs_all_paths(neighbor, path)
                    path.pop()
            
            visited.remove(vertex)
        
        dfs_all_paths(start_vertex, [start_vertex])
        return all_paths


# Example usage
if __name__ == "__main__":
    # Create an undirected graph
    g = Graph(directed=False)
    
    # Add connections
    connections = [
        ('A', 'B', 5),
        ('A', 'C', 3),
        ('B', 'D', 2),
        ('C', 'D', 4),
        ('B', 'E', 1),
        ('D', 'F', 6)
    ]
    g.add_connections(connections)
    
    print("Graph structure:")
    g.show_graph()
    print(f"\nGraph representation: {g}")
    
    # Test DFS
    print(f"\nDFS from A: {g.dfs('A')}")
    print(f"DFS iterative from A: {g.dfs_iterative('A')}")
    print(f"DFS from A to F: {g.dfs('A', 'F')}")
    
    # Test BFS
    print(f"\nBFS from A: {g.bfs('A')}")
    print(f"BFS from A to F: {g.bfs('A', 'F')}")
    
    # Test shortest path
    print(f"\nShortest path from A to F: {g.shortest_path_bfs('A', 'F')}")
    
    # Test connectivity and cycles
    print(f"\nIs connected: {g.is_connected()}")
    print(f"Has cycle: {g.has_cycle()}")
    
    # Test all paths
    print(f"\nAll paths from A to D: {g.get_all_paths('A', 'D')}")
    
    # Test with directed graph
    print("\n" + "="*50)
    print("Testing with directed graph:")
    
    dg = Graph(directed=True)
    directed_connections = [
        ('A', 'B', 1),
        ('B', 'C', 2),
        ('C', 'D', 3),
        ('A', 'C', 4),
        ('B', 'D', 5)
    ]
    dg.add_connections(directed_connections)
    
    print("Directed graph structure:")
    dg.show_graph()
    
    print(f"\nDFS from A: {dg.dfs('A')}")
    print(f"BFS from A: {dg.bfs('A')}")
    print(f"Shortest path A to D: {dg.shortest_path_bfs('A', 'D')}")
    print(f"All paths A to D: {dg.get_all_paths('A', 'D')}")