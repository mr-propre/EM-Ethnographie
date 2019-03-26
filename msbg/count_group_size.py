#!/usr/bin/env python3

import pandas as pd
import sys


teams = []


def mean_of_group_size(teams):
    j = 0
    nb = 0
    while j < len(teams):
        nb += len(teams[j])
        j += 1
    return nb / j


filePath = sys.argv[1]
xlsx = pd.read_excel(filePath, usecols=[0, 1, 3])
resultDF = pd.DataFrame()

teams_in_actis = []

set_acti = set()


for index, row in xlsx.iterrows():
    if str(row[2]).find(',') != -1:
        first_split = str(row[2]).split(',')
    else:
        first_split = str(row[2]).split('.')
    set_acti.update(first_split)

list_acti = list(set_acti)

print(len(list_acti))

index = 0


for index in range(0, 4723):
    print(index)
    teams_in_actis.append([])
    for i, row in xlsx.iterrows():
        if len(teams_in_actis[index]) > 50:
            break
        j = 0
        if str(row[2]).find(list_acti[index]) != -1:
            j = 0
            while j < len(teams_in_actis[index]) and j != -1:
                if row[0] in teams_in_actis[index][j]:
                    teams_in_actis[index][j].append(row[1])
                    j = -1
                else:
                    j += 1
            if j != -1:
                teams_in_actis[index].append([row[0], row[1]])
    name_acti = list_acti[index]
    mean = mean_of_group_size(teams_in_actis[index])
    resultDF = resultDF.append(([(name_acti, float(mean))]), ignore_index=True)

resultDF.to_excel("sizePerProject.xlsx")


