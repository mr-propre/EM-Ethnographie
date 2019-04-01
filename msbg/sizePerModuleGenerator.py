#!/usr/bin/env python3

import pandas as pd

modulesFile = pd.read_excel('moduleLinkedToActivities.xlsx', usecols=[1, 2])
sizeFile = pd.read_excel('sizePerProject.xlsx', usecols=[1, 2])

resultDF = pd.DataFrame()

for index, row in modulesFile.iterrows():
    sum = 0
    total = 0
    max = row[1].count('\'')
    for jindex, jrow in sizeFile.iterrows():
        true_module_id = str(int(jrow[0]))
        deb = row[1].find(true_module_id)
        if deb != -1 and row[1][deb + len(true_module_id)] == '\'':
            sum += jrow[1]
            total +=1
        if total == max:
            break
    if total == 0:
        mean = 0
    else:
        mean = sum / total
    resultDF = resultDF.append([(row[0], mean)], ignore_index=True)

resultDF.to_excel("meanSizePerModule.xlsx")
