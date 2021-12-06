# Clase del grafo
class Graph:
 
    # Constructor
    def __init__(self, edges, N):
 
        # Lista de lista para representar la adyacencia
        self.adj_list = [[] for _ in range(N)]
 
        # Almacena el grado del vertice
        self.degree = [0] * N
 
        # add edges to the undirected graph
        for (start, end) in edges:
 
            # Se agrega un vetice desde su inicio hasta su destino
            self.adj_list[start].append(end)
 
            # Cada vez que se agrega, se incrementa el grado del vertice
            self.degree[end] = self.degree[end] + 1
 
# Función para encontrar todos los ordenamentos topológicos
def all_topological_orders(graph, path, visited, n):
 
    # Se itera por cada vertice
    for v in range(n):

        # Si el nodo no ha sido visitado se hace lo siguiente...
        if graph.degree[v] == 0 and not visited[v]:
 
            # Para cada vertice se reduce el grado en 1
            for u in graph.adj_list[v]:
                graph.degree[u] = graph.degree[u] - 1

            # Se agrega el vertice a la ruta
            path.append(v)
            visited[v] = True
 
            # Se aplica la recursión para seguir con el siguiente nodo...
            all_topological_orders(graph, path, visited, n)
 
            # Se limpia la información de la visita pasada
            for u in graph.adj_list[v]:
                graph.degree[u] = graph.degree[u] + 1
 
            # Se remueve el vertice de la ruta pasada
            path.pop()
            visited[v] = False
 
    # Una vez finaliza el recorrido se imprime el path
    if len(path) == n:
        print(path)
 
def print_topological_orders(graph):
    n = len(graph.adj_list)
    visited = [False] * n
    path = []
    all_topological_orders(graph, path, visited, n)
 
# Probar el código
if __name__ == "__main__":

    # Número de vetices y aristas
    n = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
 
    print("Posibles ordenamientos:")
 
    graph = Graph(edges, n)
    print_topological_orders(graph)