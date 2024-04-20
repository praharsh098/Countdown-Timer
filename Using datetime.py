# using datetime module

import datetime
import pygame
pygame.mixer.init()  # to use mixer functions
times_up_sound = pygame.mixer.sound('2.mp3')
start_time = datetime.datetime.now()
countdown_time = 5  # Set the countdown time (in seconds)

while True:
    current_time = datetime.datetime.now()
    elapsed_time = current_time - start_time
    remaining_time = max(countdown_time - elapsed_time.total_seconds(), 0)

    mins, secs = divmod(int(remaining_time), 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')

    if remaining_time <= 0:
        #play the sound
        times_up_sound.play()
        
        while pygame.mixer.get_busy():
            pygame.time.clock().tick(2)
    
    print("Time's up!")
    break
    