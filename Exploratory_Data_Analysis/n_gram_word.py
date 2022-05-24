import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import json

def n_gram_words():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    with open('../Dataset/Books/stop_words_english.txt', 'r') as stop_words_english:
        stop_words = stop_words_english.read().splitlines()
    with open("../Dataset/Books/2_gram_words_allBook.json", 'w') as f:
        new_words = []
        for nb in book_list:
            print(nb)
            words_book_counter = []
            allLines = []
            with open('../Dataset/Books/Book'+nb+'.txt', 'r') as book:
                lines = book.read().splitlines()
                allLines += lines
            words = [w for segments in allLines if (not segments.startswith('Page | ') and not segments.endswith('Rowling ')) for w in segments.split()]
            punctuation = '''!()[]{};:"“”\,<>./?@#$%^&*_~0123456789—|•■□'''
            for i, word in enumerate(words):
                new_word = ""
                i = 0
                for char in word:
                    if char not in punctuation and not (i == 0 and char == "'"):
                        new_word += char
                    # else:
                    #     if i != 0:
                    #         break
                    i+=1
                if new_word != "":
                    #if new_word.lower() in new_words:
                    new_words.append(new_word.lower())
                    # else:
                    #     new_words.append(new_word) #TODO add only lower case words?
        words_2_gram = []
        for i in range(len(new_words) - 1):
            words_2_gram.append(new_words[i] + ' ' + new_words[i + 1])
        words_2_gram_without_stop_word = []
        for word in words_2_gram:
            #print(word)
            if word.split()[0] not in stop_words and word.split()[1] not in stop_words:
                #print(word)
                words_2_gram_without_stop_word.append(word)
        wordsCounter = Counter(words_2_gram_without_stop_word)
        wordsCounter  = {k: v for k, v in sorted(wordsCounter.items(), key=lambda item: item[1], reverse=True)}
        for (w, c) in wordsCounter.items():
            words_book_counter.append([w, c])
        df = pd.DataFrame(words_book_counter, columns=['Words', 'Count'])
        print(df)
        json.dump(df[:1000].to_json(orient='records'), f)

def _2_gram_book(book):
    book_list = [book]
    with open('../Dataset/Books/stop_words_english.txt', 'r') as stop_words_english:
        stop_words = stop_words_english.read().splitlines()
    with open("../Dataset/Books/2_gram_words_book"+ book + ".json", 'w') as f:
        new_words = []
        for nb in book_list:
            print(nb)
            words_book_counter = []
            allLines = []
            with open('../Dataset/Books/Book'+nb+'.txt', 'r') as book:
                lines = book.read().splitlines()
                allLines += lines
            words = [w for segments in allLines if (not segments.startswith('Page | ') and not segments.endswith('Rowling ')) for w in segments.split()]
            punctuation = '''!()-[]{};:"“”\,<>./?@#$%^&*_~0123456789—|•■□'''
            for i, word in enumerate(words):
                new_word = ""
                #i = 0
                for char in word:
                    if char not in punctuation and not (i == 0 and char == "'"):
                        new_word += char
                    # else:
                    #     if i != 0:
                    #         break
                    # i+=1
                if new_word != "":
                    if new_word.lower() in new_words:
                        new_words.append(new_word.lower())
                    else:
                        new_words.append(new_word) #TODO add only lower case words?
        words_2_gram = []
        for i in range(len(new_words) - 1):
            words_2_gram.append(new_words[i] + ' ' + new_words[i + 1])
        words_2_gram_without_stop_word = []
        for word in words_2_gram:
            if word.split()[0] not in stop_words and word.split()[1] not in stop_words:
                words_2_gram_without_stop_word.append(word)
        wordsCounter = Counter(words_2_gram_without_stop_word)
        wordsCounter  = {k: v for k, v in sorted(wordsCounter.items(), key=lambda item: item[1], reverse=True)}
        for (w, c) in wordsCounter.items():
            words_book_counter.append([w, c])
        df = pd.DataFrame(words_book_counter, columns=['Words', 'Count'])
        print(df)
        json.dump(df[:1000].to_json(orient='records'), f)

def book_specification(book):
    all_words = pd.read_json('../Dataset/Books/2_gram_words_allBook.json')
    words_book = pd.read_json('../Dataset/Books/2_gram_words_book'+book+'.json')
    reduce_words_book = []
    for i, row in words_book.iterrows():
        if not row['Words'].lower() in all_words[:100]['Words'].values:
            #print(row['Words'].lower())
            reduce_words_book.append([row['Words'], row['Count']])
    reduce_words_book = pd.DataFrame(reduce_words_book, columns=['Words', 'Count'])
    #reduce_words_book = words_book[~words_book['Words'].isin(all_words[:100]['Words'])]
    with open("../Dataset/Books/2_gram_words_specific_book"+book+'.json', 'w') as f:
        json.dump(reduce_words_book[:50].to_json(orient='records'), f)

#n_gram_words()
book_list = ['1', '2', '3', '4', '5', '6', '7']
for book in book_list:
    #_2_gram_book(book)
    book_specification(book)