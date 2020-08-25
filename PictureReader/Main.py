import sys
from tkinter import *
from PIL import Image, ImageTk

file_path = ""
imgX = 960
imgY = 540

def get_file():
	global file_path
	try:
 		file_path = str(sys.argv[1])
 		print(file_path)
	except LookupError:
 		print("error")
 		sys.exit(1)

def main():
	global imgX
	global imgY

	get_file()
	imagePIL = Image.open(file_path)
	imagePIL = imagePIL.resize((imgX, int(imagePIL.size[1] * (imgX / imagePIL.size[0]))), Image.ANTIALIAS)

	root = Tk()
	root.title("Picture reader")
	root.geometry("960x540")
	root.resizable(False, False)

	image = ImageTk.PhotoImage(imagePIL)

	canv = Canvas(root, width = imgX, height = imgY)
	imageSprite = canv.create_image(imgX / 2, imgY / 2, image = image)
	canv.pack()

	root.mainloop()

main()