from collections import deque

def bfs(G, s):
    colour = {}
    d = {}
    p = {}
    Q = deque()

    for u in G:
        if u != s:
            colour[u] = 'W'
            d[u] = float('inf')
            p[u] = None
        else:
            colour[u] = 'G'
            d[u] = 0
            p[u] = None
            Q.append(u)

    # BFS
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if colour[v] == 'W':
                colour[v] = 'G'
                d[v] = d[u] + 1
                p[v] = u
                Q.append(v)

        colour[u] = 'B'

    return d, p

def bfs_spanning_tree(G, s, parents):
    spanning_tree = {}
    for v, parent in parents.items():
        if parent is not None:
            if parent not in spanning_tree:
                spanning_tree[parent] = []
            spanning_tree[parent].append(v)
    return spanning_tree

# Get user input for the graph
def input_graph():
    G = {}
    num_vertices = int(input("Enter the number of vertices: "))
    for _ in range(num_vertices):
        vertex = input("Enter the vertex: ")
        edges = input(f"Enter the neighbors of {vertex} separated by spaces: ").split()
        G[vertex] = edges
    return G

# Get user input for the starting vertex
def input_start_vertex():
    return input("Enter the starting vertex: ")

# Main function to run BFS and display results
def main():
    G = input_graph()
    start_vertex = input_start_vertex()
    
    distances, parents = bfs(G, start_vertex)
    print("\nDistances from", start_vertex + ":", distances)
    print("Parents:", parents)

    spanning_tree_parents = bfs_spanning_tree(G, start_vertex, parents)
    print("\nBFS Spanning Tree:")
    for parent, children in spanning_tree_parents.items():
        for child in children:
            print(parent, "->", child)

if __name__ == "__main__":
    main()
