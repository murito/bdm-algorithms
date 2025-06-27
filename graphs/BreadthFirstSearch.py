from collections import deque
from simple_connected_graph import SimpleGraph
#from unconnected_graph import UnconnectedGraph

def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Initialize the queue with the start node
    visited.add(start_node)  # Mark the start node as visited
    traversal_order = []  # To store the order of visited nodes

    while queue:
        current_node = queue.popleft()  # Dequeue the first node
        traversal_order.append(current_node)  # Add to traversal order

        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

if __name__ == '__main__':
    #simple_graph = SimpleGraph()
    #unconnected_graph = UnconnectedGraph()

    #print(bfs(simple_graph.get_adjacent_list(), 4));
    lista = {
        'a': ['b','d','h','e'],
        'b': ['a', 'd', 'c', 'g'],
        'c': ['b', 'f', 'g'],
        'd': ['a', 'b'],
        'e': ['a', 'j'],
        'f': ['c', 'h', 'i', 'j'],
        'g': ['b', 'c', 'j'],
        'h': ['a', 'i', 'f'],
        'i': ['h', 'f'],
        'j': ['e', 'f', 'g']
    }

    print(bfs(lista, 'e'))