# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/b76b2acb-c4f7-4cb1-80cc-7b66506f8aed


# Main Function of text_processing.py:
# Pass in a text file from user input and separate every word and remove all punctuation in the words
# Finally, return a sorted list of all the words in the text file.
import string
word_list = []
def text_processor(text_choice):
    with open(text_choice, "r", encoding="UTF-8-sig") as file:
        for line in file:
            for word in line.split():
                translation_table = word.maketrans(dict.fromkeys(string.punctuation + '—“”’‘'))
                word2 = word.translate(translation_table)
                word2 = word2.lower()
                if word2 == "":
                    pass
                else:
                    word_list.append(word2)
        word_list.sort()
        return word_list