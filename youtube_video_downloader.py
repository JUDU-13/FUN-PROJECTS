import tkinter as tk
from pytube import YouTube

def download_video():
    # Get the URL from the entry field
    url = url_entry.get()

    # Create a YouTube object
    yt = YouTube(url)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Download the video
    stream.download()

    # Update the status label
    status_label.config(text="Download complete!")

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create a label for the URL entry field
url_label = tk.Label(text="Enter the YouTube URL:")
url_label.pack()

# Create an entry field for the URL
url_entry = tk.Entry()
url_entry.pack()

# Create a button to start the download
download_button = tk.Button(text="Download", command=download_video)
download_button.pack()

# Create a label to show the download status
status_label = tk.Label(text="")
status_label.pack()

# Start the GUI main loop
window.mainloop()
