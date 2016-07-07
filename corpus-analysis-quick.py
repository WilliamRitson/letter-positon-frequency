from tabulate import tabulate
from collections import Counter
import codecs
import pickle


def sum_letter_in_nth(word_counts, letter, n):
    total = 0
    for word in word_counts:
		print word, word_counts[word]
		if n < len(word) and word[n] == letter:
			total += word_counts[word]

    return total

alphabet = 'abcdefghijklmnopqrstvwxyz'
corpus_path = './corpus'

results = codecs.open('./results/counter', 'r', 'utf-8-sig')
word_counts = pickle.load(results)

header = ['Position'] + list(alphabet.upper())
table = [[i + 1] + [sum_letter_in_nth(word_counts, letter, i)
                    for letter in alphabet] for i in xrange(20)]

open('./results/corpus_results.txt',
     'w').write(tabulate(table, headers=header, tablefmt='orgtbl'))
print('done')
