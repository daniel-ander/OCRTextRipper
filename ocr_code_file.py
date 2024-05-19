import pytesseract
import pyautogui
from PIL import Image
from pynput.mouse import Listener
import os
#CURRENT VERSION: v0.1

#--- OCR Text Ripper ---#
#--- A simple OCR tool that allows you to open an image file, apply filters, and extract text from the image ---#

#v0.1
#--- GUI functionality, open file, take screenshot, apply filters, apply OCR, set tesseract path ---#


#Required for next update
#v0.2
#--- Add a function to take a screenshot of a specific area, add a way to set the dimensions for the screenshot, and a warning for the screenshot function ---#
#--- increase the size of the window and add a box to view the image as it is being processed ---#
#--- Add a way to set the path for the tesseract executable ---#
#--- Add a way to save the text to a file ---#
#--- Increase the accuracy of the OCR somehow ---#



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

        

