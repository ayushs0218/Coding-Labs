# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/b76b2acb-c4f7-4cb1-80cc-7b66506f8aed

# Main Function of main.py:
# Run the methods from the other .py files directly

import time
import text_processing
import list_histogram
import dictionary_histogram

def main():
    last_four = ""
    while last_four != ".txt":
        text_choice = input("What Is Your Text File: (Please Include '.txt'):")
        last_four = text_choice[-4:]
        if last_four != ".txt":
            print("Try Again With A File With '.txt' at the end ")
    l1 = text_processing.text_processor(text_choice)

    list_start = time.time()
    list_histogram.list_count(l1)
    list_end = time.time()

    for i in list_histogram.list_count(l1):
        print(i)

    dict_start = time.time()
    dictionary_histogram.dictionary_count(l1)
    dict_end = time.time()

    for key, value in dictionary_histogram.dictionary_count(l1).items():
        print(key, ':', value)

    print("List Runtime: " + str(list_end - list_start) + " seconds")
    print("List Word Count: " + str(len(list_histogram.list_count(l1))))
    print("Dictionary Runtime " + str(dict_end - dict_start) + " seconds")
    print("Dictionary Word Count: " + str(len(dictionary_histogram.dictionary_count(l1))))

if __name__ == "__main__":
    main()