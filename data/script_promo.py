#!/usr/bin/env python3

import csv
import pandas
import itertools

df = pandas.read_csv("final_binomes.csv", delimiter=';', header=0, names=["id1", "id2","nomProjet","idProjet","nbProjetCommun"])

gpa = pandas.read_csv("GPA.csv", delimiter=';', header=1, names=["id","gpa"])
promo = pandas.read_csv("final_usr_promo.csv", delimiter=',', header=1, names=["id", "year", "promo", "city"])

f = open("binomes_city_promo.csv", "w")

for b_index, b_row in df.iterrows():
    for promo_i, promo_r in promo.iterrows():
        if (b_row["id1"] == promo_r["id"]):
            for value in promo_r:
                f.write(str(value) + ";")
            f.write(str(gpa_row["gpa"]).replace(",", ".") + "\n")

f.close()
