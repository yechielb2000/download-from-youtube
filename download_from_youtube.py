import threading

from pytube import YouTube
from tkinter.font import BOLD
from tkinter import Entry, Tk, Button, messagebox
from consts import *
from utils import create_label


root = Tk() 

entry = Entry(root, font=BOLD)
entry.grid(row=row2, column=1, padx=PADDING_X, pady=PADDING_Y)


def create_app() -> None:
	root.geometry("580x200") 
    root.resizable(False, False)
    root.title('Download from youtube')
    root.configure(background=YELLOW_COLOR)
	add_elements()
	root.mainloop()


def add_elements() -> None:
    highlight = create_label(root, "Download from Youtube!")
    highlight.grid(row=row0, column=1, padx=PADDING_X, pady=PADDING_Y)
    label = create_label(root, text="Enter youtube link :")
    label.grid(row=row2,column=0,  padx=PADDING_X, pady=PADDING_Y)
    button = Button(root,
					text="Download", 
					background=YELLOW_COLOR,
					foreground=BLACK_COLOR, 
					font=BOLD, 
					command=lambda:thread(entry.get()))
    button.grid(row=row2, column=3, padx=PADDING_X, pady=PADDING_Y)
    

def thread(url):
	downloading_message = create_label(root, 'downloading..')
	downloading_message.grid(row=1,column=1) 
    downloading_thread = threading.Thread(target=download_youtube_video, args=(url))
    downloading_thread.start()


def download_youtube_video(url) -> None:
    try:
        video = YouTube(url).streams.first()
		video.download()    
		messagebox.showinfo('', 'Download completed!')
    except Exception as e:
        messagebox.showinfo('', f'Download failed!\n{e}')
		  

if __name__ == '__main__':
    create_app()