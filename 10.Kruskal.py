class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []  # This will store the resultant MST
        i, e = 0, 0  # `i` is used for sorted edges, `e` is used for result[]
        total_weight = 0  # Variable to store total weight of the MST

        # Step 1: Sort all the edges in non-decreasing order of their weight.
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If not, include it. Otherwise, discard it.
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does not cause a cycle, include it in the result and increment the index of result for the next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
                total_weight += w  # Add weight to the total

        # Print the contents of the result[] to display the built MST
        print("\nEdges in the constructed Minimum Spanning Tree:")
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")

        # Print the total weight of the MST
        print(f"\nTotal weight of the Minimum Spanning Tree: {total_weight}")

# Function to get user input for the graph
def input_graph():
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    graph = Graph(num_vertices)
    print("Enter each edge in the format 'vertex1 vertex2 weight':")
    for _ in range(num_edges):
        u, v, w = map(int, input().split())
        graph.add_edge(u, v, w)
    return graph

def main():
    graph = input_graph()
    graph.kruskal_algo()

if __name__ == "__main__":
    main()
