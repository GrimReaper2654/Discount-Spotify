import os
import pygame
import random
import threading
import copy
import math
import time
from mutagen.mp3 import MP3

lastSongs = []
paused = False
volume = 0.5

def control():
    global paused
    while 1:
        res = input("Press Enter to stop the music or enter command.\n")
        if res == '':
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            print("Stopped MP3 player")
            return
        elif res == 'p':
            if not paused:
                print("Paused MP3 player")
                paused = True
                pygame.mixer.music.pause()
            else:
                print("Unpaused MP3 player")
                paused = False
                pygame.mixer.music.unpause()
        elif res == '+':
            volume = round(min(volume + 0.1, 1), 1)
            print(f"Increased Volume to {volume}")
            pygame.mixer.music.set_volume(volume)
        elif res == '-':
            volume = round(max(volume - 0.1, 0.1), 1)
            print(f"Decreased Volume to {volume}")
            pygame.mixer.music.set_volume(volume)
        

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
    global paused
    directory = os.path.dirname(os.path.abspath(__file__))
    playlistFolder = os.path.join(directory, playlistName)

    pygame.mixer.init()

    playlist = [f for f in os.listdir(playlistFolder) if f.endswith('.mp3')]

    if len(playlist) == 0:
        print("No songs found in playlist. Check that all files are .mp3")
        return

    controlThread = threading.Thread(target=control)
    controlThread.start()

    print("Started MP3 player")
    while (1):
        song = chooseSong(playlist)
        songPath = os.path.join(playlistFolder, song)

        audio = MP3(songPath)
        duration = audio.info.length

        print(f"Now playing: {song}")
        startTime = time.time()
        pygame.mixer.music.load(songPath)
        pygame.mixer.music.play()
        while time.time()-startTime <= duration:
            pygame.time.wait(1000)
            if paused:
                duration += 1
        pygame.mixer.music.stop()

print('loading MP3 player')
MP3Player('playlist')
