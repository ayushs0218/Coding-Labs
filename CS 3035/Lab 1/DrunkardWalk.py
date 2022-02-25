# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01

import random

n = int(input("How Many Intersections Does The Drunkard Walk Over: "))

x = 0
y = 0
print("Drunkard Original Position: (" + str(x) + ", " + str(y) + ")" )
for i in range(1, n+1):
    random_position = random.randint(0, 3)

    print("Move #" + str(i))
    if(random_position == 0):
        x = x - 1
        print("Drunkard Moved Left")
    elif(random_position == 1):
        x = x + 1
        print("Drunkard Moved Right")

    elif(random_position == 2):
        y = y - 1
        print("Drunkard Moved Down")
    elif(random_position == 3):
        y = y + 1
        print("Drunkard Moved Up")

    print("Drunkard Position: (" + str(x) + ", " + str(y) + ")" )