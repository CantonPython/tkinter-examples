
from tkinter import *

class MyApplication:
    def __init__(self, parent):
        frame = Frame(parent)
        frame.pack()
        Button(frame, text='Quit', command=frame.quit).pack()
        Button(frame, text='Hello', command=self.say_hello).pack()
        self.label = Label(frame, text='')
        self.label.pack()

    def say_hello(self):
        print('Hello World')
        self.label['text'] = 'Hello World'

root = Tk()
root.geometry('200x200+100+100')
MyApplication(root)
root.mainloop()
root.destroy()
