import pandas

nato_alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dic = { row.letter:row.code for (index, row) in nato_alphabet_data_frame.iterrows() }

word = input("Enter a word: ")
letters = [letter for letter in word.upper()]
phonetic_codes = [nato_alphabet_dic[letter] for letter in letters]
print(phonetic_codes)
