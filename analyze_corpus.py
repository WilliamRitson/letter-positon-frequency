from count_words_in_corpus import read_word_counts
from letter_counting import create_letter_table, sum_letter_frequency_in_nth, write_letter_table_as_csv
import csv

output_filename = 'results/corpus-analysis.csv'
word_counts = read_word_counts()
table = create_letter_table(word_counts, sum_letter_frequency_in_nth)

write_letter_table_as_csv(table, output_filename)
