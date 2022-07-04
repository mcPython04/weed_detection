from tkinter import *
from test import start
from PIL import Image, ImageTk
import cv2

window = Tk()
window.geometry("1920x1080") # window size
window.title("Weed Detection") # window name

# widget code will go here

# video stuff
label = Label(window)
label.grid(row=0, column=0)
cap = cv2.VideoCapture(1)

def video():
	# Get the latest frame and convert into Image
	cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
	img = Image.fromarray(cv2image)
	
	# Convert image to PhotoImage
	imgtk = ImageTk.PhotoImage(image = img)
	label.imgtk = imgtk
	label.configure(image=imgtk)

# button
start_b = Button(window, text='Start', command=video)
start_b.grid(row=20, column=0)

window.mainloop()
