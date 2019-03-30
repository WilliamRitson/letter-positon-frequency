from letter_counting import  create_letter_table, write_letter_table_as_csv
import csv
import os

dictonary_folder_path = 'dicts'
dictonary_folder = os.listdir(dictonary_folder_path)

for dictionary_path in dictonary_folder:
    input_filename = '{}/{}'.format(dictonary_folder_path, dictionary_path)
    output_filename = 'results/{}_results.csv'.format(dictionary_path)

    words = open(input_filename).read().split('\n')
    word_counts = [[word, 1] for word in words]
    table = create_letter_table(word_counts)

    write_letter_table_as_csv(table, output_filename)
