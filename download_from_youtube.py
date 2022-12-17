from pytube import YouTube
from tkinter.font import BOLD
from tkinter import *
import os
import threading
import getpass
from consts import *
from utils import *


root = Tk()

entry = Entry(root, font=BOLD)
entry.grid(row=row2, column=1, padx=PADDING_X, pady=PADDING_Y)

optionVar = StringVar()
optionVar.set(SELECTION[1])
options = OptionMenu(root, optionVar, *SELECTION)
options.config(font=BOLD, background=YELLOW_COLOR, width=12)
options.grid(row=row1,column=0)

update_label = create_label(root, None)
update_label.grid(row=1,column=1)  

def main():
    root.geometry("580x200") 
    root.resizable(False, False)
    root.title('Download from youtube')
    root.configure(background=YELLOW_COLOR)

    highlight = create_label(root, "Download from Youtube!")
    highlight.grid(row=row0, column=1, padx=PADDING_X, pady=PADDING_Y)
    label = create_label(root, text="Enter youtube link :")
    label.grid(row=row2,column=0,  padx=PADDING_X, pady=PADDING_Y)

    button = Button(root, text="Download", background=YELLOW_COLOR, foreground=BLACK_COLOR, font=BOLD, command=lambda:thread(entry.get(), fr'C:/Users/{getpass.getuser()}/Downloads'))
    button.grid(row=row2, column=3, padx=PADDING_X, pady=PADDING_Y)
    
    root.mainloop()

def thread(videourl, path):
    update_label.configure(text='downloading..')
    downloading_thread = threading.Thread(target=downloadYouTube, args=(videourl, path))
    downloading_thread.start()

def downloadYouTube(videourl, path):
    try:
        yt = YouTube(videourl)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        
        yt = selectResolution(yt)
       
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)
        update_label.configure(text='download successfully!')
    except:
        update_label.configure(text='download failed!')


def selectResolution(yt):
    if(optionVar.get() == SELECTION[0]):
        return yt.get_highest_resolution()
    elif(optionVar.get() == SELECTION[1]):
        return yt.get_by_resolution()
    else:
       return yt.get_lowest_resolution()       

if __name__ == '__main__':
    main()