import json
from turtle import position
import numpy as np
import pandas as pd
from random import randrange

spells = pd.read_csv("../Dataset/spell_sorting.csv", sep=',')

df = pd.DataFrame(spells)
spells_name = df['Name']
pos_columns = df.columns[5::2]
count_columns = df.columns[6::2]

j = []
for pos_col, count_col in zip(pos_columns, count_columns):
    position = df[pos_col]
    count= df[count_col]
    book = {'book': pos_col}
    for spell, pos, c in zip(df.iterrows(), position, count):
        if not pd.isna(pos):
            book[spell[1]['Name']] = {
                "incantation": spell[1]['Incantation'],
                "position": int(pos),
                "count": int(c),
                "type": spell[1]['Type'],
                "effect": spell[1]['Effect'],
                "light": spell[1]['Light'] if pd.isna(spell[1]['Light']) else None,
            }
    j.append(book)
#print(j)
with open('../Dataset/spells_book2.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json.dumps(j, indent=4))
# j = []

# for type in df['Type'].unique():
#     df_type = df[df['Type']==type]
#     children = []
#     for i, spell in df_type.iterrows():
#         s = {
#             'name': spell['Name'],
#             'value': spell['Count']
#         }
#         children.append(s)
#     child = {
#         'name': type,
#         'value': len(df[df['Type']==type]),
#         'children': children
#     }
#     j.append(child)

# with open('spells.json', 'w') as outfile:
#     json.dump(json.dumps(j), outfile)

