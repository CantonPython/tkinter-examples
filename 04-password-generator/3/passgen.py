
import string
import random
import tkinter as tk

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
        pass

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
