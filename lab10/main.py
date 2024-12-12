import tkinter as tk

root = tk.Tk()
root.title("test")

frame = tk.Frame(root)
label = tk.Label(frame, text="text")
label.grid()

frame.pack()

root.mainloop()