"""
Jun 15, 2025
Francisco Javier Alcalá Olivares
--------------------------------------
Depth-first Search
"""
from unconnected_graph import UnconnectedGraph
from Graph import Graph

def depth_first_search(graph_in, node):
    # Set the current node as visited
    graph_in.set_node_visited(node)

    # Go through each neighbor for this node
    for neighbor in graph_in.get_adj_list()[node]:
        # validate if the current neighbor has not been visited
        if neighbor not in graph_in.get_visited():
            # I want to track vertices, so I have added a vertex feeder here
            graph_in.add_vertex(node, neighbor)
            # Our recurrent call for the current neighbor
            depth_first_search(graph_in, neighbor)

if __name__ == '__main__':
    # Build an unconnected graph
    unconnected_graph = UnconnectedGraph()

    # Get the adjacency list
    adjacent_list = unconnected_graph.get_adjacent_list()

    # Build a custom graph from an adjacency list
    graph = Graph(adjacent_list)

    # Execute the Depth First Search from some node
    depth_first_search(graph, 0)

    # Print connected nodes
    print(graph.visited)
    # Print vertices
    print(graph.vertices)
