import tkinter as tk

class MyApplication:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.grid(row=0, column=0, padx=40, pady=20)
        self.create_widgets(frame)

    def create_widgets(self, parent):
        label = tk.Label(parent, text='Enter a number:')
        entry = tk.Entry(parent)
        ok = tk.Button(parent, text='Ok', command=self.handle_ok)
        results = tk.Label(parent, width=40, bd=2, relief='groove', justify='left')

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        ok.grid(row=0, column=2)
        results.grid(row=1, column=0, columnspan=3)
        entry.focus_set()

        self.entry = entry
        self.results = results

    def handle_ok(self):
        entered = self.entry.get()
        try:
            number = int(entered)
            self.display('You entered the number %d.' % (number))
        except:
            self.display('Sorry, that is not a number.')

    def display(self, msg):
        self.results['text'] = msg

def main():
    root = tk.Tk()
    root.title('Menubar Example')
    MyApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()
