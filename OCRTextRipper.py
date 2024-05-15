import pytesseract
import pyautogui
from PIL import Image, ImageFilter
import cv2
from pynput.mouse import Listener
import time
import os

# I need to create a python OCR Application Prototype that can do the following:
# 1. Open an image from file, or take a picture of the screen. 
# 2. Apply a greyscale filter
# 3. Apply a binarize filter
# 4. Apply an OCR filter
# 5. Print the OCR result, or store it in a file, or spreadsheet format. 

# I would like all of this to be able to be done from the command line to start. 
# I also need to be able to package this and deploy it as a prototype to a website. 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OCRTextRipper:
    
    def __init__(self):
        self.img = None
        self.set_tesseract_path()

    def open_file(self, filename):
        self.img = Image.open(filename)

    def set_tesseract_path(self, path=r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
        else:
            return "Tesseract path doesn't exist. Please set the path."
    

    def apply_filters(self):
        if self.img is not None:
            self.img = self.img.convert('L')
            #self.img = self.img.filter(ImageFilter.MedianFilter(size=3))
            self.img = self.img.point(lambda x: 0 if x < 100 else 255, '1')
            self.img.show()
        else:
            error = "No image loaded!"
            return error

    def apply_ocr(self):
        if self.img is not None:
            text = pytesseract.image_to_string(self.img)
            return text
        else:
            error = "No image loaded!"
            return error
        
    
    def take_screenshot(self): #help me create a simpler screenshot function
        # Use this later to set a screens ize or something

        """screen_width, screen_height = pyautogui.size()"""
        
        # Capture the screen image
        screenshot = pyautogui.screenshot()
        
        # Set the image attribute
        self.img = screenshot.convert('RGB')
        
        # Show the image
        self.img.show()

        

