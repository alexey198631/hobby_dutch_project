"""
this code is for reading pdf files from dutch exercise books. the main goal - to update the disctionary with examples
of sentences.
additional goal is to test tkinter the first time
"""

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

#logo
logo = Image.open('dutch.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

#instruction
instrusction = tk.Label(root, text='Select a PDF file', font='Arial')
instrusction.grid(columnspan=3, column=0, row=1)

#browse button

root.mainloop()