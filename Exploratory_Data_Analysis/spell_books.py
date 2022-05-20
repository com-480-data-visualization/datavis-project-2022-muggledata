import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
import json

def word_to_json_total():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    #with open("../Dataset/Books/word_counting_total.json", 'w') as f:
    spell_book_counter = []
    for nb in book_list:
        allLines = []
        with open('../Dataset/Books/Book'+nb+'.txt', 'r') as book:
            lines = book.read().splitlines()
            allLines += lines

    #All words 
    lines = [segments for segments in allLines]
    #words = [w for segments in allLines for w in segments.split()]
    #print(lines)
    
    spells = pd.DataFrame(pd.read_csv("../Dataset/Spells.csv", sep=';'))

    spells_names = spells['Name']
    spells_incantation = spells['Incantation']
    # spells_incantation.drop(spells_incantation[spells_incantation == 'Unknown'])
    #punctuation = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~0123456789—|•■□'''
    spells_list = []
    for j, l in enumerate(lines):
        print(j * 100 / len(lines), end='\r')
        for i, (sname, incant) in enumerate(zip(spells_names, spells_incantation)):
            if sname in str(l) or (incant in str(l) and incant != "Unknown"):
                spells_list.append(sname)
    print(spells_list)
    print("spell list done finish")
    spellSet = set(spells_list)
    spellCounter = Counter(spells_list)
    spellCounter  = {k: v for k, v in sorted(spellCounter.items(), key=lambda item: item[1], reverse=True)}
    for (s, c) in spellCounter.items():
        spell_book_counter.append([s, c])
    df = pd.DataFrame(spell_book_counter, columns=['Name', 'Count'])
    df = spells.merge(df, how="right", on='Name')
    df.to_csv('../Dataset/spell_counting.csv')

        # json.dump(df[:200].to_json(orient='records'), f)

#words_in_books()
word_to_json_total()

# df = pd.DataFrame(pd.read_csv('../Dataset/Books/word_counting.csv'))
# print(df.loc[df['Book'].isin([1, 4, 5])].groupby(['Word']).sum().sort_values('Count', ascending=False))
