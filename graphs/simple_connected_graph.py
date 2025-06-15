"""
Jun 15, 2025
Francisco Javier Alcalá Olivares
--------------------------------------
SimpleGraph for testing
"""
class SimpleGraph:
    nodes = range(1,10) # 9 nodes from 1 to 9
    edges = [(1,2),(1,4),(1,6),(1,7),(2,1),(2,3),(2,8),(3,2),(3,8),(4,1),(4,5),(5,4),(5,6),(6,1),(6,5),(6,7),(7,1),(7,6),(7,9),(8,2),(8,3),(8,9),(9,7),(9,8)]
    adjacent_list = {}

    def __init__(self):
        # Create an array's dict
        for node in self.nodes:
            self.adjacent_list[node] = []

        # Feed the dict
        for edge in self.edges:
            self.adjacent_list[edge[0]].append(edge[1])
            self.adjacent_list[edge[1]].append(edge[0])

    def get_edges(self):
        return self.edges

    def get_adjacent_list(self):
        return self.adjacent_list
