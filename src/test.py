import threading
import tkinter as tk
from tkinter import Tk
import tkinter.font as tkFont


class App:
    def __init__(self, root: tk) -> None:
        self.video_url: str = ""
        self.create_window(root)
    
    def create_window(self, root: Tk) -> None:
        root.title("Download From YouTube")
        width = 490
        height = 190
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        highlight = tk.Label(
            root,
            anchor="center",
            font=tkFont.Font(family="Times", size=10),
            fg="#333333",
            justify="center",
            text="Download From Youtube",
        )
        highlight.place(x=0, y=0, width=490, height=30)

        url_input = tk.Entry(
            root,
            bg="#f9c5e6",
            borderwidth="1px",
            font=tkFont.Font(family="Times", size=10),
            fg="#333333",
            justify="left",
            text="Insert video link here",
            show="undefined",
        )
        url_input.place(x=10, y=40, width=359, height=30)

        download_button = tk.Button(
            root,
            activebackground="#c71585",
            activeforeground="#ffffff",
            disabledforeground="#ffffff",
            anchor="center",
            bg="#c71585",
            cursor="watch",
            font=tkFont.Font(family="Times", size=10),
            fg="#000000",
            justify="center",
            text="Download",
            relief="raised",
            command=lambda: threading.Thread(target=self.download_button_command, args=()).start(),
        )
        download_button.place(x=380, y=40, width=100, height=30)

        message = tk.Label(
            root,
            font=tkFont.Font(family="Times", size=10),
            fg="#333333",
            justify="center",
            text="Video download successfully!",
        )
        message.place(x=0, y=90, width=492, height=31)

    def download_button_command(self):
        print("command")


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
