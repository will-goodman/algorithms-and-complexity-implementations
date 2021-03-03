
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


def kruskal(graph):
    """
    Performs Kruskal's algorithm on a weighted graph to find the Minimum Spanning Tree

    :param graph: Dictionary representing the graph. Each vertex is a key and its value is a list of tuples representing
                  each edge from that vertex. E.g. {'u': [('v', 3), ('x', 1)]} means that vertex u has an edge of length
                  3 to vertex v, and also an edge of length 1 to vertex x.
    :return: A list of tuples where each tuple is an edge in the MST e.g. ('u', 'v', 3) represents the edge between u
             and v with weight 3
    """
    edges = []
    for vertex, vertex_edges in graph.items():
        for vertex_edge in vertex_edges:
            if (vertex_edge[0], vertex, vertex_edge[1]) not in edges:
                edges.append((vertex, vertex_edge[0], vertex_edge[1]))

    sorted_edges = sorted(edges, key=lambda x: x[2])

    covered_vertices = []
    mst_edges = []
    i = 0
    while i < len(sorted_edges):
        current_edge = sorted_edges[i]
        first_vertex = current_edge[0]
        second_vertex = current_edge[1]
        if not _cycle_present(_convert_edges_to_graph(mst_edges + [current_edge])):
            mst_edges.append(current_edge)
            covered_vertices += [first_vertex, second_vertex]
        i += 1

    return mst_edges


def _convert_edges_to_graph(edges):
    """
    Converts a list of tuples representing edges into a dictionary representing the whole graph

    :param edges: A list of tuples where each tuple is an edge in the MST e.g. ('u', 'v', 3) represents the edge between u
                  and v with weight 3
    :return: Dictionary representing the graph. Each vertex is a key and its value is a list of tuples representing
             each edge from that vertex. E.g. {'u': [('v', 3), ('x', 1)]} means that vertex u has an edge of length
             3 to vertex v, and also an edge of length 1 to vertex x.
    """
    graph = {}
    for edge in edges:
        first_vertex = edge[0]
        second_vertex = edge[1]
        weight = edge[2]
        if first_vertex in graph.keys():
            graph.get(first_vertex).append((second_vertex, weight))
        else:
            graph.update({first_vertex: [(second_vertex, weight)]})

        if second_vertex in graph.keys():
            graph.get(second_vertex).append((first_vertex, weight))
        else:
            graph.update({second_vertex: [(first_vertex, weight)]})

    return graph


def _cycle_present(graph, current_vertex=None, previous_vertex=None, already_visited_vertices=None):
    """
    Checks if a given graph contains a cycle by recursively following each possible path from each vertex. If the same
    vertex is seen twice on a given path, then that path must contain a cycle, and hence a cycle is present within the
    graph.

    :param graph: The graph to check
    The below parameters start as None and are only set on recursive calls:
    :param current_vertex: Current vertex we are on within the graph
    :param previous_vertex: Previous vertex we just visited (do not want to go backwards on the path)
    :param already_visited_vertices: List of vertices we have already visited on the current path
    :return: Whether or not the given graph contains a cycle
    """
    if len(graph) == 0:
        return False

    if already_visited_vertices is None:
        already_visited_vertices = []
    if current_vertex is None:
        cycle_present = False
        for vertex in graph.keys():
            cycle_present = cycle_present or _cycle_present(graph, vertex)
        return cycle_present
    else:
        if current_vertex in already_visited_vertices:
            return True
        elif len(graph.get(current_vertex)) == 0:
            return False
        else:
            already_visited_vertices.append(current_vertex)

            cycle_present = False
            for edge in graph.get(current_vertex):
                if edge[0] != previous_vertex:
                    cycle_present = cycle_present or _cycle_present(graph, edge[0], current_vertex,
                                                                     already_visited_vertices)
            return cycle_present


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

mst = kruskal(graph)
# Expected (specific order): [('x', 'y', 1), ('c', 'd', 2), ('y', 'z', 3), ('x', 'a', 4), ('z', 'd', 5), ('x', 'b', 6)]
print(mst)
