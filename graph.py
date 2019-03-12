#!/usr/bin/env python3

import csv
import itertools
import pandas
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.community as com
import community
from operator import itemgetter

G = nx.Graph()

with open("data/final_binomes.csv") as f:
    reader = csv.reader(f, delimiter=';')
df = pandas.read_csv("data/final_binomes.csv", delimiter=';', header=0, names=["id1","id2","nomProjet","idProjet", "nbProjetCommun"])

tekProject = [""]

i = 0
for index,row in df.iterrows():
    if (row["id1"] != "hors_cohorte" and row["id2"] != "hors_cohorte" and int(row["nbProjetCommun"]) > 0):
        G.add_edge(row["id1"], row["id2"], weight=int(row["nbProjetCommun"]))
        i += 1
color_map = []
#cities = com.greedy_modularity_communities(G)
def heaviest(G):
    u, v, w = max(G.edges(data='weight'), key=itemgetter(2))
    return (u, v)
cities = com.girvan_newman(G, most_valuable_edge=heaviest)
p = community.best_partition(G, weight='weight')
j = 0

for c, v in p.items():
    color_map.append(v)



# Girvan_newman
#for c in cities:
#    for b in sorted(c):
#        j += 1
#        for node in b:
#            if (j != 3):
#                color_map.append('blue')
#            elif (j == 3):
#                color_map.append('red')
#        print ("\n\n\n\n")
#    break

j = 0
#for city in cities:
#    if (j == 1):
#        for node in sorted(city):
#            color_map.append('blue')
#    else:
#        for node in sorted(city):
#            color_map.append('red')
#    j += 1



print ("Number of edges : ", i)
print ("Number of nodes : ", nx.number_of_nodes(G))
weights = [G[u][v]['weight']/7 for u,v in G.edges]
nx.draw(G, node_size=10, width=weights, node_color=color_map)
plt.show()

