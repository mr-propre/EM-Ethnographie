#!/usr/bin/env python3

import pandas as pd
import sys

#the title of this file is no more valid, i transformed the json into an excel before using it(personnal reasons)
# the goal of this is to get all the module linked to the activities in it.

filePath = sys.argv[1]
json = pd.read_excel('transformedJson.xlsx')

resultDF = pd.DataFrame()

list_modules = []
list_acti = []

# First step is to get the code of the module
# If we didnt already work on it we create a new list
# Then we get all the activity and put them in the boxes we created for them linked to an index to find the module name

for index, row in json.iterrows():
    begin = row[1].find('\'codemodule\': \'') + 15
    end = row[1].find('\'', begin + 1)
    new_name = row[1][begin:end]
    if new_name not in list_modules:
        name_module = new_name
        list_modules.append(name_module)
        list_acti.append([])
    index_module = list_modules.index(new_name)
    begin_acti = 0
    i = 0
    while begin_acti != 17:
        i += 1
        begin_acti = row[1].find('\'codeacti\': \'acti-', begin_acti) + 18
        if begin_acti != 17:
            end_acti = row[1].find('\'', begin_acti + 1)
            if len(row[1][begin_acti:end_acti]) > 4:
                new_acti_code = row[1][begin_acti:end_acti]
                list_acti[index_module].append(new_acti_code)

i = 0
while i != len(list_modules):
    resultDF = resultDF.append([(list_modules[i], list_acti[i])], ignore_index=True)
    i += 1
resultDF.to_excel("moduleLinkedToActivities.xlsx")
