from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("334x332")
root.title("Volume Controller GUI")

# Function to show the current volume
def show_volume():
    volume = scale.get()
    tmsg.showinfo("Volume", f"Your Volume is set to - {volume}")

# Label
label = Label(root, text="Adjust the Volume that you want", font="arial,19,bold")
label.pack()

# Scale widget
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
scale.pack()

# Button to submit volume
Button(root, text="Submit Volume", relief=SUNKEN, command=show_volume).pack()

# Mainloop
root.mainloop()
