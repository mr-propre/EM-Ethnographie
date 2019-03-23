#! bin/python3.6
import pandas as pd
import sys

filePath = sys.argv[1]
xlsx = pd.read_excel(filePath, index_col=0, usecols=[0, 4, 5])
xlsx = xlsx.sort_values(['Identifiant élève'], ascending=False)
xlsx = xlsx[xlsx['Grade obtenu'] != '-']
xlsx = xlsx['Grade obtenu'].replace(['A'], '4')
xlsx = xlsx['Grade obtenu'].replace(['B'], '3')
xlsx = xlsx['Grade obtenu'].replace(['C'], '2')
xlsx = xlsx['Grade obtenu'].replace(['D'], '1')

print(xlsx)

xlsxLen = xlsx['Identifiant élève'].count()
i = 0
while (i < xlsxLen):
    # Build of the new GPA dataFrame
    i += 1
