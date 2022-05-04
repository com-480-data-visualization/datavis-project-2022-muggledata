import numpy as np
import pandas as pd
from difflib import SequenceMatcher

characters_dscr = pd.read_csv("../Dataset/HPCharactersData.csv")
characters = pd.read_csv("../Dataset/Characters.csv")

df_descr = pd.DataFrame(characters_dscr)
df_char = pd.DataFrame(characters)
names = []
#compare = df_descr['Name'].compare(df_char['Name'])
descr_list = []
for name in df_char['Name']:
    sim_name = []
    for name2 in df_descr['Name']:
        sim = SequenceMatcher(None, name, name2).ratio()
        sim_name.append(sim)
    i = np.argmax(sim_name)
    # if sim_name[i] < 1.:
    #     print(list(df_char['Name']).index(name) + 1, name + '|' + df_descr['Name'][i], i + 2, '\n')
    descr_list.append(df_descr['Descr'][i])
    names.append(df_descr['Name'][i])
df_char.insert(13, 'Description', descr_list)
df_char.to_csv('../Dataset/Characters.csv')
#print(names)
#print(compare)
print(len(names), len(df_char['Name']))