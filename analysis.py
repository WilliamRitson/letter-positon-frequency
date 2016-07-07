from tabulate import tabulate
import os


def sum_letter_in_nth(words, letter, n):
    total = 0
    for word in words:
        if n < len(word) and word[n] == letter:
            total += 1
    return total

alphabet = 'abcdefghijklmnopqrstvwxyz'
dictonary_folder_path = './dicts'
dictonary_folder = os.listdir(dictonary_folder_path)

for dictionary_path in dictonary_folder:
    words = open(dictonary_folder_path + '/' +
                 dictionary_path).read().split('\n')
    header = ['Position'] + list(alphabet.upper())
    table = [[i + 1] + [sum_letter_in_nth(words, letter, i)
                        for letter in alphabet] for i in xrange(20)]
    open('./results/' + dictionary_path + '_results.txt',
         'w').write(tabulate(table, headers=header, tablefmt='orgtbl'))
