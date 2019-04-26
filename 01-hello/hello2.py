try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk # Python2

class HelloApplication:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.hello = tk.Button(self.frame, text='Hello', command=self.say_hello)
        self.quit = tk.Button(self.frame, text='Quit', command=parent.quit)
        self.label = tk.Label(self.frame, text='', bd=1)
        self.frame.grid(row=0, column=0, padx=40, pady=40)
        self.hello.grid(row=0, column=0, padx=5)
        self.quit.grid(row=0, column=1, padx=5)
        self.label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    def say_hello(self):
        self.label['text'] = 'Hello World'

def main():
    root = tk.Tk()
    root.title('Hello World')
    HelloApplication(root)
    root.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()
