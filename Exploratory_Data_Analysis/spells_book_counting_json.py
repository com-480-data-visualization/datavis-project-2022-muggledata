import json
import numpy as np
import pandas as pd
from random import randrange

spells = pd.read_csv("../Dataset/spell_counting2.csv", sep=',')

df = pd.DataFrame(spells)
spells_name = df['Name']
#df = df.drop('Light', 1)
columns = df.columns[2:]

j = []
for col in columns:
    count = df[col].dropna()
    book = {'book': col}
    for name, c in zip(spells_name, count):
        if c is not None:
            book[name] = int(c)
    j.append(book)
print(j)
with open('../Dataset/spells_book.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json.dumps(j))
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

