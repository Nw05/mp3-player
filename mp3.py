import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3

root = Tk()
root.minsize(300,300)

listofsongs = []
realnames = []

song_paused = False

v = StringVar()
songlabel = Label(root,textvariable = v,width = 35)

index = 0

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    v.set(realnames[index])
    #return songname

def nextsong():
    global index
    if index + 1 == len(listofsongs):
        index = 0
    else:       
        index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong():
    global index
    if index == 0:
        index = len(listofsongs) - 1
    else:
        index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def pausesong():
    global song_paused
    if song_paused:
        pygame.mixer.music.unpause()
        v.set("Song Unpaused")
        pausebutton.config(text="Pause song")
        song_paused = False
        
    else:
        pygame.mixer.music.pause()
        v.set("Song Paused")
        pausebutton.config(text="Unpause song")
        song_paused = True
    #return songname

def stopsong():
    pygame.mixer.music.stop()
    v.set("")
    #return songname


label = Label(root,text='Music Player')
label.pack()
label.configure(background = "#ffffff")

listbox = Listbox(root)
listbox.pack()
listbox.configure(background = "#ffffff")

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()


nextbutton = Button(root,text = 'Next Song', command=nextsong)
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song', command=prevsong)
previousbutton.pack()

pausebutton = Button(root, text= 'Pause Song', command=pausesong)
pausebutton.pack()

stopbutton = Button(root,text='Stop Music', command=stopsong)
stopbutton.pack()

#all the colors from the buttons and the background from the root 
root.configure(background = "#0000FF")
label.configure(background = "#ffffff")
listbox.configure(background = "#ffffff")
nextbutton.configure(background = "#ffffff")
previousbutton.configure(background = "#ffffff")
pausebutton.configure(background = "#ffffff")
stopbutton.configure(background = "#ffffff")

songlabel.pack()
root.mainloop() 