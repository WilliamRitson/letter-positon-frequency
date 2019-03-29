from letter_counting import sum_letter_in_nth, create_letter_table, write_letter_table_as_csv
import csv
import os

dictonary_folder_path = 'dicts'
dictonary_folder = os.listdir(dictonary_folder_path)

for dictionary_path in dictonary_folder:
    input_filename = '{}/{}'.format(dictonary_folder_path, dictionary_path)
    output_filename = 'results/{}_results.csv'.format(dictionary_path)

    words = open(input_filename).read().split('\n')
    table = create_letter_table(words, sum_letter_in_nth)

    write_letter_table_as_csv(output_filename, table)
