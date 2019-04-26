#
# Button callbacks examples.
#
# 1. parameterless function
# 2. bound method
# 3. lambda method (closure)
# 4. callback object
#

import tkinter as tk

count = 0; # Global for simple_callback

# No arguments. Access to globals only.
def simple_callback():
    global count
    count += 1
    print('Simple callback called %d time%s.' % (count, 's' if count>1 else ''))

# Argument: print the name of the button pressed.
def print_name(name):
    print('Button %s pressed' % (name))

# Command object example.
class Counter:
    def __init__(self, name):
        self.count = 0
        self.name = name

    def __call__(self):
        self.count += 1
        print('Command callback called %d time%s on button %s.' % \
              (self.count, 's' if self.count>1 else '', self.name))

class CallbackExamples:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.grid(row=0, column=0, padx=40, pady=20)

        # Simple callback
        self.b1 = tk.Button(self.frame, text='Simple callback', command=simple_callback)
        self.b1.grid(row=0, column=0)

        # Bound method
        self.count = 0;
        self.b2 = tk.Button(self.frame, text='Method callback', command=self.method_callback)
        self.b2.grid(row=1, column=0)

        # Lambda
        name = 'Name 1'
        self.b3 = tk.Button(self.frame, text=name, command=lambda : print(name))
        self.b3.grid(row=2, column=0)

        # Command object
        name = 'Command object'
        command = Counter(name)
        self.b4 = tk.Button(self.frame, text=name, command=command)
        self.b4.grid(row=3, column=0)


    def method_callback(self):
        # Get the 'self' context.
        self.count += 1
        print('Bound method callback called %d time%s.' % (self.count, 's' if self.count>1 else ''))


def main():
    root = tk.Tk()
    root.title('Hello World')
    CallbackExamples(root)
    root.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()
