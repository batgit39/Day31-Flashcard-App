from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"

card = {}
french_words = {}
try:
    cached_data = pandas.read_csv("./data/french_words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    french_words = data.to_dict(orient = "records")
    # with open("./data/french_words.csv", "w") as data_file:
        
    # data = pandas.read_csv("./data/french_words.csv")
else:
    french_words = cached_data.to_dict(orient = "records") 


def random_word():
    global card 
    card = random.choice(french_words)

def next_card_generator():
    random_word()
    canvas.itemconfig(main_img, image = img_card_front) 
    canvas.itemconfig(title, text = "French", fill = "black")
    canvas.itemconfig(word, text = card['French'], fill = "black")
    window.after(3000, func = card_flipper)

def card_flipper():
    canvas.itemconfig(main_img, image = img_card_back) 
    canvas.itemconfig(title, text = "English", fill="white")
    canvas.itemconfig(word, text = card['English'], fill="white")

def correct_answer():
    french_words.remove(card)
    words_left = pandas.DataFrame(french_words)
    words_left.to_csv("./data/french_words_to_learn.csv", index = False)
    next_card_generator()


window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

canvas = Canvas(width = 800, height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)
img_card_front = PhotoImage(file = "./images/card_front.png")
img_card_back = PhotoImage(file = "./images/card_back.png")
main_img = canvas.create_image(400,263, image = img_card_front)
canvas.grid(row = 0, column = 0, columnspan = 2, rowspan = 2)
title = canvas.create_text(400, 150, text = "", font = ("Ariel", 40 , "italic"))
word = canvas.create_text(400, 263, text = "", font = ("Ariel", 60 , "bold"))

next_card_generator() # calling function to display on start

img_right = PhotoImage(file = "./images/right.png")
button_right = Button(image=img_right, highlightthickness=0, command = correct_answer)
button_right.grid(row = 3, column = 1)

img_wrong = PhotoImage(file = "./images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command = next_card_generator)
button_wrong.grid(row = 3, column = 0)

window.mainloop()
