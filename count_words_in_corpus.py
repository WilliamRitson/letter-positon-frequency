from collections import Counter
import nltk
import fnmatch
import os
import codecs
import csv

# nltk.download()

DEFAULT_CORPUS_PATH = 'D:/data/english/corpus/OANC-GrAF/data'
DEFAULT_WORD_COUNTS_OUTPUT = 'results/word_counts.csv'

def create_word_count(corpus_path=DEFAULT_CORPUS_PATH):
    text_files = []
    for root, dirnames, filenames in os.walk(corpus_path):
        for filename in fnmatch.filter(filenames, '*.txt'):
            text_files.append(os.path.join(root, filename))
    
    word_counts = Counter()
    for file_path in text_files:
        text = codecs.open(file_path, 'r', 'utf-8-sig').read().lower()
        tokens = nltk.word_tokenize(text)
        word_counts.update(tokens)
        print('reading tokens from', file_path)
    
    write_word_counts(word_counts)

def write_word_counts(word_counts, word_count_filename=DEFAULT_WORD_COUNTS_OUTPUT):
    with open(word_count_filename, 'w', newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for word, count in word_counts.most_common():
            csv_writer.writerow([word, count])

def read_word_counts(word_count_filename=DEFAULT_WORD_COUNTS_OUTPUT):
    try:
        with open(word_count_filename, 'r',  encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result = {}
            for row in reader:
                result[row[0]] = int(row[1])
            return result
    except:
        return None

