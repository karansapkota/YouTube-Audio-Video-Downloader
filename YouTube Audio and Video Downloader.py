from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_media(url, save_path, is_video=True):
    try:
        yt = YouTube(url)
        if is_video:
            streams = yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res_stream = streams.get_highest_resolution()
        else:
            streams = yt.streams.filter(only_audio=True)
            highest_res_stream = streams.first()

        highest_res_stream.download(output_path=save_path)
        print("Successfully Downloaded !")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}\n")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter Your YouTube Video url: ")
    save_dir = open_file_dialog()

    if save_dir:
        download_type = input("Enter 'v' to download video or 'a' to download audio: ").lower()
        
        if download_type == 'v':
            print("Downloading video... Please wait.")
            download_media(video_url, save_dir, is_video=True)
        elif download_type == 'a':
            print("Downloading audio... Please wait.")
            download_media(video_url, save_dir, is_video=False)
        else:
            print("Invalid choice. Please enter 'v' for video or 'a' for audio.")
    else:
        print("Folder Not Selected")
