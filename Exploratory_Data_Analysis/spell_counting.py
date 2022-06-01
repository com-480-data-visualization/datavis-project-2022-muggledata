import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
import json

def word_to_json_total():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    #with open("../Dataset/Books/word_counting_total.json", 'w') as f:
    spells = pd.DataFrame(pd.read_csv("../Dataset/spell_counting.csv", sep=','))
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
#word_to_json_total()



def spells_total_count():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    #with open("../Dataset/Books/word_counting_total.json", 'w') as f:
    spells = pd.DataFrame(pd.read_csv("../Dataset/Spells.csv", sep=';', usecols=['Name', 'Incantation', 'Type']))
    spells_names = spells['Name']
    spells_incantation = spells['Incantation']
    spells_list = []
    spell_book_counter = []
    for nb in book_list:
        allLines = []
        with open('../Dataset/Books/Book'+nb+'.txt', 'r') as book:
            lines = book.read().splitlines()
            allLines += lines

        #All words 
        lines = [segments for segments in allLines]
        #words = [w for segments in allLines for w in segments.split()]

        # spells_incantation.drop(spells_incantation[spells_incantation == 'Unknown'])
        #punctuation = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~0123456789—|•■□'''
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
    df = pd.DataFrame(spell_book_counter, columns=['Name', 'Count'])
    print(df)
    df = spells.join(df.set_index('Name'), on='Name').dropna()
    df.to_csv('../Dataset/spell_counting3.csv', index=False)

#spells_total_count()


def spells_sorting():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    #with open("../Dataset/Books/word_counting_total.json", 'w') as f:
    spells = pd.DataFrame(pd.read_csv("../Dataset/Spells.csv", sep=';'))
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
        spellCounter  = {k: v for k, v in sorted(spellCounter.items(), key=lambda item: item[1], reverse=True)}
        # for s in list(spellCounter.keys()):
        #     print(len(list(spellCounter)) - list(spellCounter).index(s))
        for (s, c) in spellCounter.items():
            pos = 5 - list(spellCounter).index(s)
            if pos <= 0:
                pos = None
            spell_book_counter.append([s, pos,  c])
        df = pd.DataFrame(spell_book_counter, columns=['Name', 'Book' + nb, 'Book' + nb + 'count'])
        print(df)
        spells = spells.join(df.set_index('Name'), on='Name')
        #spells['Book' + nb][spells['Book' + nb].isna()] = -1
    spells.to_csv('../Dataset/spell_sorting.csv', index=False)
spells_sorting()
