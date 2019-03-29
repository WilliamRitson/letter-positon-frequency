import csv

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
MAX_LETTER_POSITION = 12

def sum_letter_in_nth(words, letter, n):
    """
    Counts the number of words in the words list where the letter appears at the nth index
    """
    total = 0
    for word in words:
        if n < len(word) and word[n] == letter:
            total += 1
    return total


def sum_letter_frequency_in_nth(word_counts, letter, n):
    """
    Counts the number of words in the words list where the letter appears at the nth index 
    then multiplies that by the frequency of the letter in the corpus.
    """
    total = 0
    for word in word_counts:
        if n < len(word) and word[n] == letter:
            total += word_counts[word]

    return total


def create_letter_table(word_list, count_function, max_letter_position=MAX_LETTER_POSITION):
    """
    Uses a list of words to create a table with each letter of the alphabet
    followed by that letters frequency at the nth position in the list
    """
    header = ['Position'] + list(ALPHABET.upper())
    table = [header]
    for letter_position in range(max_letter_position):
        one_index = letter_position + 1
        letter_frequencies = [count_function(
            word_list, letter, letter_position) for letter in ALPHABET]
        table.append([one_index] + letter_frequencies)
    return table

def write_letter_table_as_csv(letter_table, filename):
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in letter_table:
            csv_writer.writerow(row)