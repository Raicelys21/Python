class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def isIsomorphic(self, g1, g2):
        if self.isSubgraphIsomorphic(g1, g2):
            return True
        if self.isSubgraphIsomorphic(g2, g1):
            return True
        return False

    def isSubgraphIsomorphic(self, g1, g2):
        if g1.V != g2.V:
            return False
        if g1.graph == g2.graph:
            return True
        for i in range(g1.V):
            for j in range(g1.V):
                if g1.graph[i][j] != g2.graph[i][j]:
                    return False
        return True

graph1 = Graph(5);
graph2 = Graph(5);

graph1.graph = [[0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]]

graph2.graph = [[0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]]

print(graph1.isIsomorphic(graph1, graph2))