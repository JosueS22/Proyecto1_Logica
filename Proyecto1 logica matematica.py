
# Se define la matriz de adyacencia del grafo 
graph = [[1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1]]

# El algoritmo de Warshall recibe como parametros la cantidad de vertices 
# y la matriz de adyacencia
def warshall_algorithm(v, graph):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j]= graph[i][j] or (graph[i][k] and graph[k][j])
    return graph

# La funciones de matrices booleanas recibe como parametros la cantidad
# de vertices, la matriz de adyacencia (dos veces) y una matriz inicial 
# que por default va a tener 0 en todas sus entradas
def boolean_matrix(v, graph1, graph2, initial_graph = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]):
    actual_graph = initial_graph
    for i in range(v):
        for j in range(v):
            for k in range(v):
                actual_graph[i][j] += graph1[i][k] *graph2[k][j]
                if actual_graph[i][j] > 1:
                    actual_graph[i][j] = 1
    if(actual_graph == graph1):
        return actual_graph
    else:
        boolean_matrix(v, actual_graph, graph1, actual_graph)

transitiveClosure_graph = warshall_algorithm(len(graph), graph)

print("\nCierre transitivo utilizando el algoritmo de Warshall: \n")
for i in transitiveClosure_graph:
    print(i)

transitiveClosure_graph = boolean_matrix(len(graph), graph, graph)

print("\nCierre transitivo utilizando matrices booleanas: \n")
for r in transitiveClosure_graph:
    print(r)