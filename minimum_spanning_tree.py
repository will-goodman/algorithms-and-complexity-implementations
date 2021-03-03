

def prim(graph):
    """
    Performs Prim's algorithm on a weighted graph to find the Minimum Spanning Tree

    :param graph: Dictionary representing the graph. Each vertex is a key and its value is a list of tuples representing
                  each edge from that vertex. E.g. {'u': [('v', 3), ('x', 1)]} means that vertex u has an edge of length
                  3 to vertex v, and also an edge of length 1 to vertex x.
    :return: A list of tuples where each tuple is an edge in the MST e.g. ('u', 'v', 3) represents the edge between u
             and v with weight 3
    """
    graph_vertices = set(graph.keys())
    explored_vertices = {list(graph_vertices)[0]}

    edges = []
    while explored_vertices != graph_vertices:

        costs = {}
        for vertex in explored_vertices:
            for dest_vertex, weight in graph.get(vertex):

                if dest_vertex not in explored_vertices:
                    costs.update({weight: (vertex, dest_vertex, weight)})

        min_cost = min(costs.keys())
        next_edge = costs.get(min_cost)
        edges.append(next_edge)
        explored_vertices.add(next_edge[1])

    return edges


graph = {
    'x': [('y', 1), ('a', 4), ('b', 6)],
    'y': [('x', 1), ('z', 3)],
    'a': [('x', 4), ('z', 10), ('b', 20)],
    'b': [('x', 6), ('a', 20), ('c', 9)],
    'z': [('y', 3), ('a', 10), ('d', 5)],
    'c': [('b', 9), ('d', 2)],
    'd': [('c', 2), ('z', 5)]
}

mst = prim(graph)
# Expected (in any order): [('c', 'd', 2), ('d', 'z', 5), ('z', 'y', 3), ('y', 'x', 1), ('x', 'a', 4), ('x', 'b', 6)]
print(mst)

