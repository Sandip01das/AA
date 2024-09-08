import heapq

def prim_mst(graph, num_vertices):
    mst = []
    visited = set()
    
    # Start from vertex 0 or any arbitrary vertex
    start_vertex = 0
    visited.add(start_vertex)
    
    # Create a priority queue and add all edges from the start vertex
    edges = [(weight, start_vertex, v) for v, weight in graph[start_vertex]]
    heapq.heapify(edges)
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        if v in visited:
            continue
        
        mst.append((u, v, weight))
        visited.add(v)
        
        for next_vertex, next_weight in graph[v]:
            if next_vertex not in visited:
                heapq.heappush(edges, (next_weight, v, next_vertex))
    
    return mst

def main():
    # User input for the number of vertices and edges
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    # Initialize the graph as an adjacency list
    graph = {i: [] for i in range(num_vertices)}
    
    # User input for edges
    print("Enter each edge in the format: u v weight")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # Since the graph is undirected
    
    # Run Prim's algorithm
    mst = prim_mst(graph, num_vertices)
    
    # Output the MST
    print("\nMinimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"Edge: ({u}, {v}), Weight: {weight}")

if __name__ == "__main__":
    main()
