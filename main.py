from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

english = None
french = None
random_word = {}
try:
    data = pandas.read_csv("C:/Users/Abdul Ahad/Naag/flash-card-project-start/data/Remaining_Words.csv")
except FileNotFoundError:
    data = pandas.read_csv("C:/Users/Abdul Ahad/Naag/flash-card-project-start/data/french_words.csv")
    my_list = data.to_dict(orient="records")
else:
    my_list = data.to_dict(orient="records")



def next_card():
    global english, french, card_flip, random_word
    window.after_cancel(card_flip)
    random_word = random.choice(my_list)
    english = random_word["English"]
    french = random_word["French"]
    canvas.itemconfig(title, text= "French", fill = "black")
    canvas.itemconfig(word, text= french, fill = "black")
    canvas.itemconfig(canvasimage , image = front_image)
    card_flip = window.after(3000, flipcard)

def flipcard():
    global english
    canvas.itemconfig(canvasimage, image= back_image)
    canvas.itemconfig(title, text= "english", fill="white")
    canvas.itemconfig(word, text= english,  fill = "white")

def knows():
    global random_word
    my_list.remove(random_word)
    data = pandas.DataFrame(my_list)
    data.to_csv("./data/Remaining_Words.csv", index= False)
    next_card()


window = Tk()
window.title("Flash Card Learning")
window.config(bg = BACKGROUND_COLOR, padx=50, pady= 50)
card_flip = window.after(3000, flipcard)
tick_image = PhotoImage(file ="C:/Users/Abdul Ahad/Naag/flash-card-project-start/images/right.png")
cross_image = PhotoImage(file ="C:/Users/Abdul Ahad/Naag/flash-card-project-start/images/wrong.png")
back_image = PhotoImage(file= "C:/Users/Abdul Ahad/Naag/flash-card-project-start/images/card_back.png")
front_image = PhotoImage(file= "C:/Users/Abdul Ahad/Naag/flash-card-project-start/images/card_front.png")
canvas = Canvas()
canvas.config(height= 526, width=800, highlightthickness=0, bg= BACKGROUND_COLOR)
canvasimage = canvas.create_image(400, 263, image= front_image)
title = canvas.create_text(400,130, text="", font= ("Ariel", 20))
word = canvas.create_text(400,263, text="", font= ("Ariel",30, "italic bold"))
canvas.grid(row = 0, column= 0, columnspan=2)
tick = Button(image= tick_image, highlightthickness=0, bg=BACKGROUND_COLOR, command= knows)
tick.grid(row = 1, column= 0)
cross = Button(image= cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command= next_card)
cross.grid(row = 1, column= 1)
next_card()
window.mainloop()