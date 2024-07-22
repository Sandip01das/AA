from collections import defaultdict

# Add edge to the graph
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# DFS algorithm
def dfs(graph, V):
    color = ['W'] * V
    parent = [None] * V
    pre = [None] * V
    post = [None] * V
    time = [0]  # Use a list to modify within dfs_visit

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

    for u in range(V):
        if color[u] == 'W':
            dfs_visit(u)

    return pre, post, parent

def print_dfs_spanning_tree(parent):
    print("DFS Spanning Tree:")
    for v in range(len(parent)):
        if parent[v] is not None:
            print(f"Edge: {parent[v]} -> {v}")

# Example usage
V = 5
graph = defaultdict(list)
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 2, 0)
add_edge(graph, 2, 3)
add_edge(graph, 3, 3)

pre, post, parent = dfs(graph, V)
print("Pre times:", pre)
print("Post times:", post)
print("Parents:", parent)

print_dfs_spanning_tree(parent)
