# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:20:30 2021

@author: DELL
"""
import tkinter as tk
import flames1 as f

# Top level window
frame = tk.Tk()
frame.title("Flames")
frame.geometry('600x400')
# Function for getting Input
# from textbox and printing it
# at label widget
lb=tk.Label(frame,text="Boyname ").grid(column=1,row=1)

def printInput():
    boy = Boyname.get("1.0",'end-1c')
    girl = Girlname.get("1.0",'end-1c')
    s= f.flames1(Boy=boy, Girl=girl)
    frame.destroy()
    frame1 = tk.Tk()
    frame1.title("Flames")
    frame1.geometry('600x400')
    lbl = tk.Label(frame1, text = s).grid(column=40,row=20)

# TextBox Creation
Boyname = tk.Text(frame,
				height = 1,
				width = 20)
Boyname.grid(column=9,row=1)



lb1=tk.Label(frame,text="Girlname ").grid(column=1,row=2)


Girlname = tk.Text(frame,
				height = 1,
				width = 20)
Girlname.grid(column=9,row=2)



# Button Creation
printButton = tk.Button(frame,
						text = "Enter",
						command = printInput)
printButton.grid(column=40,row=5)

# Label Creation



frame.mainloop()
