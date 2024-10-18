import random
import tkinter as tk

root = tk.Tk()
root.title("apps")



    

while True:
    

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Joins the randomized letters
    letters1 = random.sample(letters,nr_letters)
    selected_items = letters1[:nr_letters]
    #Joins the randomized numbers
    numbers_1 = random.sample(numbers,nr_numbers)
    selected_numbers = numbers_1[:nr_numbers]
    #Joins the randomized Symbols
    symbols_1 = random.sample(symbols,nr_symbols)
    selected_symbols = symbols_1[:nr_symbols]

    added_inputs= nr_letters + nr_symbols + nr_numbers

    pass_word = "".join(selected_items) + "".join(selected_numbers) + "".join(selected_symbols)
    pass_word_scrambled = random.sample(pass_word, added_inputs)

    print("Your password is")
    print("".join(pass_word_scrambled))
    

root.mainloop()
    





