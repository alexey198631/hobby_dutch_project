"""
this code is for reading pdf files from dutch exercise books. the main goal - to update the disctionary with examples
of sentences.
additional goal is to test tkinter the first time
"""

import tkinter as tk
import PyPDF2
from PyPDF2 import PdfReader
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=100)
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

def open_file():
    browse_text.set('loading...')
    file = askopenfile(parent=root, mode='rb', title="Choose a file",filetypes=[('PDf Files', '*.pdf')])
    if file:

        reader = PdfReader(file)
        number_of_pages = len(reader.pages)
        page = reader.pages[500]
        text = page.extract_text()

        #textbox
        text_box = tk.Text(root,height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, text)
        text_box.tag_configure('center', justify='center')
        text_box.tag_add('center',1.0,'end')
        text_box.grid(column=1,row=3)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
brows_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Arial", height=2, width=10)
browse_text.set("Browse")
brows_btn.grid(column=1,row=2)

root.mainloop()