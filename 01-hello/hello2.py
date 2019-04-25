
from tkinter import *

class MyApplication:
    def __init__(self, parent):
        frame = Frame(parent)
        frame.pack()
        button1 = Button(frame, text='Quit', command=frame.quit)
        button1.pack(side=LEFT)
        button2 = Button(frame, text='Hello', command=self.hello)
        button2.pack(side=LEFT)

    def hello(self):
        print('Hello World')

root = Tk()
app = MyApplication(root)
root.mainloop()
root.destroy()
