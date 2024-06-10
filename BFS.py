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


G = {
    '1': ['2', '3'],
    '2': ['4', '5', '1'],
    '3': ['6', '7', '1'],
    '4': ['8', '2'],
    '5': ['2', '8'],
    '6': ['8', '3'],
    '7': ['8','3'],
    '8': ['4','5','6','7']
}

start_vertex = '1'
distances, parents = bfs(G, start_vertex)
print("Distances from", start_vertex + ":", distances)
print("Parents:", parents)


def bfs_spanning_tree(G, s, parents):
    spanning_tree = {}
    for v, parent in parents.items():
        if parent is not None:
            if parent not in spanning_tree:
                spanning_tree[parent] = []
            spanning_tree[parent].append(v)
    return spanning_tree

spanning_tree_parents = bfs_spanning_tree(G, start_vertex, parents)
print("BFS Spanning Tree:")
for parent, children in spanning_tree_parents.items():
    for child in children:
        print(parent, "->", child)
