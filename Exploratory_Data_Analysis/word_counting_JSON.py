import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
import json

def word_to_json():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    with open('../Dataset/Books/stop_words_english.txt', 'r') as stop_words_english:
        stop_words = stop_words_english.read().splitlines()
    with open("../Dataset/Books/word_counting.json", 'w') as f:
        for nb in book_list:
            print(nb)
            words_book_counter = []
            allLines = []
            with open('../Dataset/Books/Book'+nb+'.txt', 'r') as book:
                lines = book.read().splitlines()
                allLines += lines
            words = [w for segments in allLines for w in segments.split() if not segments.startswith('Page | ')
                                                                        and not w.lower() in stop_words]
            new_words = []
            punctuation = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~0123456789—|•■□'''
            for i, word in enumerate(words):
                new_word = ""
                i = 0
                for char in word:
                    if char not in punctuation:
                        new_word += char
                    else:
                        if i != 0:
                            break
                    i+=1
                if new_word != "" and not new_word.lower() in stop_words:
                    if new_word.lower() in new_words:
                        new_words.append(new_word.lower())
                    else:
                        new_words.append(new_word) #TODO add only lower case words?
            wordsSet = set(new_words)
            wordsCounter = Counter(new_words)
            wordsCounter  = {k: v for k, v in sorted(wordsCounter.items(), key=lambda item: item[1], reverse=True)}
            for (w, c) in wordsCounter.items():
                words_book_counter.append([w, c])
            df = pd.DataFrame(words_book_counter, columns=['Word', 'Count'])
            json.dump(df[:200].to_json(orient='records'), f)

def word_to_json_total():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    with open('../Dataset/Books/stop_words_english.txt', 'r') as stop_words_english:
        stop_words = stop_words_english.read().splitlines()
    with open("../Dataset/Books/word_counting_total.json", 'w') as f:
        words_book_counter = []
        new_words = []
        for nb in book_list:
            print(nb)
            allLines = []
            with open('../Dataset/Books/Book'+nb+'.txt', 'r') as book:
                lines = book.read().splitlines()
                allLines += lines
            words = [w for segments in allLines for w in segments.split() if not segments.startswith('Page | ')
                                                                        and not w.lower() in stop_words]
            punctuation = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~0123456789—|•■□'''
            for i, word in enumerate(words):
                new_word = ""
                i = 0
                for char in word:
                    if char not in punctuation:
                        new_word += char
                    else:
                        if i != 0:
                            break
                    i+=1
                if new_word != "" and not new_word.lower() in stop_words:
                    if new_word.lower() in new_words:
                        new_words.append(new_word.lower())
                    else:
                        new_words.append(new_word) #TODO add only lower case words?
        wordsSet = set(new_words)
        wordsCounter = Counter(new_words)
        wordsCounter  = {k: v for k, v in sorted(wordsCounter.items(), key=lambda item: item[1], reverse=True)}
        for (w, c) in wordsCounter.items():
            words_book_counter.append([w, c])
        df = pd.DataFrame(words_book_counter, columns=['Word', 'Count'])
        json.dump(df[:200].to_json(orient='records'), f)

#words_in_books()
word_to_json_total()

# df = pd.DataFrame(pd.read_csv('../Dataset/Books/word_counting.csv'))
# print(df.loc[df['Book'].isin([1, 4, 5])].groupby(['Word']).sum().sort_values('Count', ascending=False))
