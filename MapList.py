import map
import numpy as np

MapList = []
song0 = map.Map("Songs\_dynamite.ogg", "Dynamite", "방탄소년단", 5)
song1 = map.Map("Songs\_shelter.mp3", "Shelter", "Porter Robinson", 2)
song2 = map.Map("Songs\_hot air balloon.mp3","Hot Air balloon", "Owl City", 6)
song3 = map.Map("Songs\_girl.mp3","Uptown Girl", "Billy Joel", 3)

MapList.append(song0) # add song
MapList.append(song1)
MapList.append(song2)
MapList.append(song3)

def load_notes(song, npy): # load notes array
    track = np.load(npy)
    
    for message in track:
        song.add_note(message[0], message[1])

load_notes(song0, "Songs\_dynamite.npy") # assign notes to song
load_notes(song1, "Songs\_shelter.npy")
load_notes(song2, "Songs\_hot air balloon.npy")
load_notes(song3, "Songs\_girl.npy")