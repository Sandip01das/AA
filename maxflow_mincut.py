from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)
    
    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # Ensure there is a reverse edge with 0 capacity initially

    def bfs(self, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)
        
        while queue:
            u = queue.popleft()
            
            for v in self.graph[u]:
                if v not in visited and self.graph[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
        return False

    def ford_fulkerson(self, source, sink):
        parent = {}
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow
        
        return max_flow

def main():
    g = Graph()
    
    # Input the number of vertices and edges
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    
    print("Enter the edges (u, v) and weights:")
    for _ in range(E):
        u, v, capacity = map(int, input().split())
        g.add_edge(u, v, capacity)
    
    source = int(input("Enter the source node: "))
    sink = int(input("Enter the sink node: "))
    
    max_flow = g.ford_fulkerson(source, sink)
    
    print(f"Maximum Flow from node {source} to node {sink}: {max_flow}")

if __name__ == "__main__":
    main()
