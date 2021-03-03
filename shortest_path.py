

def dijkstra(graph, start_vertex):
    """
    Performs the Dijkstra algorithm to find the shortest distance between one vertex and all other vertices in a graph.

    :param graph: Dictionary representing the graph. Each vertex is a key and its value is a list of tuples representing
                  each edge from that vertex. E.g. {'u': [('v', 3), ('x', 1)]} means that vertex u has an edge of length
                  3 to vertex v, and also an edge of length 1 to vertex x.
    :param start_vertex: The start vertex to calculate all distances from
    :return: A dictionary where each vertex is a key and its shortest distance from the start vertex is its value
    """
    graph_vertices = set(graph.keys())

    explored_vertices = {start_vertex}
    distances = {start_vertex: 0}
    while graph_vertices != explored_vertices:

        temp_distances = {}
        for vertex in explored_vertices:
            for dest_vertex, distance in graph.get(vertex):
                if dest_vertex not in explored_vertices:
                    temp_distances.update({distances.get(vertex) + distance: dest_vertex})

        min_temp_distance = min(temp_distances.keys())
        next_vertex = temp_distances.get(min_temp_distance)
        explored_vertices.add(next_vertex)
        distances.update({next_vertex: min_temp_distance})

    return distances


graph = {
    's': [('u', 1), ('x', 4), ('v', 2)],
    'u': [('v', 3), ('x', 1)],
    'x': [('y', 2), ('z', 2)],
    'y': [],
    'v': [('x', 2), ('z', 3)],
    'z': []
}
start_vertex = 's'

distances = dijkstra(graph, start_vertex)

# Expected: {'s': 0, 'u': 1, 'v': 2, 'x': 2, 'z': 4, 'y': 4}
print(distances)
