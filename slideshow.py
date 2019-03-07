#!/usr/bin/env python3

flash_drive = "FA26-2330"

"""Display a slideshow from a list of filenames"""

import os
import tkinter
import math

from itertools import cycle
from PIL import Image, ImageTk

from pathlib import Path
import os
import subprocess
from time import sleep


class Slideshow(tkinter.Tk):
    """Display a slideshow from a list of filenames"""
    def __init__(self, images, slide_interval):
        """Initialize
        images = a list of filename
        slide_interval = milliseconds to display image
        """
        tkinter.Tk.__init__(self)
        self.configure(background='black')
        self.overrideredirect(True)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(),self.winfo_screenheight()))
        self.focus_set()  #Move focus to this widget
        self.bind("<Button-3>", self.close)
        self.config(cursor="none")
        self.slide_interval = slide_interval
        self.images = None
        self.set_images(images)
        self.slide = tkinter.Label(self)
        self.slide.pack()
        self.bind('<Escape>', self.close)

    def set_images(self, images):
         self.images = cycle(images)
    def close(self, event):
        self.destroy()
        print("Exiting")
    def center(self):
        """Center the slide window on the screen"""
        self.update_idletasks()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        self.geometry("+%d+%d" % (x, y))

    def set_image(self):
        """Setup image to be displayed"""
        self.image_name = next(self.images)
        filename, ext = os.path.splitext(self.image_name)
        self.raw_img = Image.open(self.image_name)
        scale = (min(self.winfo_screenwidth() / self.raw_img.width, self.winfo_screenheight() / self.raw_img.height))
        self.raw_img = self.raw_img.resize((int(self.raw_img.width*scale), int(self.raw_img.height*scale)), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.raw_img)
    def main(self):
        """Display the images"""
        self.set_image()
        self.slide.config(image=self.image)
        self.title(self.image_name)
        self.center()
        self.after(self.slide_interval, self.start)

    def start(self):
        """Start method"""
        self.main()
        self.mainloop()




# Read from flash drive
path = "/media/pi/" + flash_drive

while True:
    files = subprocess.run(['ls', path], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
    if len(files) > 1:
        break
    sleep(1)

my_file = Path(path)
if(my_file.exists()):
    # Load images
    exts = ["jpg", "bmp", "png", "gif", "jpeg"]
    images = [(path + "/" + fn) for fn in os.listdir(path) if any(fn.endswith(ext) for ext in exts)]
    if(len(images) > 0):
        # Start slideshow
        sl = Slideshow(images, 4000)
        sl.start()
    else:
        print("No images found")
else:
    print("Flash drive is not plugged in")

print("Done")
