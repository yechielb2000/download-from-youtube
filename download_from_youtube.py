from pytube import YouTube
from tkinter.font import BOLD
from tkinter import *
import os
import threading
import getpass

root = Tk()

entry = Entry(root, font=BOLD)
entry.grid(row=0, column=1,  padx=10, pady=20)

update_label = Label(root, foreground='black', background='#856ff8', font=BOLD)
update_label.grid(row=1,column=1)  


def main():
    root.geometry("580x200") 
    root.resizable(False, False)
    root.title('Download from youtube')
    root.configure(background='#856ff8')

    label = Label(root, text="Enter youtube link :", foreground='black', background='#856ff8', font=BOLD)
    label.grid(row=0,column=0,  padx=10, pady=20)
    
   
    button = Button(root, text="Download", background='#856ff8', foreground='black', font=BOLD, command=lambda:thread(entry.get(), 'C:/Users/{}/Downloads'.format(getpass.getuser())))
    button.grid(row=0, column=3, padx=10, pady=20)
    

    root.mainloop()

def thread(videourl, path):
    update_label.configure(text='downloading..')
    t1 = threading.Thread(target=downloadYouTube, args=(videourl, path))
    t1.start()

def downloadYouTube(videourl, path):
     
    try:
        yt = YouTube(videourl)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().get_highest_resolution()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)
        update_label.configure(text='download successfully!')
    except:
        update_label.configure(text='download failed!')


if __name__ == '__main__':
    main()