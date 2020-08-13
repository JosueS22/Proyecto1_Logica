# Integrantes:
# Josue Sagastume 18173
# Mario Perdomo 18029
# Juan Diego Solorzano 18151

# Universidad del Valle de Guatemala
# Logica Matematica
# Proyecto 1
# Cierres Transitivos de un grafo

# Se define la matriz de adyacencia del grafo 

graph = [[0, 0, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]]

print("\nMatriz de adyacencia del grafo")
for i in graph:
    print(i)

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
    current_graph = initial_graph
    for i in range(v):
        for j in range(v):
            for k in range(v):
                current_graph[i][j] += graph1[i][k] *graph2[k][j]
                if current_graph[i][j] > 1:
                    current_graph[i][j] = 1
    if(current_graph == graph1):
        return current_graph
    else:
        boolean_matrix(v, current_graph, graph1, current_graph)

transitiveClosure_graph = warshall_algorithm(len(graph), graph)
print("\nCierre transitivo utilizando el algoritmo de Warshall:")
for i in transitiveClosure_graph:
    print(i)

transitiveClosure_graph2 = boolean_matrix(len(graph), graph, graph)
print("\nCierre transitivo utilizando matrices booleanas:")
for r in transitiveClosure_graph2:
    print(r)

# Referencias
# https://www.tutorialspoint.com/Transitive-closure-of-a-Graph#:~:text=Transitive%20Closure%20it%20the%20reachability,matrix%20is%20the%20Boolean%20type.
# http://repositori.uji.es/xmlui/bitstream/handle/10234/119829/tema11.pdf?sequence=1