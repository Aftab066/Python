import tkinter as tk

def clicked():
    print("Alhamdulillah!")

root = tk.Tk()
root.title("Asma Mulani")

btn = tk.Button(root, text="Click Me", command=clicked)
btn.pack()

root.mainloop()