#!/usr/bin/env python3

import json
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

with open("data/final_binomes.json") as f:
    data = json.load(f)

H = nx.path_graph(10)
G.add_nodes_from(H)
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()