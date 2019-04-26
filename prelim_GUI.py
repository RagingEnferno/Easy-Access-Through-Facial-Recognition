#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk, Image
import cv2

window = Tk()

app = Frame(window, bg="grey")
app.grid(column=2, row=3)

screen = Label(app)
screen.grid()

capture = cv2.VideoCapture(0)

def camFeed():
    _, frame = capture.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    screen.imgtk = imgtk
    screen.configure(image=imgtk)
    screen.after(1, camFeed) 

camFeed()

window.title("Facial Recgonition Application")
window.geometry('1200x650')
window.configure(background='grey')

lbl = Label(window, text="Enter new user name", font=("Courier", 22), fg="#006400", background='grey')
lbl.grid(column=0, row=0)

txt = Entry(window,width=30)
txt.grid(column=1, row=0)

lbl = Label(window, text="Add User", font=("Courier", 22), fg="#006400", background='grey')
lbl.grid(column=0, row=1)

lbl = Label(window, text="Take Picture", font=("Courier", 22), fg="#006400", background='grey')
lbl.grid(column=0, row=20)


btn_takePic = Button(window, height=1, width=4)
btn_takePic.grid(column=1, row=20)

def clicked():
    messagebox.showinfo('User added', 'name')
    
btn_addUser = Button(window, command=clicked, height=1, width=4)
btn_addUser.grid(column=1, row=1)

window.mainloop()
