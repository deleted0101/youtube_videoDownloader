import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Function to download the video
def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        download_path = destination_entry.get()
        video_stream.download(download_path)
        messagebox.showinfo("Download Complete", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create and pack labels and entry fields
url_label = tk.Label(window, text="Enter YouTube URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

destination_label = tk.Label(window, text="Destination Folder:")
destination_label.pack()
destination_entry = tk.Entry(window, width=50)
destination_entry.pack()

# Create and pack download button
download_button = tk.Button(window, text="Download Video", command=download_video)
download_button.pack()

# Run the main loop
window.mainloop()
