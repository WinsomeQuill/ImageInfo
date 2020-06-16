#######################################
#            By WinsomeQuill		  #
#######################################
from PIL import Image
import pytesseract
from pytesseract import Output
import cv2
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\winsomequill\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

def coordinates():
	img = cv2.imread(kartinka)
	d = pytesseract.image_to_data(img, output_type=Output.DICT)
	n_boxes = len(d['level'])
	for i in range(n_boxes):
		(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

	return x,y

def GetImage():
	root = tk.Tk()
	root.withdraw()
	global kartinka
	kartinka = askopenfilename(initialdir="C:\\", filetypes =(("JPG", "*.jpg"),("PNG","*.png*"),("All files","*.*")), title = "Choose a file.")
	im = Image.open(kartinka)
	text = pytesseract.image_to_string(im, lang = 'eng')

	return text

while True:
	try:
		print('Image text: {0}' .format(GetImage()))
		print('Image text coordinates: X / Y = {0}' .format(coordinates()))

		line = input('Exit? [ y / N ]')
		if line == 'y' or 'Y':
			print('Good buy!')
			quit()
	except(AttributeError):
		print('Error #0 <File not selected>')
