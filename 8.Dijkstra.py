from collections import defaultdict

def dijkstra(graph, weights, start, V):
    S = set()
    d = {v: float('inf') for v in range(V)}
    d[start] = 0

    while len(S) != V:
        # Choose the node y not in S with the smallest distance d[y]
        y = None
        for v in range(V):
            if v not in S:
                if y is None or d[v] < d[y]:
                    y = v

        if y is None:
            break

        S.add(y)

        # Update distances
        for v in graph[y]:
            if v not in S:
                d[v] = min(d[v], d[y] + weights[(y, v)])

    return d

# Add edge to the graph
def add_edge(graph, weights, u, v, weight):
    graph[u].append(v)
    weights[(u, v)] = weight
    # If the graph is undirected, add the reverse edge as well
    graph[v].append(u)
    weights[(v, u)] = weight

# Example usage
def main():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    
    graph = defaultdict(list)
    weights = {}
    
    print("Enter the edges (u, v) and weights:")
    for _ in range(E):
        u, v, weight = map(int, input().split())
        add_edge(graph, weights, u, v, weight)
    
    start_node = int(input("Enter the start node: "))
    distances = dijkstra(graph, weights, start_node, V)
    
    print(f"Distances from node {start_node}:")
    for node in range(V):
        print(f"Distance to node {node}: {distances[node]}")

if __name__ == "__main__":
    main()