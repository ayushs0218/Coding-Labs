# # Student Name: Ayush Singh
# # CIN: 306692040
# # Course: CS 3035-01
#
# def perfect_number_finder(numbers):
#     sum = 0
#     perfect_number_list = []
#     for number_index in range(6, numbers + 1):
#         for divisor_index in range(1, number_index + 1):
#             if (number_index % divisor_index == 0 and number_index/divisor_index != number_index):
#                 sum = sum + int(number_index/divisor_index)
#                 if(sum == number_index and number_index / divisor_index == 1):
#                     perfect_number_list.append(number_index)
#                 if (number_index / divisor_index == 1):
#                     sum = 0
#     return perfect_number_list
#
# numbers = int(input("Find Perfect Numbers Up To: "))
# print("Perfect Numbers: " + str(perfect_number_finder(numbers)))
x = 1058
def f():
    global x
    x = 100
    x = 78

f()
print(x)