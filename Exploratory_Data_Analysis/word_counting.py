import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

def words_in_books():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    allLines = []
    words_book_counter = []
    with open('../Dataset/Books/stop_words_english.txt', 'r') as stop_words_english:
        stop_words = stop_words_english.read().splitlines()
    for nb in book_list:
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
                new_words.append(new_word.lower()) #TODO add only lower case words?
        wordsSet = set(new_words)
        wordsCounter = Counter(new_words)
        wordsCounter  = {k: v for k, v in sorted(wordsCounter.items(), key=lambda item: item[1], reverse=True)}
        for (w, c) in wordsCounter.items():
            words_book_counter.append([w, nb, c])
    df = pd.DataFrame(words_book_counter, columns=['Word', 'Book', 'Count'])
    df.to_csv('../Dataset/Books/word_counting.csv')

words_in_books()

df = pd.DataFrame(pd.read_csv('../Dataset/Books/word_counting.csv'))
print(df.loc[df['Book'].isin([1, 4, 5])].groupby(['Word']).sum().sort_values('Count', ascending=False))

    # number_to_plot = 20
    # count_serie = pd.Series(list(wordsCounter.values())[:number_to_plot])
    # plt.figure(figsize=(fig_sizes[0], fig_sizes[1]))
    # ax = count_serie.plot(kind='bar')
    # ax.set_title("Words in all books", fontsize=fontsize)
    # ax.set_xlabel("Words", fontsize=fontsize)
    # ax.set_ylabel("Number", fontsize=fontsize)
    # ax.set_xticklabels(list(wordsCounter.keys())[:number_to_plot], rotation=20, fontsize=fontsize)
    # plt.yticks(fontsize=fontsize)
    # plt.savefig('../Figs/words_counter.png')