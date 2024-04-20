# using time.sleep() module

import time


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1


countdown(5)  # Set the countdown time (in seconds)
print("Times up!")
