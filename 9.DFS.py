from collections import defaultdict

# Add edge to the graph
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# DFS algorithm
def dfs(graph, V):
    color = {vertex: 'W' for vertex in graph}  # Using a dictionary for consistency
    parent = {vertex: None for vertex in graph}
    pre = {vertex: None for vertex in graph}
    post = {vertex: None for vertex in graph}
    time = [0]  # Use a list to modify time within dfs_visit

    def dfs_visit(u):
        color[u] = 'G'
        time[0] += 1
        pre[u] = time[0]
        for v in graph[u]:
            if color[v] == 'W':
                parent[v] = u
                dfs_visit(v)
        color[u] = 'B'
        time[0] += 1
        post[u] = time[0]

    for u in graph:
        if color[u] == 'W':
            dfs_visit(u)

    return pre, post, parent

def print_dfs_spanning_tree(parent):
    print("DFS Spanning Tree:")
    for child, par in parent.items():
        if par is not None:
            print(f"{par} -> {child}")

# Get user input for the graph
def input_graph():
    graph = defaultdict(list)
    num_vertices = int(input("Enter the number of vertices: "))
    print("Enter the edges in the format 'vertex1 vertex2':")
    for _ in range(num_vertices):
        vertex = input("Enter the vertex: ")
        edges = input(f"Enter the neighbors of {vertex} separated by spaces: ").split()
        for edge in edges:
            add_edge(graph, vertex, edge)
    return graph

# Get user input for the starting vertex
def input_start_vertex():
    return input("Enter the starting vertex: ")

# Main function to run DFS and display results
def main():
    graph = input_graph()
    start_vertex = input_start_vertex()

    pre, post, parent = dfs(graph, len(graph))
    print("\nPre times:", pre)
    print("Post times:", post)
    print("Parents:", parent)

    print("\nDFS Spanning Tree:")
    print_dfs_spanning_tree(parent)

if __name__ == "__main__":
    main()
