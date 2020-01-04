#
# ScrolledText example
#


import tkinter as tk
from tkinter import scrolledtext

class ExampleApp:
    def __init__(self, root):
        self.root = root
        root.title('Example')
        frame = tk.Frame(root, width=200, height=200)
        frame.pack(fill='both', expand=True)
        self.create_widgets(frame)
        root.bind('<Return>', self.add_text)

    def create_widgets(self, parent):
        self.text = scrolledtext.ScrolledText(
                    master=parent,
                    wrap=tk.WORD,
                    height=10)
        self.text.pack(padx=10, pady=10, fill='both', expand=True)
        self.text.insert('insert',

"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
""")
        self.entry = tk.Entry(parent)
        self.ok = tk.Button(parent, text='Ok', command=self.add_text)
        self.entry.pack(padx=10, pady=10, side='left', fill='both', expand=True)
        self.ok.pack(padx=10, pady=10, side='right')
        self.entry.focus_set()
        self.ok.bind('<Button-1>', self.add_text)

    def add_text(self, event=None):
        entered = self.entry.get()
        if entered:
            self.text.insert('end', entered + '\n')
            self.text.see('end')
            self.entry.delete(0, 'end')

def main():
    root = tk.Tk()
    app = ExampleApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
