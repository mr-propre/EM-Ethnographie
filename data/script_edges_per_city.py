#!/usr/bin/env python3

import csv
import itertools
import pandas
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.community as com
import community
from operator import itemgetter

tab_city = ["PAR", "BDX", "NCY", "LYN", "TLS", "REN", "LIL", "STG", "MPL", "NCE", "MAR", "RUN", "TIR", "NAN"]
tab_promo = ["all", "2022", "2021", "2020"]

G = nx.Graph()

df = pandas.read_csv("final_binomes.csv", delimiter=';', header=0, names=["id1", "id2","nomProjet","idProjet","nbProjetCommun"])








# Creation of edges and nodes
i = 0
for index,row in df.iterrows():
    if (row["id1"] != "hors_cohorte" and row["id2"] != "hors_cohorte" and int(row["nbProjetCommun"]) > 0):
        G.add_edge(row["id1"], row["id2"], weight=int(row["nbProjetCommun"]))
        i += 1


# first clustering to split cities, and remove node who don't belong to 'ville'
p = community.best_partition(G, weight='weight')
for c, v in p.items():
    if (v != ville):
        G.remove_node(c)


# second clustering to determine group inside a city
p = community.best_partition(G, weight='weight')


# export clusters for the city
f = open("data/cluster_" + str(ville) + ".csv", "w")
for c, v in p.items():
    f.write(str(c) + ";" + str(v) + ";" + str(ville) + "\n")
f.close()


# export gexf format for gephi
# nx.write_gexf(G, "graph.gexf", prettyprint=True)

print ("Number of edges : ", i)
print ("Number of nodes : ", nx.number_of_nodes(G))

weights = [G[u][v]['weight']/7 for u,v in G.edges] # take weight into account for edges

# draw and show
nx.draw(G, node_size=50, width=weights, node_color=color_map)
plt.show()

