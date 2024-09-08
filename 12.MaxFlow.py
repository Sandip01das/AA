from collections import deque

class Graph:
    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, graph, s, t, parent):
        ROW = len(graph)
        visited = [False] * ROW
        queue = deque()

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.popleft()

            for ind, val in enumerate(graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

    # Applying Ford-Fulkerson algorithm
    def ford_fulkerson(self, graph, source, sink):
        ROW = len(graph)
        parent = [-1] * ROW
        max_flow = 0

        while self.searching_algo_BFS(graph, source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while v != source:
                u = parent[v]
                graph[u][v] -= path_flow
                graph[v][u] += path_flow
                v = parent[v]

        return max_flow

def take_input():
    nodes = int(input("Enter the number of nodes: "))
    graph = []

    print("Enter the adjacency matrix (row by row):")
    for i in range(nodes):
        row = list(map(int, input().split()))
        graph.append(row)

    source = int(input("Enter the source node: "))
    sink = int(input("Enter the sink node: "))

    return graph, source, sink

def main():
    graph, source, sink = take_input()
    g = Graph()
    print("Max Flow: %d" % g.ford_fulkerson(graph, source, sink))

if __name__ == "__main__":
    main()