# Student Name: Ayush Singh
# Course: CS 3035-01

import random

initial_pile = random.randint(10, 100)
turn_selector = random.randint(0, 1)
cpu_iq = random.randint(0, 1)


def stupid_cpu(initial_pile):
    cpu_move = random.randint(1, int(initial_pile / 2))
    rule_check = cpu_move
    while rule_check > initial_pile/2:
        cpu_move = random.randint(1, int(initial_pile / 2))
        rule_check = cpu_move
    if rule_check <= initial_pile/2:
        print("CPU Move: " + str(cpu_move))
        initial_pile = initial_pile - cpu_move
        return initial_pile

def smart_cpu(initial_pile):
    smart_moves = [63, 31, 15, 7, 3]
    loop = True

    if(initial_pile < 6):
        random_move = random.randint(1, 3)
        while random_move > initial_pile / 2:
            random_move = random.randint(1, 3)
        print("CPU Move: " + str(random_move))
        initial_pile = initial_pile - random_move
        print("Remaining Marbles: " + str(initial_pile))
        return initial_pile

    for i in range(0, len(smart_moves)):
        if(smart_moves[i] <= (initial_pile / 2) and loop == True):
            difference = initial_pile - smart_moves[i]
            rule_check = difference
            loop = False
            if difference > initial_pile / 2:
                difference = initial_pile - smart_moves[i - 1]
            print("CPU Move: " + str(difference))
            initial_pile = initial_pile - difference
            print("Remaining Marbles: " + str(initial_pile))
            return initial_pile

def player_move(initial_pile):
    player_move = int(input("What Is Your Move: "))
    rule_check = player_move
    if(initial_pile == 1):
        return 0
    while rule_check > initial_pile/2:
        player_move = int(input("Try Again: "))
        rule_check = player_move
    if rule_check <= initial_pile/2:
        initial_pile = initial_pile - player_move
        return initial_pile

while initial_pile > 0:
    # Dumb CPU goes first
    if(turn_selector == 0 and cpu_iq == 0):
        print("The Stupid CPU Goes First")
        print("Total Marbles: " + str(initial_pile))
        if initial_pile > 1:
            initial_pile = stupid_cpu(initial_pile)
            print("Remaining Marbles: " + str(initial_pile))
            initial_pile = player_move(initial_pile)
            if(initial_pile == 0):
                print("YOU LOST")
        else:
            cpu_move = 1
            print("CPU Move: " + str(cpu_move))
            initial_pile = initial_pile - cpu_move
            print("Remaining Marbles: " + str(initial_pile))
            print("CPU LOST")

    elif(turn_selector == 1 and cpu_iq == 0):
        print("You Go First Against A Stupid CPU")
        print("Total Marbles: " + str(initial_pile))
        if initial_pile > 1:
            initial_pile = player_move(initial_pile)
            print("Remaining Marbles: " + str(initial_pile))
            if (initial_pile == 1):
                cpu_move = 1
                print("CPU Move: " + str(cpu_move))
                initial_pile = initial_pile - cpu_move
                print("Remaining Marbles: " + str(initial_pile))
                print("CPU LOST")
            if(initial_pile > 1):
                initial_pile = stupid_cpu(initial_pile)
        else:
            cpu_move = 1
            initial_pile = player_move(initial_pile)
            print("Remaining Marbles: " + str(initial_pile))
            print("YOU LOST")

    # Smart CPU Goes First
    elif(turn_selector == 0 and cpu_iq == 1):
        print("Smart CPU Goes First")
        print("Total Marbles: " + str(initial_pile))
        if initial_pile > 1:
            initial_pile = smart_cpu(initial_pile)
            initial_pile = player_move(initial_pile)
            print("Remaining Marbles: " + str(initial_pile))
            if(initial_pile == 0):
                print("YOU LOST")
        else:
            cpu_move = 1
            print("CPU Move: " + str(cpu_move))
            initial_pile = initial_pile - cpu_move
            print("Remaining Marbles: " + str(initial_pile))
            print("CPU LOST")
    elif(turn_selector == 1 and cpu_iq == 1):
        print("You Go First Against A Smart CPU")
        print("Total Marbles: " + str(initial_pile))
        if initial_pile > 1:
            initial_pile = player_move(initial_pile)
            print("Remaining Marbles: " + str(initial_pile))
            if (initial_pile == 1):
                cpu_move = 1
                print("CPU Move: " + str(cpu_move))
                initial_pile = initial_pile - cpu_move
                print("Remaining Marbles: " + str(initial_pile))
                print("CPU LOST")
            if(initial_pile > 1):
                initial_pile = smart_cpu(initial_pile)
        else:
            initial_pile = player_move(initial_pile)
            print("Remaining Marbles: " + str(initial_pile))
            print("YOU LOST")

