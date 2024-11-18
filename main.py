from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    
    screen=Tk()
    screen.geometry("375x398")
    
    # icon
    image_icon=PhotoImage(file="keys.png")
    screen.iconphoto(False,image_icon)

    screen.title("Encryption and Decryption Tool")

    screen.mainloop()
main_screen()