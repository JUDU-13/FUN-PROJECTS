import tkinter as tk
from datetime import datetime

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

        # Create the GUI
        self.root = tk.Tk()
        self.root.title("Advanced Timer")
        self.root.geometry("200x100")

        self.label = tk.Label(self.root, text="00:00:00")
        self.label.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()
        self.stop_button.config(state=tk.DISABLED)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack()

    def start(self):
        self.start_time = datetime.now()
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.update_time()

    def stop(self):
        self.elapsed_time += (datetime.now() - self.start_time).total_seconds()
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def reset(self):
        self.elapsed
