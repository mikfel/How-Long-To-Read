import tkinter
import pyperclip
from tkinter import *
from tkinter import ttk
import time
#word counter
x = str(pyperclip.paste())
b = len(x.split())
print(b)
timeleft=round(b/200, 2)


#Tkinter window displaying word count
root = Tk()
root.geometry("+1750+70")
frm = ttk.Frame(root, padding=10)
root.attributes('-topmost', True)
frm.grid()
ttk.Label(frm, text="Words count: "+str(b)).grid(column=0, row=0)
ttk.Label(frm, text="Time to read: "+str(timeleft)+" minutes").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
root.mainloop()