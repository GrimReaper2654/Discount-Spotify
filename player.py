import os
import pygame
import random
import threading
import copy
from mutagen.mp3 import MP3

lastSongs = []

def stopMusic():
    input("Press Enter to stop the music.\n")
    pygame.mixer.music.stop()
    pygame.mixer.quit()

def removeArray(arr, toRemove):
    for element in toRemove:
        if element in arr:
            arr.remove(element)
    return arr

def chooseSong(p):
    playlist = copy.deepcopy(p)
    length = len(playlist)
    if length > 3:
        playlist = removeArray(playlist, lastSongs)
    chosen = random.choice(playlist)
    lastSongs.append(chosen)
    if len(lastSongs) > min(length-2, 5):
        lastSongs.pop(0)
    return chosen

def MP3Player(playlistName='playlist'):
    directory = os.path.dirname(os.path.abspath(__file__))
    playlistFolder = os.path.join(directory, playlistName)

    pygame.mixer.init()

    playlist = [f for f in os.listdir(playlistFolder) if f.endswith('.mp3')]

    if len(playlist) == 0:
        print("No songs found in playlist. Check that all files are .mp3")
        return

    quitPlayer = threading.Thread(target=stopMusic)
    quitPlayer.start()

    while (1):
        song = chooseSong(playlist)
        songPath = os.path.join(playlistFolder, song)

        audio = MP3(songPath)
        duration = audio.info.length

        print(f"Now playing: {song}")
        pygame.mixer.music.load(songPath)
        pygame.mixer.music.play()
        pygame.time.wait(int(duration * 1000))
        pygame.mixer.music.stop()

MP3Player()