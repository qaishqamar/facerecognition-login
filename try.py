from tkinter import *

root = Tk()
root.geometry("400x300")

def startMain():
    root.destroy()
    import jarvis


button = Button(text="START", command=startMain)
button.pack()

root.mainloop()