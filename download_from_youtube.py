from pytube import YouTube
from tkinter.font import BOLD
from tkinter import *
import os
import threading
import getpass

SELECTION = ['Highest quality', 'Regular quality', 'Lowest quality']
row0 = 0; row1 = 1; row2 = 2
YELLOW_COLOR = '#f5e149'
BLACK_COLOR = 'black'

root = Tk()

entry = Entry(root, font=BOLD)
entry.grid(row=row2, column=1, padx=10, pady=20)

optionVar = StringVar()
optionVar.set(SELECTION[1])
options = OptionMenu(root, optionVar, *SELECTION)
options.config(font=BOLD, background=YELLOW_COLOR, width=12)
options.grid(row=row1,column=0)

update_label = Label(root, foreground=BLACK_COLOR, background=YELLOW_COLOR, font=BOLD)
update_label.grid(row=1,column=1)  

def main():
    root.geometry("580x200") 
    root.resizable(False, False)
    root.title('Download from youtube')
    root.configure(background=YELLOW_COLOR)

    highlight = Label(root, text="Download from Youtube!", foreground=BLACK_COLOR, background=YELLOW_COLOR, font=BOLD)
    highlight.grid(row=row0,column=1,  padx=10, pady=20)

    label = Label(root, text="Enter youtube link :", foreground=BLACK_COLOR, background=YELLOW_COLOR, font=BOLD)
    label.grid(row=row2,column=0,  padx=10, pady=20)

    button = Button(root, text="Download", background=YELLOW_COLOR, foreground=BLACK_COLOR, font=BOLD, command=lambda:thread(entry.get(), 'C:/Users/{}/Downloads'.format(getpass.getuser())))
    button.grid(row=row2, column=3, padx=10, pady=20)
    
    root.mainloop()

def thread(videourl, path):

    print(optionVar.get())

    update_label.configure(text='downloading..')
    t1 = threading.Thread(target=downloadYouTube, args=(videourl, path))
    t1.start()

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