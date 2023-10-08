import pygame

# Initialize pygame
pygame.init()

# Specify the path to your audio file
audio_file_path = "Alarm/growl.mp3"

# Create a pygame mixer
pygame.mixer.init()

# Load the audio file
sound = pygame.mixer.Sound(audio_file_path)

# Play the audio
sound.play()

# Add a delay to allow the sound to play (optional)
pygame.time.delay(1000)  # Delay for 1 second (1000 milliseconds)

# Quit pygame (optional, but recommended)
pygame.quit()