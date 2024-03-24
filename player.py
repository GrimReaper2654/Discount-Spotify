import os
import pygame
import random
from mutagen.mp3 import MP3

def play_random_song_in_playlist_folder():
    # Get the path to the 'playlist' folder in the same directory as the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    playlist_folder = os.path.join(script_directory, 'playlist')

    # Initialize the music player
    pygame.mixer.init()
    
    # Set the volume (optional)
    pygame.mixer.music.set_volume(0.5)

    # Get a list of music files in the 'playlist' folder
    music_files = [f for f in os.listdir(playlist_folder) if f.endswith('.mp3')]

    if len(music_files) == 0:
        print("No music files found in the 'playlist' folder.")
        return

    # Randomly select a music file from the 'playlist' folder
    random_music_file = random.choice(music_files)
    music_path = os.path.join(playlist_folder, random_music_file)
    
    # Get the duration of the selected music file
    audio = MP3(music_path)
    music_duration = audio.info.length
    
    # Load and play the selected music file
    print(f"Now playing: {random_music_file}")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()

    # Wait for the music file to finish playing
    pygame.time.wait(int(music_duration * 1000))  # Convert duration to milliseconds

    # Clean up after playing
    pygame.mixer.music.stop()
    pygame.mixer.quit()
