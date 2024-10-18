import random
import tkinter as tk

root = tk.Tk()
root.title("apps")
root.geometry("500x500")

    
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    try:
        nr_letters = int(letters_input.get())
        nr_symbols = int(symbols_Input.get())
        nr_numbers = int(numbers_input.get())
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

        result_lable.config(text=f"Your password is: {''.join(pass_word_scrambled)}")

        

    except ValueError:
        messagebox.showwarning("Input Error", "Please enter valid numbers.")


tk.Label(root, text ="letters").grid(row=0,column=0,padx=0,pady=0)  
letters_input = tk.Entry(root, width=5) 
letters_input.grid(row=0, column=1, padx= 10, pady= 5 ) 

tk.Label(root, text="numbers").grid(row=1, column=0,padx=0,pady=5)
numbers_input =tk.Entry(root, width= 5)
numbers_input.grid(row=1,column=1)

tk.Label(root, text="Symbols").grid(row=2,column=0,padx=0,pady=0)
symbols_Input = tk.Entry(root, width=5)
symbols_Input.grid(row=2,column=1)

btn = tk.Button(text="hi", command= generate_password)
btn.grid(row=0,column=3)

result_lable = tk.Label(root, text="",)
result_lable.grid(row=4, column=1, columnspan=2)


    

root.mainloop()
    
