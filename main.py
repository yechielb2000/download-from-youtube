import threading

from pytube import YouTube
from tkinter import Label, Tk, messagebox, Entry, Button
from tkinter.font import BOLD
from consts import *


def create_app() -> None:
    root = Tk()
    root.geometry("600x300")
    root.resizable(False, False)
    root.title("Download from youtube")
    root.configure(background=YELLOW_COLOR)
    add_elements(root)
    root.mainloop()


def add_elements(root: Tk) -> None:
    entry = Entry(root, font=BOLD)
    entry.grid(row=row2, column=1, padx=PADDING_X, pady=PADDING_Y)
    highlight = create_label(root, "Download from Youtube!")
    highlight.grid(row=row0, column=1, padx=PADDING_X, pady=PADDING_Y)
    label = create_label(root, text="Enter youtube link :")
    label.grid(row=row2, column=0, padx=PADDING_X, pady=PADDING_Y)
    button = Button(
        root,
        text="Download",
        background=YELLOW_COLOR,
        foreground=BLACK_COLOR,
        font=BOLD,
        command=lambda: thread(root, entry.get()),
    )
    button.grid(row=row2, column=3, padx=PADDING_X, pady=PADDING_Y)


def create_label(root: Tk, text: str) -> Label:
    return Label(root, text=text, foreground=BLACK_COLOR, background=YELLOW_COLOR, font=BOLD)


def thread(root: Tk, url: str):
    downloading_message = create_label(root, "downloading..")
    downloading_message.grid(row=1, column=1)
    downloading_thread = threading.Thread(target=download_youtube_video, args=(url, downloading_message))
    downloading_thread.start()


def download_youtube_video(url: str, downloading_message: Label, *args) -> None:
    try:
        video = YouTube(url).streams.first()
        print(video)
        video.download()
        downloading_message.configure(text=Messages.DOWNLOAD_COMPLETE)
    except Exception as ex:
        downloading_message.configure(text=Messages.DOWNLOAD_FAILED)
        messagebox.showerror(title=Messages.DOWNLOAD_FAILED, message=str(ex))


if __name__ == "__main__":
    create_app()
