# Import Required Modules
import tkinter as tk
from pyyoutube import Api
from pytube import YouTube
from threading import Thread
from tkinter import messagebox
from decouple import config


def get_list_videos():
    global playlist_item_by_id
    # Clear ListBox
    list_box.delete(0, "end")

    # Create API Object
    api_key = config("API_KEY")
    api = Api(api_key=api_key)

    if "youtube" in playlistId.get():
        playlist_id = playlistId.get()[len("https://www.youtube.com/playlist?list=") :]
    else:
        playlist_id = playlistId.get()

    # Get list of video links
    playlist_item_by_id = api.get_playlist_items(
        playlist_id=playlist_id, count=None, return_json=True
    )

    # Iterate through all video links and insert into listbox
    for index, videoid in enumerate(playlist_item_by_id["items"]):
        list_box.insert(tk.END, f" {str(index+1)}. {videoid['snippet']['title']}")

    download_start.config(state=tk.NORMAL)


def threading():
    # Call download_videos function
    t1 = Thread(target=download_videos)
    t1.start()


def download_videos():
    download_start.config(state="disabled")
    get_videos.config(state="disabled")

    # Iterate through all selected videos
    for i in list_box.curselection():
        videoid = playlist_item_by_id["items"][i]["contentDetails"]["videoId"]

        link = f"https://www.youtube.com/watch?v={videoid}"

        yt_obj = YouTube(link)

        try:
            filters = yt_obj.streams.filter(progressive=True, file_extension="mp4")
            
            # download the highest quality video
            filters.get_highest_resolution().download("~/YouTube-Downloads/")

            messagebox.showinfo("Success", "Video Successfully downloaded")
            download_start.config(state="normal")
            get_videos.config(state="normal")

        except Exception as e:
            print(repr(e))
            break




# Create Object
root = tk.Tk()
# Set geometry
root.geometry("400x400")

# Add Label
tk.Label(root, text="Youtube Playlist Downloader", font="italic 15 bold").pack(pady=10)
tk.Label(root, text="Enter Playlist URL:-", font="italic 10").pack()

# Add Entry box
playlistId = tk.Entry(root, width=60)
playlistId.pack(pady=5)

# Add Button
get_videos = tk.Button(root, text="Get Videos", command=get_list_videos)
get_videos.pack(pady=10)

# Add Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
list_box = tk.Listbox(root, selectmode="multiple")
list_box.pack(expand=tk.YES, fill="both")
list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

download_start = tk.Button(
    root, text="Download Start", command=threading, state=tk.DISABLED
)
download_start.pack(pady=10)

# Execute Tkinter
root.mainloop()
