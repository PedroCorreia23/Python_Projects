import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageOps  

root = tk.Tk()

original_image = None
processed_image = None
canvas = None
tk_img = None
grayscale = None
sepia = None
blur = None

def setup():

    global canvas, grayscale, sepia, blur, save

    root.title("Image Filter App")
    root.geometry("700x700")

    #select image button
    open_folder_button = tk.Button(root, text="Select Image", command=select_image)
    open_folder_button.pack(pady=20)

    # Create a canvas 
    canvas = tk.Canvas(root, width=450, height=450)
    canvas.pack()

    #frame to center the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=50)  # Center vertically

    #grayscale, sepia & blur buttons 
    grayscale = tk.Button(button_frame, text="Grayscale", command=apply_grayscale)
    sepia = tk.Button(button_frame, text="Sepia", command=apply_sepia)
    blur = tk.Button(button_frame, text="Blur", command=apply_blur)

    save = tk.Button(root, text="Save", command=save_image)

    root.mainloop()

def select_image():
    global original_image, processed_image

    file = filedialog.askopenfile()  # Opens a dialog to select a image
    if file:
        image_path = file.name
        original_image = Image.open(image_path)
        processed_image = original_image.copy()
        print("Selected Image:", image_path)
        display_image(processed_image)

        grayscale.pack(side=tk.LEFT, padx=5)
        sepia.pack(side=tk.LEFT, padx=5)
        blur.pack(side=tk.LEFT, padx=5)

        save.pack(pady=10)

def display_image(img):

    global tk_img
    
    #resize image to fit in the canvas
    resized_img = img.resize((450, 450), Image.LANCZOS)

    tk_img = ImageTk.PhotoImage(resized_img)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
    
def apply_grayscale():
    global processed_image
    processed_image = ImageOps.grayscale(original_image)  # Apply grayscale
    display_image(processed_image)  

def apply_sepia():
    global processed_image
    sepia_img = original_image.convert("RGB")
    sepia_data = [
        (int(r * 0.393 + g * 0.769 + b * 0.189),
         int(r * 0.349 + g * 0.686 + b * 0.168),
         int(r * 0.272 + g * 0.534 + b * 0.131))
        for r, g, b in sepia_img.getdata()
    ]
    sepia_img.putdata(sepia_data)
    processed_image = sepia_img
    display_image(processed_image)  

def apply_blur():
    global processed_image
    processed_image = original_image.filter(ImageFilter.BLUR)  
    display_image(processed_image)  

def save_image():
    global processed_image

    if processed_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",                                                  
                                                filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg"),
                                                            ("All files", "*.*")])
        
        if file_path:
            processed_image.save(file_path)
            print(f"Image saved as {file_path}")
        else:
            print("Save cancelled.")
    else:
        print("No image to save.")

setup()