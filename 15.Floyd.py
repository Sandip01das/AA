def floyd_warshall(graph):
    V = len(graph)
    INF = float('inf')
    
    # Initialize distance and predecessor matrices
    dist = [[INF] * V for _ in range(V)]
    pred = [[None] * V for _ in range(V)]
    
    # Initialize the distance and predecessor matrices based on the input graph
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != INF:
                dist[i][j] = graph[i][j]
                pred[i][j] = i
    
    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    
    return dist, pred

def get_path(pred, u, v):
    if pred[u][v] is None:
        return []  # No path exists
    path = []
    while v is not None:
        path.insert(0, v)
        v = pred[u][v]
    return path

def main():
    # Get user input for the graph
    INF = float('inf')
    
    V = int(input("Enter the number of vertices: "))
    print("Enter the adjacency matrix (use 'INF' for infinity):")
    
    graph = []
    for i in range(V):
        row = input().strip().split()
        graph_row = []
        for val in row:
            if val.upper() == 'INF':
                graph_row.append(INF)
            else:
                graph_row.append(int(val))
        graph.append(graph_row)

    dist, pred = floyd_warshall(graph)

    print("\nDistance Matrix:")
    for row in dist:
        print(row)

    print("\nPredecessor Matrix:")
    for row in pred:
        print(row)

    # Print all pairs shortest paths
    print("\nAll Pairs Shortest Paths:")
    for u in range(V):
        for v in range(V):
            if u != v:
                path = get_path(pred, u, v)
                if path:
                    path_str = " -> ".join(map(str, path))
                    print(f"Shortest path from {u} to {v}: {path_str}, Distance: {dist[u][v]}")
                else:
                    print(f"No path exists from {u} to {v}")

if __name__ == "__main__":
    main()
