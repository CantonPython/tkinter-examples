
import string
import random
import tkinter as tk
from tkinter import messagebox

def _generate(length, upper=0, digits=0, symbols=0):
    pw = []
    for _ in range(upper):
        c = random.choice(string.ascii_uppercase)
        pw.append(c)
    for _ in range(digits):
        c = random.choice(string.digits)
        pw.append(c)
    for _ in range(symbols):
        c = random.choice(string.punctuation)
        pw.append(c)
    length = length - len(pw)
    for _ in range(length):
        c = random.choice(string.ascii_lowercase)
        pw.append(c)
    random.shuffle(pw)
    return ''.join(pw)

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        root.title('Password Generator')
        frame = tk.Frame(root, width=200, height=200)
        frame.grid(row=0, column=0)
        self.create_widgets(frame)

    def create_widgets(self, parent):
        self.length = tk.IntVar(value=12)

        label = tk.Label(parent, text="Password length:")
        entry = tk.Entry(parent, textvariable=self.length)
        generate = tk.Button(parent, text="Generate", command=self.generate)
        quit = tk.Button(parent, text="Quit", command=self.root.destroy)
        result = tk.Label(parent, width=40, bd=2, relief='sunken', anchor='w')

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        generate.grid(row=1, column=0)
        quit.grid(row=1, column=1)
        result.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

        entry.focus_set()
        self.result = result

    def generate(self):
        try:
            length = self.length.get()
            if not 4 <= length <= 40:
                raise ValueError('out of range')
        except:
            messagebox.showwarning('Invalid length', 'Enter a length value between 4 and 40.')
        else:
            password = _generate(length)
            self.result['text'] = password

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
