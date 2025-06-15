import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Provided adjacency list
    adjacency_list = {
        0: [29, 46, 21, 14, 38, 31],
        1: [41, 31, 21, 17],
        2: [9, 26, 5, 25, 4],
        3: [18, 30, 47],
        4: [28, 9, 8, 2],
        5: [44, 12, 2],
        6: [37, 10],
        7: [23, 22, 39],
        8: [4],
        9: [2, 4, 19, 28, 27],
        10: [6],
        11: [33],
        12: [5],
        13: [25, 38, 29],
        14: [0, 26, 28, 39],
        15: [22, 31, 19, 41],
        16: [46, 26, 38, 27],
        17: [1, 40, 29],
        18: [3, 45, 42, 35, 33, 47],
        19: [9, 15],
        20: [36, 49, 42],
        21: [0, 1],
        22: [7, 15, 26, 34],
        23: [7, 31, 32, 40],
        24: [31, 44],
        25: [2, 13, 38],
        26: [2, 14, 16, 22, 31],
        27: [9, 16, 32],
        28: [4, 9, 14],
        29: [0, 13, 17, 41, 48],
        30: [3, 47, 37],
        31: [0, 1, 15, 23, 24, 26],
        32: [23, 27],
        33: [11, 18, 36, 49],
        34: [22, 48],
        35: [18, 45],
        36: [20, 33, 45],
        37: [6, 30, 49, 45, 47],
        38: [0, 13, 16, 25, 41],
        39: [7, 14],
        40: [17, 23, 48],
        41: [1, 15, 29, 38, 44],
        42: [18, 20, 49],
        43: [48],
        44: [5, 24, 41],
        45: [18, 35, 36, 37, 47],
        46: [0, 16],
        47: [3, 18, 30, 37, 45],
        48: [29, 34, 40, 43],
        49: [20, 33, 37, 42]
    }

    # Create an undirected graph (assumes symmetric connections)
    G = nx.Graph()

    # Add edges
    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Draw the graph
    plt.figure(figsize=(16, 12))
    pos = nx.spring_layout(G, seed=42)  # nice layout
    nx.draw_networkx(G, pos, node_size=500, node_color="skyblue", with_labels=True, font_size=8)
    plt.title("Graph from Adjacency List", fontsize=16)
    plt.axis("off")
    plt.show()