from pytube import YouTube
from tkinter.font import BOLD
from tkinter import *
import threading
import getpass
import os

row0 = 0; row1 = 1; row2 = 2
color = '#FFAE42'

root = Tk()

update_label = Label(root, foreground='black', background=color, font=BOLD)
update_label.grid(row=row2,column=1)  

def main():
    root.geometry("580x200") 
    root.resizable(False, False)
    root.title('Download from YouTube')
    root.configure(background=color)
    
    highlight = Label(root, text="Download from Youtube!", foreground='black', background=color, font=BOLD)
    highlight.grid(row=row0,column=1,  padx=10, pady=20)

    label = Label(root, text="Enter youtube link :", foreground='black', background=color, font=BOLD)
    label.grid(row=row1,column=0,  padx=10, pady=20)

    entry = Entry(root, font=BOLD)
    entry.grid(row=row1, column=1, padx=10, pady=20)

    button = Button(root, text="Download", background=color, foreground='black', font=BOLD, command=lambda:thread(entry.get(), 'C:/Users/{}/Downloads'.format(getpass.getuser())))
    button.grid(row=row1, column=2, padx=10, pady=20)
    
    root.mainloop()

def thread(videourl, path):
    update_label.configure(text='downloading to\n' + path)
    t1 = threading.Thread(target=downloadYouTube, args=(videourl, path,))
    t1.start()

def downloadYouTube(videourl, path):
    try:
        youTube = YouTube(videourl)
       
        if not os.path.exists(path):
            os.makedirs(path)

        youTube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().get_highest_resolution().download(path)
        update_label.configure(text='download successfully!')
    except Exception as ex:
        print(type(ex).__name__, ex.args)
        update_label.configure(text='download failed!')
   
if __name__ == '__main__':
    main()