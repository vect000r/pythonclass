import tkinter as tk
import generator
import random

class App:
    def __init__(self, window_width=700, window_height=400):
        self.root = tk.Tk()
        self.root.title("Slot Machine Simulator")
        self.root.geometry(f"{window_width}x{window_height}")
        
        self.base_frame = tk.Frame(self.root, bd=5, relief="sunken")
        self.base_frame.pack()

        # Ramki dla slotów
        self.slot_frames = [tk.Frame(self.base_frame, bd=2, relief="groove") for _ in range(3)]
        for i, frame in enumerate(self.slot_frames):
            frame.grid(row=0, column=i, padx=5, pady=5)

        # Etykiety dla slotów
        self.slot_labels = [
            tk.Label(frame, text="1", width=10, height=5, font=("Arial", 24))
            for frame in self.slot_frames
        ]
        for label in self.slot_labels:
            label.pack()

        # Przycisk SPIN
        self.spin_button = tk.Button(
            self.base_frame, text="Spin", command=self.spin_slots, font=("Arial", 16)
        )
        self.spin_button.grid(row=1, column=1, pady=10)

        # Etykieta z informacją o wygranej
        self.result_label = tk.Label(
            self.base_frame, text="", font=("Arial", 16), fg="blue"
        )
        self.result_label.grid(row=2, column=0, columnspan=3)

        self.root.mainloop()

    def generate_numbers(self):
        """Funkcja korzystająca z NumberGenerator do wylosowania trzech losowych liczb z przedziału 1 do 5"""
        gen = generator.NumberGenerator()
        return gen.result()

    def spin_slots(self):
        """Funkcja uruchmiająca kręcenie automatu"""
        self.spin_button.config(state=tk.DISABLED)
        self.result_label.config(text="")
        self.spinning = True
        self.final_numbers = self.generate_numbers()
        self.spin_count = 0
        self.animate_spin()

    def animate_spin(self):
        """Funkcja odpowiedzialna za animacje kręcenia"""
        if self.spinning:
            # Podczas kręcenia pokazujemy użytkownikowi losowe liczby
            for label in self.slot_labels:
                label.config(text=str(random.randint(1, 5)))

            self.spin_count += 1

            if self.spin_count < 20:  # Kręcimy określoną liczbę razy
                self.root.after(100, self.animate_spin)
            else:
                self.spinning = False
                self.show_final_numbers()

    def show_final_numbers(self):
        """Funkcja wyświetlająca użytkownikowi wynik"""
        # Pokaż końcowy wynik na slotach
        for i, label in enumerate(self.slot_labels):
            label.config(text=str(self.final_numbers[i]))

        self.check_win()
        self.spin_button.config(state=tk.NORMAL)

    def check_win(self):
        """Funkcja sprawdzająca czy wszystkie wylosowane liczby są takie same"""
        if len(set(self.final_numbers)) == 1:
            self.result_label.config(text="Mega big win!")
        else:
            self.result_label.config(text="Better luck next time!")
