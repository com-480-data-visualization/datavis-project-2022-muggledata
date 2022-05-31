import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
import json

def word_to_json_total():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    #with open("../Dataset/Books/word_counting_total.json", 'w') as f:
    spells = pd.DataFrame(pd.read_csv("../Dataset/spell_counting.csv", sep=',', usecols=['Name', 'Incantation']))
    spells_names = spells['Name']
    spells_incantation = spells['Incantation']
    for nb in book_list:
        allLines = []
        spell_book_counter = []
        with open('../Dataset/Books/Book'+nb+'.txt', 'r') as book:
            lines = book.read().splitlines()
            allLines += lines

        #All words 
        lines = [segments for segments in allLines]
        #words = [w for segments in allLines for w in segments.split()]

        # spells_incantation.drop(spells_incantation[spells_incantation == 'Unknown'])
        #punctuation = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~0123456789—|•■□'''
        spells_list = []
        for j, l in enumerate(lines):
            print(j * 100 / len(lines), end='\r')
            for i, (sname, incant) in enumerate(zip(spells_names, spells_incantation)):
                if sname in str(l) or (incant in str(l) and incant != "Unknown"):
                    spells_list.append(sname)
        print("spell list done finish")
        spellCounter = Counter(spells_list)
        spellCounter  = {k: int(v) for k, v in sorted(spellCounter.items(), key=lambda item: item[1], reverse=True)}
        for (s, c) in spellCounter.items():
            spell_book_counter.append([s, c])
        df = pd.DataFrame(spell_book_counter, columns=['Name', 'Book' + nb])
        print(df)
        #print(spells)
        spells = spells.join(df.set_index('Name'), on='Name')
    spells.to_csv('../Dataset/spell_counting2.csv', index=False)

        # json.dump(df[:200].to_json(orient='records'), f)

#words_in_books()
word_to_json_total()


# df = pd.DataFrame(pd.read_csv('../Dataset/Books/word_counting.csv'))
# print(df.loc[df['Book'].isin([1, 4, 5])].groupby(['Word']).sum().sort_values('Count', ascending=False))
