from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
BACK_CARD_COLOR = "#91c2af"

# languagedata
if os.path.isfile("./data/words_to_learn.csv"):
    languagedata = pd.read_csv("./data/words_to_learn.csv")
    language_dict = languagedata.to_dict("records")
else:
    languagedata = pd.read_csv("./data/french_words.csv")
    language_dict = languagedata.to_dict("records")


# functions
# generate random word
def know_word():
    global word
    global language_dict
    new_dict = [i for i in language_dict if not (i["French"] == word["French"])]
    language_dict = new_dict
    df = pd.DataFrame.from_records(language_dict)
    df.to_csv("./data/words_to_learn.csv", index=False)
    generate_word()


def generate_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    flashcard.itemconfig(flashcard_front, image=flashcard_front_img)
    word = random.choice(language_dict)
    input_label.config(text=word["French"], bg="white")
    language_label.config(text="French", bg="white")
    window.after(3000, flip_card)


def flip_card():
    flashcard.itemconfig(flashcard_front, image=flashcard_back_img)
    input_label.config(text=word["English"], bg=BACK_CARD_COLOR)
    language_label.config(text="English", bg=BACK_CARD_COLOR)


# window
window = Tk()
window.title("PahlawanJoey's Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# flashcard
flashcard_back_img = PhotoImage(file="./images/card_back.png")
flashcard_front_img = PhotoImage(file="./images/card_front.png")
flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = flashcard.create_image(400, 263, image=flashcard_front_img)
flashcard.grid(column=0, row=0, columnspan=2)
# buttons
button_right = PhotoImage(file="./images/right.png")
button = Button(image=button_right, highlightthickness=0, bg=BACKGROUND_COLOR, command=know_word)
button.grid(column=1, row=1)
button_wrong = PhotoImage(file="./images/wrong.png")
button = Button(image=button_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_word)
button.grid(column=0, row=1)
# textlabels
input_label = Label(text="Word", bg="white", font=("Arial", 60, "bold"))
input_label.grid(column=0, row=0, columnspan=2)
language_label = Label(text="Language", bg="white", font=("Arial", 40, "italic"))
language_label.grid(column=0, row=0, columnspan=2, sticky="n", pady=90)
# loop to change cards
flip_timer = window.after(3000, flip_card)
generate_word()

# call function to refresh card on start

window.mainloop()
