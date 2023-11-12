from curses import BUTTON1_CLICKED
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox


root = tk.Tk()
root.title('aceitas?')
root.geometry('600x600')
root.configure(background='#ffc8dd')


def move_button_1(e):
    if abs(e.x - BUTTON1_CLICKED.winfo_x()) < 50 and abs(e.y - BUTTON1_CLICKED.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - BUTTON1_CLICKED.winfo_width())
        y = random.randint(0, root.winfo_height() - BUTTON1_CLICKED.winfo_height())
        BUTTON1_CLICKED.place(x=x, y=y)


def accepted():
    messagebox.showinfo( 'te amo meu gatinho de papai, vamo MIMIR juntinho?' )      

    def denied():
        button_1.destroy() 


        margin = Canvas(root, width=500, bg='#ffc8dd', height=100, bd=0, highlightthickness=0, relief='ridge')
        
        margin.pack()
        text_id = Label(root, bg='#ffc8dd', text= 'quer namorar comigo?',fg='#590d22', font=('Montserrat', 24, 'bold'))

        text_id.pack()
        button_1 = tk.Button(root, text='nao', bg='#ffb3c1', command=denied,relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))

        button_1.pack()
        root.bind('<Motion>', move_button_1)
        button_2 = tk.Button(root, text='sim', bg='#ffb3c1', relief=RIDGE, bd=3, command=accepted, font=('Montserrat', 14, 'bold') )

        button_2.pack()


        root.mainloop()

        

        
        