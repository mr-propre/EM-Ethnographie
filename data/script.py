#!/usr/bin/env python3

import csv
import pandas
import itertools
from datetime import datetime

df = pandas.read_csv("GPA.csv", delimiter=';', header=1)
ref = pandas.read_csv("cluster_1.csv", delimiter=';', header=0, names=["id","cluster","city"])

tab = []

f = open("gephi_gpa.csv", "w")

for index,row in df.iterrows():
    for inde,ro in ref.iterrows():
        if (ro["id"] == row[1]):
            f.write(row[1] + ";" + row[2].replace(",", ".") + "\n")
            #for value in row:
            #    f.write(str(value) + ";")
            #f.write(str(ro["cluster"]) + "\n")

f.close()





