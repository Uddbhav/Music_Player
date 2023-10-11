from tkinter import *
import os
from pygame import *

root = Tk()

# Configure row and column weights
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Set window dimensions
width, height = 600, 500
x = (root.winfo_screenwidth() - width) // 2
y = (root.winfo_screenheight() - height) // 4

# Set geometry
root.geometry(f'{width}x{height}+{x}+{y}')

# Navigating through windows
window = Frame(root)
window2 = Frame(root)

for frame in (window, window2):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(window)

window.config(background='#7852E6')

back = PhotoImage(file="F:/VS Code/Python/Music Player/images/back.png")
image_1 = Label(window,bg='#7852E6',image=back)
image_1.place(x=41,y=41)

image_image_1 = PhotoImage(file="F:/VS Code/Python/Music Player/images/image_2.png")
image_2 = Label(window,bg='#7852E6',image=image_image_1)
image_2.place(x=60,y=340)

drake_img = PhotoImage(file="F:/VS Code/Python/Music Player/images/drake.png")
image_3 = Label(window,bg='#7852E6',image=drake_img)
image_3.place(x=203, y=131)

play_button = PhotoImage(file="F:/VS Code/Python/Music Player/images/play.png")
button_2 = Button(window, image=play_button, borderwidth=0, highlightthickness=0, command=lambda: play(), 
            relief="flat", activebackground='#7852E6')
button_2.place(x=243, y=386.0, width=80.0, height=81.0)

next_button = PhotoImage(file="F:/VS Code/Python/Music Player/images/next.png")
button_3 = Button(window, image=next_button, borderwidth=0, highlightthickness=0, command=lambda: next_song(), 
                relief="flat", activebackground='#7852E6')
button_3.place(x=355, y=397.0, width=74.0, height=56.0)

pre_button = PhotoImage(file="F:/VS Code/Python/Music Player/images/previous.png")
button_4 = Button(window, image=pre_button, borderwidth=0, highlightthickness=0, command=lambda: previous_song(), 
                relief="flat", activebackground='#7852E6')
button_4.place(x=137, y=398.0, width=74.0, height=56.0)

playlist_button = PhotoImage(file="F:/VS Code/Python/Music Player/images/playlist.png")
button_5 = Button(window, image=playlist_button, borderwidth=0, highlightthickness=0, 
                command=lambda: show_frame(window2), relief="flat", activebackground='#7852E6')
button_5.place(x=49, y=378.0, width=76.0, height=32.0)

playing_song = Label(window, text="", bg='#7852E6', fg='#ffffff', font=('yu gothic ui', 8, 'bold'))
playing_song.place(x=150,y=360, height=20, width=300)

window2.config(background='#7852E6')

button_image_6 = PhotoImage(file="F:/VS Code/Python/Music Player/images/play.png")
button_6 = Button(window2, image=button_image_6, borderwidth=0, highlightthickness=0, command=lambda: call_play(),
                 relief="flat", activebackground='#7852E6')
button_6.place(x=100.0, y=2.0, width=80.0, height=80.0)

def call_play():
    show_frame(window)
    play()

button_7 = Button(window2, text="""BACK""", borderwidth=0, highlightthickness=0, command=lambda: show_frame(window),
         relief="flat", activebackground='#000000', bg='#000000', fg='#ffffff')
button_7.place(x=26.0, y=25.0, width=54.0, height=33.0)

listbox = Listbox(window2, selectmode=SINGLE, bg='#000000', fg='#ffffff', font=('yu gothic ui', 10, 'bold'), 
                    bd=25, relief='flat')
listbox.place(x=30, y=80, height=406, width=520)

scroll = Scrollbar(window2)
scroll.place(x=550, y=80, height=406)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

os.chdir(r'F:/VS Code/Python/Music Player/songs')
songs = os.listdir()

button_image_1 = PhotoImage(file="F:/VS Code/Python/Music Player/images/pause.png")

def play():
    current_song = listbox.get(ACTIVE)
    playing_song['text'] = current_song
    mixer.music.load(current_song)
    mixer.music.play()

    button_1 = Button(window, image=button_image_1, borderwidth=0, highlightthickness=0,
        command=lambda: pause_song(), relief="flat", activebackground='#7852E6')
    button_1.place(x=241, y=385.0, width=80.0, height=81.0)

resume_pic = PhotoImage(file="F:/VS Code/Python/Music Player/images/play.png")

def pause_song():
    mixer.music.pause()

    resume_button = Button(window, image=resume_pic, borderwidth=0, highlightthickness=0,
        command=lambda: resume_song(), relief="flat", activebackground='#7852E6')
    resume_button.place(x=243, y=386.0, width=80.0, height=81.0)

def resume_song():
    mixer.music.unpause()
    button_1 = Button(window, image=button_image_1, borderwidth=0, highlightthickness=0,
        command=lambda: pause_song(), relief="flat", activebackground='#7852E6')
    button_1.place(x=241, y=385.0, width=80.0, height=81.0)

def next_song():
    playing = playing_song['text']
    index = songs.index(playing)
    next_index = index + 1
    playing = songs[next_index]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0, END)
    song_list()
    listbox.select_set(next_index)
    playing_song['text'] = playing

def previous_song():
    playing = playing_song['text']
    index = songs.index(playing)
    next_index = index - 1
    playing = songs[next_index]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0, END)
    song_list()
    listbox.select_set(next_index)
    playing_song['text'] = playing

def song_list():
    for i in songs:
        listbox.insert(END, i)

song_list()

mixer.init()
songs_state = StringVar()

root.resizable(False, False)
root.mainloop()