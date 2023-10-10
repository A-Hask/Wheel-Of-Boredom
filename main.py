from tkinter import *
import random
from PIL import ImageTk, Image


root = Tk()
root.title("WHEEL! OF! BOREDOM!")

# upload images for icons
ico1 = Image.open('spinnerwheel.jpg')
ico2 = Image.open('list.jpg')
ico3 = Image.open('trophy.jpg')
wheel = ImageTk.PhotoImage(ico1)
list = ImageTk.PhotoImage(ico2)
trophy = ImageTk.PhotoImage(ico3)

# Change root icon
root.wm_iconphoto(False, wheel)

# Widgets
welcome = Label(root, text="Welcome to the")
title = Label(root, text="Wheel of Boredom!")
viewOrSurprise = Label(root, text="Would you like to view the list before you spin?")

# Activity List
activities = ["go for a walk", "watch your favorite show", "go see a movie", "draw something", "play a video game",
              "take a bubble bath", "go for a drive", "play with a pet", "chat with a friend", "have a tea party",
              "complete one task that you've been putting off", "listen to music", "try a new recipe",
              "visit the library", "try a new restaurant", "take a nap", "write a poem", "visit a cafe",
              "go to an ice cream shop", "start learning a new hobby", "organize your clothes", "build a fort"]


# Functions
# Popup window to display the list
def viewList():
    activityList = Toplevel()
    activityList.wm_iconphoto(False, list)
    activityList.title("Activity List!")
    activityList.geometry("300x600")

    words = Label(activityList, text="Here is the list of activities:")
    words.pack()

    for choice in activities:
        actList = Label(activityList, text=str(choice))
        actList.pack()

    back = Button(activityList, text="Back to homepage", command=activityList.destroy, padx=5, pady=5)
    back.pack(padx=5, pady=5)

# Randomize the array and display the result in a pop up window
def randomizer():
    randomize = Toplevel()
    randomize.wm_iconphoto(False, trophy, text="trophy")
    randomize.title("Here is your Result!")
    randomize.geometry("400x100")

    result = random.choice(activities)
    announcement = Label(randomize, text="I think that you should... " + result + "!")
    announcement.pack()

    back = Button(randomize, text="Back to home page", command=randomize.destroy )
    back.pack(padx=5, pady=5)

# Buttons
seeTheList = Button(root, text="See the list", command=viewList)
surpriseMe = Button(root, text="Surprise me", command=randomizer)
exit = Button(root, text="Exit", command=root.quit)

# Main Window Widget Placement
welcome.grid(row=0, column=1)
title.grid(row=1, column=1)
viewOrSurprise.grid(row=2, column=1)
seeTheList.grid(row=3, column=0, padx=5, pady=5)
surpriseMe.grid(row=3, column=2, padx=5, pady=5)
exit.grid(row=8, column=1, padx=5, pady=5)


root.mainloop()