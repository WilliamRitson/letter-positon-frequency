from letter_counting import ALPHABET, create_letter_table, write_letter_table_as_csv
import urllib.request
import gzip
from collections import Counter
import fnmatch
import os
import codecs
import csv
import itertools

BASE_URL = 'http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-{}.gz'
NGRAM_DIR = 'ngram'


def download_one_grams():
    for letter in ALPHABET:
        print('Download ngram for', letter)
        urllib.request.urlretrieve(BASE_URL.format(letter),
                           'ngram/{}.gz'.format(letter))


def get_ngram_files():
    gz_files = []
    for root, dirnames, filenames in os.walk(NGRAM_DIR):
        for filename in fnmatch.filter(filenames, '*.gz'):
            gz_files.append(os.path.join(root, filename))
    return gz_files


def check_for_files():
    return len(get_ngram_files()) >= len(ALPHABET)


def process_one_grams(min_year, max_year):
    for gz_file in get_ngram_files():
        print('read from', gz_file)
        opened_file = gzip.open(
            gz_file, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None)
        line_num = 0
        for line in opened_file:
            tokens = line.decode('utf-8').split('\t')
            word = tokens[0].lower()
            year = int(tokens[1])
            count = int(tokens[2])

            if year >= min_year and year <= max_year:
                yield word, count

if __name__ == '__main__':
    if not check_for_files():
        download_one_grams()
    
    generator = process_one_grams(2006, 2006)
    output_filename = 'results/ngrams-analysis.csv'
    table = create_letter_table(generator)

    write_letter_table_as_csv(table, output_filename)
