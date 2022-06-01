import json
import numpy as np
import pandas as pd
from random import randrange

spells = pd.read_csv("../Dataset/spell_counting3.csv", sep=',')

df = pd.DataFrame(spells)
j = []

for type in df['Type'].unique():
    df_type = df[df['Type']==type]
    children = []
    for i, spell in df_type.iterrows():
        s = {
            'name': spell['Name'],
            'value': int(spell['Count'])
        }
        children.append(s)
    child = {
        'name': type,
        'value': len(df[df['Type']==type]),
        'children': children
    }
    j.append(child)

with open('../Dataset/spells.json', 'w') as outfile:
    json.dump(json.dumps(j), outfile)

