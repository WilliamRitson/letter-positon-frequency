import csv

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
MAX_LETTER_POSITION = 12
A_VALUE = ord('a')

def is_letter_in_nth_position(word, letter, n):
    return n < len(word) and word[n] == letter

def create_letter_table(word_list, max_letter_position=MAX_LETTER_POSITION):
    """
    Uses a list of words to create a table with each letter of the alphabet
    followed by that letters frequency at the nth position in the list
    """
    header = ['Position'] + list(ALPHABET.upper())
    table = []
    for _ in range(max_letter_position):
        table.append([])
        for _ in ALPHABET:
            table[-1].append(0)

    for word, count in word_list:
        for letter_positon, letter in list(enumerate(word))[:max_letter_position]:
            letter_index = ord(letter) - A_VALUE
            if (letter_index >= 0 and letter_index < 26):
                table[letter_positon][letter_index] += count

    for i, row in enumerate(table):
        table[i] = [i + 1] + row
    return [header] + table

def write_letter_table_as_csv(letter_table, filename):
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in letter_table:
            csv_writer.writerow(row)