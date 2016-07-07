from tabulate import tabulate
from collections import Counter
import nltk
import fnmatch
import os
import codecs
import pickle

#nltk.download()

def sum_letter_in_nth(word_counts, letter, n):
    total = 0
    for word in word_counts:
        if n < len(word) and word[n] == letter:
            total += word_counts[word]
    return total

alphabet = 'abcdefghijklmnopqrstvwxyz'
corpus_path = '.\corpus'

matches = []
for root, dirnames, filenames in os.walk(corpus_path):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))

word_counts = Counter()
for file_path in matches:
    text = codecs.open(file_path, 'r', 'utf-8-sig').read().lower()
    tokens = nltk.word_tokenize(text)
    word_counts.update(tokens)
    print 'reading tokens from', file_path

header = ['Position'] + list(alphabet.upper())
table = [[i + 1] + [sum_letter_in_nth(word_counts, letter, i)
                    for letter in alphabet] for i in xrange(20)]
pickle.dump(word_counts, open('./results/counter', 'w'))
open('./results/corpus_results.txt',
     'w').write(tabulate(table, headers=header, tablefmt='orgtbl'))
print('done')
