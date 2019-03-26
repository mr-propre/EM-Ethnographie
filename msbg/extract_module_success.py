#!/usr/bin/env python3

import pandas as pd
import sys

#file who get the final module excel already modified (i will clean this) it generate a file with Code Module and percent of sucess

filePath = sys.argv[1]
xlsx = pd.read_excel(filePath, usecols=[2, 4])

resultDF = pd.DataFrame()

moduleID = xlsx.iloc[0, 0]
sumOfSuccess = 0
i = 0

#for each row if it's the same module it will add if the student succeed or not
#when all the student are taken in sumOfSucess it will do the mean of success and
# create an row of excel with the module Id and his mean of success

for index, row in xlsx.iterrows():
    if moduleID == row[0]:
        sumOfSuccess += row[1]
        i += 1

    else:
        print(moduleID)
        mean = sumOfSuccess / i
        resultDF = resultDF.append([(moduleID, mean, i)], ignore_index=True)
        sumOfSuccess = 0
        moduleID = row[0]
        sumOfSuccess += row[1]
        i = 1

resultDF.to_excel("percentPerModule.xlsx")
