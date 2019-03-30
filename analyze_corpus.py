from count_words_in_corpus import read_word_counts
from letter_counting import create_letter_table, write_letter_table_as_csv
import csv

output_filename = 'results/corpus-analysis.csv'
word_counts = read_word_counts()
table = create_letter_table(word_counts, max_letter_position=20)

write_letter_table_as_csv(table, output_filename)
