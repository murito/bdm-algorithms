"""
Jun 15, 2025
Francisco Javier Alcalá Olivares
--------------------------------------
Graph object
"""
class Graph:
    # Initialize memory slots
    visited = []
    vertices = []

    # construct the object with the Adjacent list provided
    def __init__(self, adj_list_in):
        self.adj_list = adj_list_in

    # return the visited nodes
    def get_visited(self):
        return self.visited

    # return the adjacency list
    def get_adj_list(self):
        return self.adj_list

    # Add a new vertex
    def add_vertex(self, node1, node2):
        self.vertices.append((node1, node2))

    # Mark a node as visited
    def set_node_visited(self, node):
        self.visited.append(node)