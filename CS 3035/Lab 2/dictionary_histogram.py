# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/b76b2acb-c4f7-4cb1-80cc-7b66506f8aed


# Main Function of dictionary_histogram:
# Populate a dictionary with each independent word and duplication of the word as key, value respectively.
def dictionary_count(input_list):
    dictionary = {}
    duplicates = 1
    for index in input_list:
        if index in dictionary:
            duplicates = duplicates + 1
            dictionary[index] = duplicates
        else:
            dictionary[index] = 1
            duplicates = 1
    return dictionary
