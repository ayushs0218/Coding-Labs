import tkinter
import tkinter as tk
import tkinter.font
from tkinter import *


def card_length_validator(card):
    if len(card) >= 13 and len(card) <= 16:
        return True
    else:
        return False


def industry_finder(card):
    if card[0:2] == "37":
        return "American Express"
    elif card[0] == "6":
        return "Discover Card"
    elif card[0] == "5":
        return "Master Card"
    elif card[0] == "4":
        return "Visa Card"
    else:
        return "Invalid Card"


def even_digit_calculator(card):
    rev_card = card[::-1]
    second_digit_sum = 0
    for num in range(1, len(rev_card), 2):
        # print("Evens: ", rev_card[num])
        if int(rev_card[num]) * 2 < 10:
            second_digit_sum += int(rev_card[num]) * 2
        else:
            tens = (int(rev_card[num]) * 2) // 10
            ones = (int(rev_card[num]) * 2) % 10
            second_digit_sum += (tens + ones)
    return second_digit_sum


def odd_digit_calculator(card):
    rev_card = card[::-1]
    first_digit_sum = 0
    for num in range(0, len(rev_card), 2):
        # print("Odds", rev_card[num])
        print(rev_card[num])
        first_digit_sum += int(rev_card[num])
    return first_digit_sum


def luhn_checker(even_values, odd_values):
    print(even_values)
    print(odd_values)
    if (even_values + odd_values) % 10 == 0:
        return "This Card Is Valid"
    else:
        return "This Card Is Invalid"


def card_type_result(event):
    if card_length_validator(entry.get()) == True:
        res.configure(text="Card Type (Industry): " + str(industry_finder(entry.get())))
    else:
        res.configure(text="Invalid Card")


def card_validity_result():
    even_values = even_digit_calculator(entry.get())
    odd_values = odd_digit_calculator(entry.get())
    if card_length_validator(entry.get()) == True and industry_finder(entry.get()) != "Invalid Card":
        res.configure(font=("Comic Sans MS", 12, "bold"), text="Card Type: " + str(industry_finder(entry.get())) + ", Card Validity: " + str(luhn_checker(even_values, odd_values)))

    else:
        res.configure(text="Invalid Card Length")


w = tk.Tk(className=" Card Validator")

w.geometry("600x200")
w['background']='#A4bdf3'

# logo = Image.open("card_validator_logo.png")
# test = ImageTk.PhotoImage(logo)

# tk.Label(w, text="Card Number:").pack()
prompt = Label(w, text="Enter Your Card Number:", bg="#A4bdf3", font=("Comic Sans MS", 20, "bold")).pack()
prompt2 = Label(w, text="(Click Submit To Enter Your Card Number)", bg="#A4bdf3", font=("Comic Sans MS", 15, "bold")).pack()
entry = tk.Entry(w, width=20, font=("Comic Sans MS", 15, "bold"))
# entry.bind("<Return>", card_validity_result)
entry.pack()
res = tk.Label(w, bg="#A4bdf3")
res.pack()
button = tkinter.Button(w, text="Submit",font=("Comic Sans MS", 10, "bold"), command = card_validity_result).pack()
# button.pack()
w.mainloop()
