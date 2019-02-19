#!/usr/bin/env python3

import csv
import json


f = open('data/final_binomes.csv', 'r')
j = open( 'data/final_binomes.json', 'w')
reader = csv.DictReader(f, fieldnames = ["id1","id2","nomProjet","idProjet", "nbProjetCommun"], delimiter=';')
print ("JSON parsed!")  
for row in reader:
    json.dump(row, j)
    j.write('\n')
# Save the JSON  
print ("JSON saved!")
