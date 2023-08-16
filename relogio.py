import tkinter as tk
import time


class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Relógio")

        self.time_label = tk.Label(root, font=("Helvetica", 200))
        self.time_label.pack()

        self.update_time()

    def update_time(self):
        current_time = time.localtime()
        hours = str(current_time.tm_hour).zfill(2)
        minutes = str(current_time.tm_min).zfill(2)
        seconds = str(current_time.tm_sec).zfill(2)
        time_string = f"{hours}:{minutes}:{seconds}"

        self.time_label.config(text=time_string)
        self.root.after(1000, self.update_time)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
