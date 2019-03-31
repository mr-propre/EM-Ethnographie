#!/usr/bin/env python3

import csv
import itertools
import pandas
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.community as com
import community
import os
import datetime


def find_city(row, f):
    count = 0
    for i,r in f.iterrows():
        if (r["id"] == row["id1"] or r["id"] == row["id2"]):
            count += 1
        if (count >= 2):
            return True
    return False

def graph_networkx(f, filename):
    G = nx.Graph()
    df = pandas.read_csv("final_binomes.csv", delimiter=';', header=0, names=["id1", "id2","nomProjet","idProjet","nbProjetCommun"])


    # Creation of edges and nodes
    print("Create edges and nodes")
    print(datetime.datetime.now())
    for index,row in df.iterrows():
        if (find_city(row, f) == True and int(row["nbProjetCommun"]) > 0):
            G.add_edge(row["id1"], row["id2"], weight=int(row["nbProjetCommun"]))

    # Clustering
    p = community.best_partition(G, weight='weight')
    
    # export
    print("exporting data : " + filename[:-4] + "_edges.csv")
    print(datetime.datetime.now())

    export = open("promo_city/" + filename[:-4] + "_edges.csv", "w")
    all_edges = pandas.read_csv("completed_binomes.csv", delimiter=';', header=1, names=["id1", "id2", "code_activity", "time_start", "time_end", "start", "end"])

    export.write("Source;Target;Code_Activity;timestamp_start;timestamp_end;Start;End;Cluster\n")
    for index, row in all_edges.iterrows():
        for c, v in p.items():
            if (row["id1"] == str(c)):
                for c2, v2 in p.items():
                    if (row["id2"] == str(c2)):
                        export.write(";".join(str(value) for value in row))
                        if (v == v2):
                            export.write(";" + str(v + 1) + "\n")
                        else:
                            export.write(";0\n")
    
    export.close()
    print("done")


def main():
    d = 'promo_city'

    for filename in os.listdir(d):
        print("Start : " + filename)
        if (filename.endswith(".csv") and filename.endswith("edges.csv") == False and os.path.isfile("./promo_city/" + filename[:-4] + "_edges.csv") != True):
            f = pandas.read_csv(d + "/" + filename, delimiter=';', header=1, names=["id", "year", "promo", "city", "gpa"])
            graph_networkx(f, filename)
    
if __name__== "__main__":
    main()

