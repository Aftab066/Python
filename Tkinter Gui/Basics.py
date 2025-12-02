# import tkinter as tk

# root = tk.Tk()
# root.title("Window")
# root.geometry("400x300")

# root.mainloop()

import tkinter as tk

def clicked():
    print("Alhamdulillah!")

root = tk.Tk()
root.title("Button Example")

btn = tk.Button(root, text="Click Me", command=clicked)
btn.pack()

root.mainloop()