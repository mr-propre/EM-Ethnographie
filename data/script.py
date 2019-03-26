#!/usr/bin/env python3

import csv
import pandas
import itertools
from datetime import datetime

def write_file(row, f):
    separator = ";"
    f.write(separator.join(str(value) for value in row) + "\n")

promo = pandas.read_csv("profile_promo_gpa.csv", delimiter=';', header=1, names=["id", "year", "promo", "city", "gpa"])

tab_city = ["PAR", "BDX", "NCY", "LYN", "TLS", "REN", "LIL", "STG", "MPL", "NCE", "MAR", "RUN", "TIR", "NAN"]

for city in tab_city:
    f = open("promo_city/all_promo_" + city +"_profile.csv", "w")
    fa = open("promo_city/2022_" + city +"_profile.csv", "w")
    fb = open("promo_city/2021_" + city + "_profile.csv", "w")
    fc = open("promo_city/2020_" + city + "_profile.csv", "w")
    f.write("id;year;promo;city;gpa\n")
    fa.write("id;year;promo;city;gpa\n")
    fb.write("id;year;promo;city;gpa\n")
    fc.write("id;year;promo;city;gpa\n")

    for index,row in promo.iterrows():
        if (row["city"] == city):
            write_file(row, f)
            if (row["promo"] == 2022):
                write_file(row, fa)
            if (row["promo"] == 2021):
                write_file(row, fb)
            if (row["promo"] == 2020):
                write_file(row, fc)


    f.close()
    fa.close()
    fb.close()
    fc.close()





