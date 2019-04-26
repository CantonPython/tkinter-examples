
import tkinter as tk
from tkinter import messagebox


def run_demo():
    """Display standard message boxes."""
    messagebox.showinfo('showinfo', 'It is good to know.')

    messagebox.showwarning('showwarning', 'You better check yourself.')

    messagebox.showerror('showerror', 'Everbody panic.')

    result = messagebox.askquestion('askquestion', 'Do you really want to do this?')
    print(result)

    result = messagebox.askokcancel('askokcancel', 'Do you want to do something?')
    print(result)

    result = messagebox.askyesno('askyesno', 'This is yes or no.')
    print(result)

    result = messagebox.askretrycancel('askretrycancel', 'This is ask/retry/cancel')
    print(result)

    messagebox.showinfo('showinfo', 'All done.')


root = tk.Tk()
root.title('Message Box Demo')
start = tk.Button(root, text='Start demo', command=run_demo)
quit = tk.Button(root, text='Quit', command=root.quit)
start.grid(row=0, column=0, padx=40, pady=20)
quit.grid(row=0, column=1, padx=40, pady=20)
root.mainloop()
root.destroy()
