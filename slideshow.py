# create a simple image slideshow using tkinter

from itertools import cycle
from PIL import Image, ImageTk  
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow")

images = [
    r"C:\Users\ASUS\Downloads\pexels-skitterphoto-909.jpg",
    r"C:\Users\ASUS\Downloads\pexels-therato-3808168.jpg",
    r"C:\Users\ASUS\Downloads\pexels-therato-9598698.jpg",
    r"C:\Users\ASUS\Downloads\pexels-kratz-1363876.jpg",
    r"C:\Users\ASUS\Downloads\pexels-life-of-pix-7919.jpg",

]

image_size = (1080 ,1080)

images = [Image.open(image).resize(image_size) for image in images]
photos = cycle(ImageTk.PhotoImage(image) for image in images)

label = tk.Label(root)
label.pack()

def slideshow():
    img = next(photos)
    label.config(image=img)
    root.after(2000, slideshow)

slideshow()
root.mainloop()