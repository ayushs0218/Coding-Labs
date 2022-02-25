# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/b76b2acb-c4f7-4cb1-80cc-7b66506f8aed


# Main Function of list_histogram.py:
# Create tuples that represent each word in a text file along with the duplication of each word,
# then store all the tuples in a list
def list_count(input_list):
    tuple_list = []
    duplicates = 1
    for index in range(len(input_list)):
        if index == 0:
            tuple = (input_list[index], duplicates)
            tuple_list.append(tuple)
        elif index != 0 and input_list[index] == input_list[index - 1]:
            duplicates = duplicates + 1
            t_List = list(tuple)
            t_List[1] = duplicates
        elif index != 0 and input_list[index] != input_list[index - 1]:
            tuple_list.append((input_list[index], duplicates))
            duplicates = 1
    return tuple_list