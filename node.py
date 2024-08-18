import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

edges = [
    ('A', 'B', 3), ('A', 'D', 4), ('A', 'C', 5),
    ('B', 'D', 2), ('B', 'E', 5), 
    ('C', 'G', 7), 
    ('D', 'A', 4), ('D', 'C', 2), ('D', 'E', 4), ('D', 'F', 6),
    ('E', 'H', 8),
    ('F', 'H', 4),
    ('G', 'F', 3)
]

def get_neighbor(curr):
    neighbors = []
    for e in edges:
        if e[0] == curr:
            neighbors.append(e[1])
    return neighbors

if __name__ == "__main__":

    # 设置随机数种子
    np.random.seed(1200)

    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G, k=0.5, iterations=30)  # 调整 k 值
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()
