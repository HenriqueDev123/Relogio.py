import tkinter as tk
import time

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Relógio")
        self.root.bind("<KeyPress>", self.handle_key_press)
        self.root.bind("<KeyRelease>", self.handle_key_release)

        self.time_label = tk.Label(root, font=("Helvetica", 200))
        self.time_label.pack()

        self.font_size = 200
        self.update_time()

    def handle_key_press(self, event):
        if event.keysym == "equal":
            self.increase_font_size()
        elif event.keysym == "minus":
            self.decrease_font_size() 

    def handle_key_release(self, event):
        pass

    def increase_font_size(self):
        self.font_size += 10
        self.update_time_font()

    def decrease_font_size(self):
        self.font_size = max(50, self.font_size - 10)
        self.update_time_font()

    def update_time_font(self):
        new_font = ("Helvetica", self.font_size)
        self.time_label.config(font=new_font)

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
