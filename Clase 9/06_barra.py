import tkinter as tk

def report(): 
    print(scl.get())

root = tk.Tk()
scl = tk.Scale(root, from_=-100, to=100, tickinterval=50, resolution=10)
scl.pack(expand=tk.YES, fill=tk.Y)

tk.Button(root, text='state', command=report).pack(side=tk.RIGHT)
root.mainloop()