#!/usr/bin/env python3

import csv
import pandas
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

with open("data/final_binomes.csv") as f:
    reader = csv.reader(f, delimiter=';')
df = pandas.read_csv("data/final_binomes.csv", delimiter=';', header=0, names=["id1","id2","nomProjet","idProjet", "nbProjetCommun"])


i = 0
for index,row in df.iterrows():
    if (row["id1"] != "hors_cohorte" and row["id2"] != "hors_cohorte"):
        G.add_edge(row["id1"], row["id2"], weight=int(row["nbProjetCommun"]))
    i += 1
    if (i > 1000):
        break
H = nx.path_graph(10)
plt.subplot(121)
nx.draw(G, node_size=10)
plt.show()