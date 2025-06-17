import pygame

def check_speaker():
    print("\nTesting Speaker (Playing sound)...")
    pygame.mixer.init()
    pygame.mixer.music.load("test_01.wav")  # Add your test_sound.mp3 in the directory.
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    print("Speaker playback completed.")
