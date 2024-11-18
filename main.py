# Import necessary libraries
from tkinter import *
from tkinter import messagebox
import base64
import os

# Function to handle decryption


def decryption_key():
    # Get the decryption key from the input field
    key = code.get()

    # Check if the key is correct
    if key == "1234":
        # Create a new window for decryption
        screen2 = Toplevel(screen)
        screen2.title("Encryption and Decryption Tool | Decryption Results")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        # Get the encrypted message from the text field
        message = text1.get(1.0, END)

        # Decode the message using base64
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decryption_key = base64_bytes.decode("ascii")

        # Display the decrypted message in the new window
        Label(screen2, text="DECRYPTION RESULTS", font="Arial",
              fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Arial 10", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decryption_key)

    # Handle incorrect or empty key
    elif key == "":
        messagebox.showerror(
            "Encryption and Decryption Tool", "Please Enter a Password")
    elif key != "1234":
        messagebox.showerror(
            "Encryption and Decryption Tool", "Incorrect Password")

# Function to handle encryption


def encryption_key():
    # Get the encryption key from the input field
    key = code.get()

    # Check if the key is correct
    if key == "1234":
        # Create a new window for encryption
        screen1 = Toplevel(screen)
        screen1.title("Encryption and Decryption Tool | Encryption Results")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        # Get the message from the text field
        message = text1.get(1.0, END)

        # Encode the message using base64
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encryption_key = base64_bytes.decode("ascii")

        # Display the encrypted message in the new window
        Label(screen1, text="ENCRYPTION RESULTS", font="Arial",
              fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Arial 10", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encryption_key)

    # Handle incorrect or empty key
    elif key == "":
        messagebox.showerror(
            "Encryption and Decryption Tool", "Please Enter a Password")
    elif key != "1234":
        messagebox.showerror(
            "Encryption and Decryption Tool", "Incorrect Password")

# Function to create the main display


def main_display():
    global screen
    global code
    global text1

    # Create the main window
    screen = Tk()
    screen.geometry("375x398")

    # Set the icon for the window
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto(False, image_icon)

    # Set the title of the window
    screen.title("Encryption and Decryption Tool")

    # Function to reset the input fields
    def reset():
        code.set("")
        text1.delete(1.0, END)

    # Create the input fields and buttons
    Label(text="Enter text for Encryption and Decryption",
          fg="black", font=("Arial", 13)).place(x=10, y=10)
    text1 = Text(font="Arial 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter Secret Key for Encryption and Decryption",
          fg="black", font=("Arial", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=(
        "Arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833",
           fg="white", bd=0, command=encryption_key).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56",
           fg="white", bd=0, command=decryption_key).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff",
           fg="white", bd=0, command=reset).place(x=10, y=300)


main_display()
screen.mainloop()
