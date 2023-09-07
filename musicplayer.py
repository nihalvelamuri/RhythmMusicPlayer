from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog


def update_display_size():
    new_height = int(height_entry.get())
    new_width = int(width_entry.get())
    songs_list.config(height=new_height, width=new_width)
    
    
def addsongs():
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))
    for s in temp_song:
        #add your song path here
        s = s.replace("C:/Users/NehaN/Desktop/Songs/", "")
        songs_list.insert(END, s)
    
    # Start playing the first song added
    if not mixer.music.get_busy():
        Play()

def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])

def Play():
    song = songs_list.get(ACTIVE)
    #add your song path here
    song = f'C:/Users/NehaN/Desktop/Songs/{song}'
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def Resume():
    mixer.music.unpause()

def Previous():
    current_song_index = songs_list.curselection()
    if not current_song_index:
        return
    
    current_song_index = current_song_index[0]
    if current_song_index == 0:
        return
    
    previous_song_index = current_song_index - 1
    previous_song = songs_list.get(previous_song_index)
    #add your song path here
    mixer.music.load(f'C:/Users/NehaN/Desktop/Songs/{previous_song}')
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(previous_song_index)
    songs_list.selection_set(previous_song_index)

def Next():
    current_song_index = songs_list.curselection()
    if not current_song_index:
        return
    
    current_song_index = current_song_index[0]
    if current_song_index == songs_list.size() - 1:
        return
    
    next_song_index = current_song_index + 1
    next_song = songs_list.get(next_song_index)
    mixer.music.load(f'C:/Users/NehaN/Desktop/Songs/{next_song}')
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(next_song_index)
    songs_list.selection_set(next_song_index)

root = Tk()
root.title('Rhythm Music Player')
mixer.init()

display_frame = Frame(root)
display_frame.grid(row=0, column=0, columnspan=6)

height_label = Label(display_frame, text="Enter Height:")
height_label.pack(side=LEFT)
height_entry = Entry(display_frame, width=2)
height_entry.insert(0, "12")  # Default height
height_entry.pack(side=LEFT)

comment_label = Label(display_frame, text="Click on song", font = ('Times', 14, 'bold', 'underline'), fg = ('red'))
comment_label.pack(side=LEFT)

width_label = Label(display_frame, text="Enter Width:")
width_label.pack(side=LEFT)
width_entry = Entry(display_frame, width=2)
width_entry.insert(0, "47")  # Default width
width_entry.pack(side=LEFT)

update_button = Button(display_frame, text="Update Display Size", command=update_display_size)
update_button.pack(side=LEFT)

songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), selectbackground="gray", selectforeground="black")
songs_list.config(height=12, width=47)  # Default height and width
songs_list.grid(row=1, column=0, columnspan=6)

defined_font = font.Font(family='Helvetica')

play_button = Button(root, text="Play", width=10, height=2, command=Play, bg="green", fg="white", bd=0, activebackground="green", activeforeground="white")
play_button.grid(row=2, column=0)

pause_button = Button(root, text="Pause", width=10, height=2, command=Pause, bg="blue", fg="white", bd=0, activebackground="blue", activeforeground="white")
pause_button.grid(row=2, column=1)

stop_button = Button(root, text="Stop", width=10, height=2, command=Stop, bg="red", fg="white", bd=0, activebackground="red", activeforeground="white")
stop_button.grid(row=2, column=2)

Resume_button = Button(root, text="Resume", width=10, height=2, command=Resume, bg="orange", fg="white", bd=0, activebackground="orange", activeforeground="white")
Resume_button.grid(row=2, column=3)

previous_button = Button(root, text="Prev", width=10, height=2, command=Previous, bg="purple", fg="white", bd=0, activebackground="purple", activeforeground="white")
previous_button.grid(row=2, column=4)

next_button = Button(root, text="Next", width=10, height=2, command=Next, bg="teal", fg="white", bd=0, activebackground="cyan", activeforeground="white")
next_button.grid(row=2, column=5)


my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)

mainloop()