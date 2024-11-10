import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io
from tkinter import filedialog
import os

root = tk.Tk()

def setup():

    root.title("Image Filter App")
    root.geometry("700x700")

    open_folder_button = tk.Button(root, text="Select Image", command=select_image)
    open_folder_button.pack(pady=20)

    root.mainloop()

def select_image():
 
    file = filedialog.askopenfile()  # Opens a dialog to select a image
    if file:
        image_path = file.name
        print("Selected Folder:", image_path)
        display_image(image_path)

def display_image(image_path):
    
    #canvas size
    canvas_width = 450
    canvas_height = 450
    
    #resize image to fit in the canvas
    img = Image.open(image_path)
    img = img.resize((canvas_width, canvas_height), Image.LANCZOS)

    # Create a canvas & display the image
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)

    canvas.image = tk_img

setup()