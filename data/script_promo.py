#!/usr/bin/env python3

import csv
import pandas
import itertools

df = pandas.read_csv("gephi_binomes_clustered.csv", delimiter=';', header=1, names=["id1","id2","code","timestamp_start","timestamp_end","start","end","cluster"])

gpa = pandas.read_csv("GPA.csv", delimiter=';', header=1, names=["id","gpa"])
promo = pandas.read_csv("final_usr_promo.csv", delimiter=',', header=1, names=["id", "year", "promo", "city"])

f = open("profile_promo_gpa.csv", "w")

for gpa_index, gpa_row in gpa.iterrows():
    for promo_i, promo_r in promo.iterrows():
        if (gpa_row["id"] == promo_r["id"]):
            for value in promo_r:
                f.write(str(value) + ";")
            f.write(str(gpa_row["gpa"]).replace(",", ".") + "\n")

f.close()
