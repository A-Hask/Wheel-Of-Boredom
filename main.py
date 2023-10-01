from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk,Image

root = Tk()
root.title("WHEEL! OF! BOREDOM!")
# root.iconbitmap('C:/Users/User/Documents/IvyTech/Fall2023/SDEV140-11P/Final-Project/Wheel-Of-Boredom/images')

# icon=ImageTk.PhotoImage(Image.open("wheel.png"))

# Widgets
welcome = Label(root, text="Welcome to the")
title = Label(root, text="Wheel of Boredom!")
viewOrSurprise = Label(root, text="Would you like to view the list before you spin?")

# List
activities = ["go for a walk", "watch your favorite show", "go see a movie", "draw something", "play a video game", 
                  "take a long bath", "go for a drive", "play with a pet", "chat with a friend", "have a tea party", 
                  "complete one task that you've been putting off", "listen to music", "try a new recipe", 
                  "visit the library", "try a new restaurant"]

# Functions
# view list: display the list
def viewList ():
    Label(root, text=activities)
# surprise me: don't display the list
# spin the wheel: select a random item the chosen list and display the result

# Display the result
def randomizer():
    result = random.choice(activities)
    messagebox.showinfo("Congratulations! You should " + result + "!")


# Buttons
view =Button(root, text="See the list", command=viewList)
surpriseMe = Button(root, text="Surprise me", command=randomizer)
spin = Button(root, text="Spin the Wheel!", command=randomizer)
exit = Button(root, text="Exit", command=root.quit)


# Widget Placement
welcome.grid(row=0, column=2)
title.grid(row=1, column=2)
viewOrSurprise.grid(row=2, column=2)
view.grid(row=3, column=2)
# surpriseMe.grid(row=3, column=2)
exit.grid(row=8, column=2)


root.mainloop()