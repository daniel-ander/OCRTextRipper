import tkinter as tk
from tkinter import filedialog, Text, scrolledtext
from OCRTextRipper import OCRTextRipper

ripper = OCRTextRipper()

def open_file():
    filename = filedialog.askopenfilename()
    ripper.open_file(filename)
    

def take_screenshot():
    ripper.take_screenshot()
    

def apply_filters():
    ripper.apply_filters()
    

def apply_ocr():
    result = ripper.apply_ocr()
    if result is not None:
        result_text.insert(tk.INSERT, result)

def set_tesseract_path():
    path = filedialog.askopenfilename()
    error = ripper.set_tesseract_path(path)
    if error is not None:
        result_text.insert(tk.INSERT, error)
    

root = tk.Tk() # Create the root window

set_path = tk.Button(root, text="Set Path", padx=10, pady=5, fg="white", bg="black", command=set_tesseract_path)
set_path.pack()

open_button = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="black", command=open_file)
open_button.pack()

screenshot_button = tk.Button(root, text="Take Screenshot", padx=10, pady=5, fg="white", bg="black", command=take_screenshot)
screenshot_button.pack()

apply_filters_button = tk.Button(root, text="Apply Filters", padx=10, pady=5, fg="white", bg="black", command=apply_filters)
apply_filters_button.pack()



apply_ocr = tk.Button(root, text="Save Result", padx=10, pady=5, fg="white", bg="black", command=apply_ocr)
apply_ocr.pack()

result_text = scrolledtext.ScrolledText(root, width=40, height=10)
result_text.pack()

root.mainloop() # Start the main loop

