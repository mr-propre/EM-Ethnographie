#!/usr/bin/env python3

import csv
import pandas
import itertools
from datetime import datetime

df = pandas.read_csv("data/gephi_binomes_time.csv", delimiter=';', header=1)
ref = pandas.read_csv("data/cluster_1.csv", delimiter=';', header=0, names=["id","cluster","city"])

tab = []

f = open("data/gephi_binomes_clustered.csv", "w")

for index,row in df.iterrows():
    for inde,ro in ref.iterrows():
        if (ro["id"] == row[0]):
            for value in row:
                f.write(str(value) + ";")
            f.write(str(ro["cluster"]) + "\n")

f.close()





