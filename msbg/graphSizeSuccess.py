#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

xlsx = pd.read_excel('FinalFile2.xlsx')
print(xlsx.iloc[0, 3])
nodeNB = int(sys.argv[1])

sum_success = 0
student_nb = 0
sum_size = 0

xlist = []
ylist = []

for index, row in xlsx.iterrows():
    print(row[1])
    while row[3] != 0:
        if student_nb == 0 and row[3] > nodeNB:
            if row[1] < 10:
                xlist.append(row[1])
                ylist.append(row[2])
            row[3] -= nodeNB
        elif nodeNB - (student_nb + row[3]) <= 0:
            row[3] -= (nodeNB - student_nb)
            sum_success += row[2] * (nodeNB - student_nb)
            sum_size += row[1] * (nodeNB - student_nb)
            if sum_size / nodeNB < 10:
                xlist.append(sum_size / nodeNB)
                ylist.append(sum_success / nodeNB)
            sum_success = 0
            sum_size = 0
            student_nb = 0
        else:
            student_nb += row[3]
            sum_success += row[2] * row[3]
            sum_size += row[1] * row[3]
            row[3] = 0


x = np.array(xlist)
y = np.array(ylist)

#print(xlist)

plt.plot(x, y)
plt.show()

