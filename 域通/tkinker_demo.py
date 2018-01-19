from tkinter import *
root = Tk()
lb = Listbox(root)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack(side=LEFT)
root.mainloop()