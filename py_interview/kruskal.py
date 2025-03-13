class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph):
    # graph is given as a list of (weight, start, end) tuples
    graph.sort()
    ds = DisjointSet([u for w, u, v in graph] + [v for w, u, v in graph])
    mst = []

    for edge in graph:
        weight, u, v = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append(edge)

    return mst

graph = [(3, 1, 2), (4, 1, 3), (1, 2, 3)]
print(kruskal(graph))
