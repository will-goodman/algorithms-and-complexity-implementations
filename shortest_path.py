import numpy as np
import math
import sys


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


def bellman_ford(graph, start_vertex):
    """
    Performs the Bellman-Ford algorithm to find the shortest distance between one vertex and all other vertices in a
    graph

    :param graph: Dictionary representing the graph. Each vertex is a key and its value is a list of tuples representing
                  each edge from that vertex. E.g. {'u': [('v', 3), ('x', 1)]} means that vertex u has an edge of length
                  3 to vertex v, and also an edge of length 1 to vertex x.
    :param start_vertex: The start vertex to calculate all distances from
    :return: A dictionary where each vertex is a key and its shortest distance from the start vertex is its value
    """
    edges = _convert_graph_to_edges(graph)
    shortest_distances = []
    for i in range(len(graph)):
        if i == 0:
            y_axis = dict.fromkeys(graph.keys(), sys.maxsize)  # math.inf does not allow addition/subtraction
            y_axis.update({start_vertex: 0})  # the distance from the start vertex to itself will always be zero
            shortest_distances.append(y_axis)
        else:
            shortest_distances.append(dict.fromkeys(graph.keys()))

    for i in range(1, len(graph)):
        for vertex in graph.keys():
            connecting_edges = sorted([edge for edge in edges if edge[1] == vertex], key=lambda x: x[2])
            if len(connecting_edges) > 0:
                shortest_distances[i][vertex] = min(shortest_distances[i - 1][vertex], connecting_edges[0][2] +
                                                    shortest_distances[i - 1][connecting_edges[0][0]])
            else:
                shortest_distances[i][vertex] = shortest_distances[i - 1][vertex]

    return shortest_distances[len(graph) - 1]


def _convert_graph_to_edges(graph):
    """
    Converts a dictionary representing a graph into a list of tuples representing edges

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

    return edges


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

graph = {
    's': [('u', 1), ('x', -4), ('v', 2)],
    'u': [('v', 3), ('x', 1)],
    'x': [('y', -2), ('z', 2)],
    'y': [],
    'v': [('x', 2), ('z', -3)],
    'z': []
}
distances = bellman_ford(graph, start_vertex)
# Expected: {'s': 0, 'u': 1, 'x': -4, 'y': -6, 'v': 2, 'z': -1}
print(distances)
