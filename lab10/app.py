import tkinter as tk
import generator
class App:
    def __init__(self, window_width=700, window_height=350):
        self.root = tk.Tk()
        self.root.title("Slot machine simulator")
        self.root.geometry(f"{window_width}x{window_height}")
        self.base_frame = tk.Frame(self.root)
        self.opt1_label = tk.Label(self.base_frame, text="A", width=10, height=10)
        self.opt2_label = tk.Label(self.base_frame, text="B", width=10, height=10)
        self.opt3_label = tk.Label(self.base_frame, text="C", width=10, height=10)
        self.opt1_label.grid(row=0, column=0)
        self.opt2_label.grid(row=0, column=1)
        self.opt3_label.grid(row=0, column=2)
        self.base_frame.pack()
        self.root.mainloop()

    def run(self):
        self.opt1_label = tk.Label(self.base_frame, text="A", width=10, height=10)
        self.opt2_label = tk.Label(self.base_frame, text="B", width=10, height=10)
        self.opt3_label = tk.Label(self.base_frame, text="C", width=10, height=10)        






