import tkinter as tk

def hello():
    print('hello')

class MyApplication:
    def __init__(self, root):
        self.create_menu(root)

    def create_menu(self, parent):
        menubar = tk.Menu(parent)

        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=hello)
        filemenu.add_command(label="Save", command=hello)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        # create more pulldown menus
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=hello)
        editmenu.add_command(label="Copy", command=hello)
        editmenu.add_command(label="Paste", command=hello)
        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=hello)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        parent.config(menu=menubar)

def main():
    root = tk.Tk()
    root.title('Menubar Example')
    MyApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()
