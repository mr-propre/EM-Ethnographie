#!/usr/bin/env python3

import pandas as pd
import sys

filePath = sys.argv[1]
xlsx = pd.read_excel(filePath, usecols=[2, 4])

resultDF = pd.DataFrame()

moduleID = xlsx.iloc[0, 0]
sumOfSuccess = 0
i = 0

for index, row in xlsx.iterrows():
    if moduleID == row[0]:
        sumOfSuccess += row[1]
        i += 1

    else:
        print(moduleID)
        mean = sumOfSuccess / i
        print(type(moduleID))
        print(type(mean))
        print(type(i))
        resultDF = resultDF.append([(moduleID, mean, i)], ignore_index=True)
        sumOfSuccess = 0
        moduleID = row[0]
        sumOfSuccess += row[1]
        i = 1

resultDF.to_excel("percentPerModule.xlsx")
