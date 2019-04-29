from tkinter import *
from tkinter import messagebox #pop up box doesn't work unless this is called for me (Justin), strange.

from PIL import ImageTk, Image
import cv2

window = Tk()

app = Frame(window, bg="grey")
app.grid(column=1, row=3)

screen = Label(app)
screen.grid()

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)


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
window.geometry('645x630')
window.configure(background='grey')

lbl = Label(window, text="Enter new user:", font=("Serif", 14), fg="black", background='grey')
lbl.grid(column=1, row=0)

txt = Entry(window,width=40)
txt.grid(column=1, row=1)

btn_takePic = Button(window, text='Take Picture', height=3, width=10)
btn_takePic.grid(column=1, row=100)

def clicked():
    messagebox.showinfo('User added', txt)
    
btn_addUser = Button(window, text='Add User', command=clicked, height=1, width=10)
btn_addUser.grid(column=1, row=2)

window.mainloop()
