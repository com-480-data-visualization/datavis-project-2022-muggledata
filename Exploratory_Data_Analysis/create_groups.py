import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

# Plot Number of character in function of houses
fig_sizes = [6, 4.5]
fontsize=6
def plot_nbChar_houses():
    characters = pd.read_csv("../Dataset/Characters.csv")
    df = pd.DataFrame(characters)
    house = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]
    house_color = ["#740001", "#222f5b", "#2a623d", "#ecb939"]
    count = []
    for i, h in enumerate(house):
        names_DA_ind = df['House'].str.contains(h, na=False)
        c = characters['Name'][names_DA_ind].shape[0]
        count.append(c)
    count_serie = pd.Series(count)
    plt.figure(figsize=(fig_sizes[0], fig_sizes[1]))
    ax = count_serie.plot(kind='bar', color=house_color)
    ax.set_title("Number of characters in houses", fontsize=fontsize)
    ax.set_xlabel("Houses", fontsize=fontsize)
    ax.set_ylabel("Number", fontsize=fontsize)
    ax.set_xticklabels(house, rotation=0, fontsize=fontsize)
    ax.yaxis.label.set_size(fontsize)
    plt.yticks(fontsize=fontsize)
    plt.savefig('../Figs/houses.png')

# Circular plot of species
def loyalty():
    col = 'Loyalty'
    characters = pd.read_csv("../Dataset/Characters.csv")
    df = pd.DataFrame(characters)
    labels = df[col].unique()
    count = df[col].value_counts()
    biggest_group = {'Order of the Phoenix':0, 'Lord Voldemort':0, "Dumbledore's Army":0, 'Ministry of Magic':0, 'Hogwarts School of Witchcraft and Wizardry':0}
    for group in biggest_group.keys():
        c = 0
        for l in labels:
            if pd.notna(l):
                if group in l:
                    c += count[l]
        biggest_group[group] = c
    count_serie = pd.Series(biggest_group.values())
    plt.figure(figsize=(fig_sizes[0], fig_sizes[1]))
    ax = count_serie.plot(kind='bar')
    ax.set_title("Loyalty group sizes", fontsize=fontsize)
    ax.set_xlabel("Loyalty", fontsize=fontsize)
    ax.set_ylabel("Number", fontsize=fontsize)
    ax.set_xticklabels(biggest_group.keys(), rotation=5, fontsize=fontsize)
    ax.yaxis.label.set_size(fontsize)
    plt.yticks(fontsize=fontsize)
    plt.savefig('../Figs/loyalty.png')
    # fig, ax = plt.subplots()
    # ax.pie(sizes, labels=biggest_group)
    # ax.axis('equal')
    # plt.show()


def words_in_books():
    book_list = ['1', '2', '3', '4', '5', '6', '7']
    allLines = []
    for nb in book_list:
        with open('../Dataset/Books/Book'+nb+'.txt', 'r') as book:
            lines = book.read().splitlines()
            allLines += lines
    with open('../Dataset/Books/stop_words_english.txt', 'r') as stop_words_english:
        stop_words = stop_words_english.read().splitlines()
    words = [w for segments in allLines for w in segments.split() if not segments.startswith('Page | ')
                                                                    and not w in stop_words]
    new_words = []
    punctuation = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~0123456789—|'''
    for i, word in enumerate(words):
        new_word = ""
        for char in word:
            if char not in punctuation:
                new_word += char
        if new_word != "" and len(new_word) > 3:
            new_words.append(new_word)
    wordsSet = set(new_words)
    wordsCounter = Counter(new_words)
    wordsCounter  = {k: v for k, v in sorted(wordsCounter.items(), key=lambda item: item[1], reverse=True)}

    number_to_plot = 20
    count_serie = pd.Series(list(wordsCounter.values())[:number_to_plot])
    plt.figure(figsize=(fig_sizes[0], fig_sizes[1]))
    ax = count_serie.plot(kind='bar')
    ax.set_title("Words in all books", fontsize=fontsize)
    ax.set_xlabel("Words", fontsize=fontsize)
    ax.set_ylabel("Number", fontsize=fontsize)
    ax.set_xticklabels(list(wordsCounter.keys())[:number_to_plot], rotation=20, fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.savefig('../Figs/words_counter.png')

plot_nbChar_houses()
loyalty()
words_in_books()
plt.show()


