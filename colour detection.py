import cv2
import tkinter as tk
from tkinter import filedialog

class ColorDetector:
    def __init__(self):
        self.color = None
        self.source = None
        self.cap = None

        # Create the GUI
        self.root = tk.Tk()
        self.root.title("Color Detector")

        self.color_var = tk.StringVar(self.root)
        self.color_var.set("Red")
        self.color_dropdown = tk.OptionMenu(self.root, self.color_var, "Red", "Green", "Blue")
        self.color_dropdown.pack()

        self.webcam_button = tk.Button(self.root, text="Webcam", command=self.start_webcam)
        self.webcam_button.pack()

        self.file_button = tk.Button(self.root, text="File", command=self.select_file)
        self.file_button.pack()

    def start_webcam(self):
        self.source = "webcam"
        self.color = self.color_var.get()
        self.cap = cv2.VideoCapture(0)
        self.detect_color()

    def select_file(self):
        self.source = "file"
        self.color = self.color_var.get()
        file_path = filedialog.askopenfilename()
        self.cap = cv2.VideoCapture(file_path)
        self.detect_color()

    def detect_color(self):
        while True:
            # Get a frame from the webcam
            ret, frame = self.cap.read()

            # Convert the frame to HSV color space
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Define the range of the color to detect
