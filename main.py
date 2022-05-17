import random
from tkinter import *
import pandas

word = []
BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_TEXT = ("Arial", 40, "bold")

dictionary_word = pandas.read_csv("data/french_words.csv")
list_of_word = dictionary_word.to_dict(orient="records")


class Correct:

    def __init__(self):
        self.list_words = random.choice(list_of_word)
        self.render_random_word()

    def render_random_word(self):
        global flip_timer
        window.after_cancel(flip_timer)
        french_words = self.list_words["French"]
        canvas.itemconfig(word_title, text="French", fill="Black")
        canvas.itemconfig(word_text, text=french_words, fill="Black")
        canvas.itemconfig(canvas_image, image=canvas_photo_front)
        flip_timer = window.after(3000, func=self.flip_card)

    def flip_card(self):
        english_words = self.list_words["English"]
        canvas.itemconfig(canvas_image, image=canvas_photo_back)
        canvas.itemconfig(word_title, text="English", fill="White")
        canvas.itemconfig(word_text, text=english_words, fill="White")
        window.after(3000, self.__init__)

    def right(self):
        list_of_word.remove(self.list_words)
        list_word_Data_Frame = pandas.DataFrame(list_of_word)
        list_word_Data_Frame.to_csv("data/french_words.csv", index=False)
        self.__init__()


window = Tk()
window.title("flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, Correct.flip_card)

# Canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
canvas_photo_front = PhotoImage(file="images/card_front.png")
canvas_photo_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(410, 270, image="")
word_title = canvas.create_text(400, 150, text="", font=FONT_TITLE)
word_text = canvas.create_text(400, 263, text="", font=FONT_TEXT)
canvas.grid(column=0, row=0, columnspan=2)

# Button
right_photo = PhotoImage(file="images/right.png")
right_button = Button(image=right_photo, highlightthickness=0, command=Correct().right)
right_button.grid(column=1, row=1)

wrong_photo = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_photo, highlightthickness=0, command=Correct().render_random_word)
wrong_button.grid(column=0, row=1)

Correct()
window.mainloop()
