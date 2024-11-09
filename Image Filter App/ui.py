import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io
from tkinter import filedialog
import os

def setup():

    root = tk.Tk()
    root.title("Image Filter App")
    root.geometry("500x500")

    open_folder_button = tk.Button(root, text="Select Folder", command=open_folder)
    open_folder_button.pack(pady=10)

    root.mainloop()

def open_folder():

    folder_path = filedialog.askdirectory()  # Opens a dialog to select a folder
    print("Selected Folder:", folder_path)

setup()