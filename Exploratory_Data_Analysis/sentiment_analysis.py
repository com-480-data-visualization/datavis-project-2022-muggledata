import json
import math
import matplotlib.pyplot as plt
from numpy import maximum
import pandas as pd

# load sentiment datasets
positive_words = pd.DataFrame(pd.read_csv('./../Dataset/positive_words.csv'))
negative_words = pd.DataFrame(pd.read_csv('./../Dataset/negative_words.csv'))

book_list = ['1', '2', '3', '4', '5', '6', '7']

def getSentimentCounter(allLines):
    with open('../Dataset/Books/stop_words_english.txt', 'r') as stop_words_english:
        stop_words = stop_words_english.read().splitlines()
    words = []
    for segments in allLines:
        i = 0
        if segments.startswith('Page | '):
            words.append("THISISAPAGE")
        for w in segments.split():
            if not w in stop_words:
                words.append(w)
                
    new_words = []
    punctuation = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~0123456789—|'''
    page_number = 0
    for i, word in enumerate(words):
        new_word = ""
        for char in word:
            if char not in punctuation:
                new_word += char
        if new_word == "THISISAPAGE":
            page_number += 1
        if new_word != "" and len(new_word) > 3:
            new_words.append(new_word)

    counter = 0
    page_counter = 0
    total_counter = []
    for i, word in enumerate(new_words):
        if word in positive_words.values:
            counter+=1
        elif word in negative_words.values:
            counter-=1

        if word == "THISISAPAGE":
            page_counter += 1

        if page_counter == int(page_number / 10):
            total_counter.append(counter)
            counter = 0
            page_counter = 0

    minimum = min(total_counter)
    maximum = max(total_counter)
    return [round(100*(c-minimum)/(maximum-minimum)) - 50 for c in total_counter]

j = []
for nb in book_list:
    allLines = []
    with open('../Dataset/Books/Book'+nb+'.txt', 'r') as book:
        lines = book.read().splitlines()
        allLines += lines
    counters = getSentimentCounter(allLines)
    print(counters)
    book = {
        "book": "Book "+nb,
        "data": []
    }
    for i in range(len(counters)):
        book["data"].append({
            "part": "Part "+str(i+1),
            "count": counters[i],
            "description": None
        })
    j.append(book)

with open('../Dataset/sentiment_analysis.json', 'w') as outfile:
    outfile.write(json.dumps(j, indent=4))


