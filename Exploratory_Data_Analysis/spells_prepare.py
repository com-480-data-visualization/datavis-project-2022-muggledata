import json
import numpy as np
import pandas as pd
from random import randrange

spells = pd.read_csv("../Dataset/spell_counting.csv", sep=',')

df = pd.DataFrame(spells)
df = df.drop('Light', 1)

j = []

for type in df['Type'].unique():
    df_type = df[df['Type']==type]
    children = []
    for i, spell in df_type.iterrows():
        s = {
            'name': spell['Name'],
            'value': spell['Count']
        }
        children.append(s)
    child = {
        'name': type,
        'value': len(df[df['Type']==type]),
        'children': children
    }
    j.append(child)

with open('spells.json', 'w') as outfile:
    json.dump(json.dumps(j), outfile)

