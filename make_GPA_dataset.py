#! bin/python3.6
import pandas as pd
import sys

filePath = sys.argv[1]
xlsx = pd.read_excel(filePath, usecols=[0, 4, 5])
xlsx = xlsx.sort_values(['Identifiant élève'], ascending=False)
xlsx = xlsx[xlsx['Grade obtenu'] != '-']
xlsx = xlsx[xlsx['Grade obtenu'] != 'Acquis']
xlsx['Grade obtenu'] = xlsx['Grade obtenu'].map({'A': 4, 'B': 3, 'C': 2, 'D': 1, 'Echec': 0})

resultDF = pd.DataFrame()
studentID = xlsx.iloc[0, 0]
GPA = 0
totalCreditsNb = 0
tmp = 0

# Reminder
# id --> row[0]
# grade --> row[1]
# creditsNb --> row[2]

for index, row in xlsx.iterrows():
    if studentID == row[0]:
        tmp += row[1] * row[2]
        totalCreditsNb += row[2]
    else:
        GPA = tmp / totalCreditsNb
        resultDF = resultDF.append([(studentID, GPA)], ignore_index=True)
        tmp = 0
        totalCreditsNb = 0
        tmp += row[1] * row[2]
        totalCreditsNb += row[2]
        studentID = row[0]

resultDF.to_excel("GPA.xlsx")