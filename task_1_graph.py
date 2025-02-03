import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# add edges with bandwidth
edges = [
    (0, 2, 25),  # Terminal 1 -> Warehouse 1
    (0, 3, 20),  # Terminal 1 -> Warehouse 2
    (0, 4, 15),  # Terminal 1 -> Warehouse 3
    (1, 3, 10),  # Terminal 2 -> Warehouse 2
    (1, 4, 15),  # Terminal 2 -> Warehouse 3
    (1, 5, 30),  # Terminal 2 -> Warehouse 4
    (2, 6, 15),  # Warehouse 1 -> Store 1
    (2, 7, 10),  # Warehouse 1 -> Store 2
    (2, 8, 20),  # Warehouse 1 -> Store 3
    (3, 9, 15),  # Warehouse 2 -> Store 4
    (3, 10, 10),  # Warehouse 2 -> Store 5
    (3, 11, 25),  # Warehouse 2 -> Store 6
    (4, 12, 20),  # Warehouse 3 -> Store 7
    (4, 13, 15),  # Warehouse 3 -> Store 8
    (4, 14, 10),  # Warehouse 3 -> Store 9
    (5, 15, 20),  # Warehouse 4 -> Store 10
    (5, 16, 10),  # Warehouse 4 -> Store 11
    (5, 17, 15),  # Warehouse 4 -> Store 12
    (5, 18, 5),  # Warehouse 4 -> Store 13
    (5, 19, 10),  # Warehouse 4 -> Store 14
]

# Add edges to the graph
G.add_weighted_edges_from(edges)

# positions for the nodes
pos = {
    0: (2, 0),  # Terminal 1
    1: (10, 0),  # Terminal 2
    2: (4, 2),  # Warehouse 1
    3: (8, 2),  # Warehouse 2
    4: (4, -2),  # Warehouse 3
    5: (8, -2),  # Warehouse 4
    6: (0, 4),  # Store 1
    7: (2, 4),  # Store 2
    8: (4, 4),  # Store 3
    9: (6, 4),  # Store 4
    10: (8, 4),  # Store 5
    11: (10, 4),  # Store 6
    12: (0, -4),  # Store 7
    13: (2, -4),  # Store 8
    14: (4, -4),  # Store 9
    15: (6, -4),  # Store 10
    16: (8, -4),  # Store 11
    17: (10, -4),  # Store 12
    18: (12, -4),  # Store 13
    19: (14, -4),  # Store 14
}

# build capacity matrix for flows bandwidth for the given graph
capacity_matrix = [
    [0, 0, 25, 20, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Terminal 1
    [0, 0, 0, 10, 15, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Terminal 2
    [0, 0, 0, 0, 0, 0, 15, 10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Warehouse 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 10, 25, 0, 0, 0, 0, 0, 0, 0, 0],  # Warehouse 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 15, 10, 0, 0, 0, 0, 0],  # Warehouse 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 10, 15, 5, 10],  # Warehouse 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Store 14
]

if __name__ == "__main__":
    # Draw the graph
    plt.figure(figsize=(16, 10))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="skyblue",
        font_size=12,
        font_weight="bold",
        arrows=True,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)

    # Show the plot
    plt.show()
