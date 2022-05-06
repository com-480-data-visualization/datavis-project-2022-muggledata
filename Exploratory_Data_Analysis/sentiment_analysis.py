import matplotlib.pyplot as plt
import pandas as pd

# load sentiment datasets
positive_words = pd.DataFrame(pd.read_csv('./../Dataset/positive_words.csv'))
negative_words = pd.DataFrame(pd.read_csv('./../Dataset/negative_words.csv'))

# book_list = ['1', '2', '3', '4', '5', '6', '7']
book_list = ['7']
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

counter = 0


total_counter = []
for i, word in enumerate(new_words):
    if word in positive_words.values:
        counter+=1
    elif word in negative_words.values:
        counter-=1

    # total_counter.append(counter)
    if i%3000 == 0 and i != 0:
        total_counter.append(counter)
        counter = 0



plt.plot(total_counter)
plt.show()


