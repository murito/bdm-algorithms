import heapq

def dijkstra(graph, start, end):
    # Inicializar distancias y predecesores
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {}
    visited = set()

    # Usamos una priority queue (min-heap)
    heap = [(0, start)]  # (distancia, nodo)

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)

        # Si llegamos al destino, podemos romper
        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    # Reconstruir el camino
    path = []
    node = end
    if node not in predecessors and node != start:
        return float('inf'), []  # No hay camino

    while node != start:
        path.append(node)
        node = predecessors[node]
    path.append(start)
    path.reverse()

    return distances[end], path

if __name__ == '__main__':
    # Example usage:
    graph = {
         'a': {'d': 5, 'e': 7, 'b': 3, 'h': 5},
         'b': {'a': 3, 'd': 2, 'g': 4, 'c': 5},
         'c': {'g': 8, 'b': 5, 'f': 6},
         'd': {'b': 2, 'a': 5},
         'e': {'a': 7, 'j': 7},
         'f': {'i': 8, 'h': 9, 'c': 6, 'j': 7},
         'g': {'c': 8, 'b': 4, 'j': 4},
         'h': {'a': 5, 'i': 3, 'f': 9},
         'i': {'h': 3, 'f': 8 },
         'j': {'e': 7, 'g': 4, 'f': 7}
    }

    dist, path = dijkstra(graph, 'd', 'i')
    print(f"Distancia más corta: {dist}")
    print(f"Ruta: {' → '.join(path)}")