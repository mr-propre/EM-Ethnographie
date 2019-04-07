#!/usr/bin/env python3

import pandas as pd

xlsx = pd.read_excel('data/final_modules_modified4.xlsx', usecols=[0, 2])

resultDF = pd.DataFrame()

moduleID = xlsx.iloc[0, 0]


countStudents = 0
sumOfSuccess = 0

for index, row in xlsx.iterrows():
    if moduleID == xlsx.iloc[index, 0]:
        countStudents += 1
        sumOfSuccess += row[1]
    else:
        print(moduleID)
        mean = sumOfSuccess / countStudents
        resultDF = resultDF.append(([(moduleID, mean, countStudents)]), ignore_index=True)
        sumOfSuccess = row[1]
        moduleID = xlsx.iloc[index, 0]
        countStudents = 1

resultDF.to_excel('percentPerModuleAccurate.xlsx')

