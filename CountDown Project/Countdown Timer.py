#Countdown
import time


def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,end="\r")
        time.sleep(1)
        t=t-1
    
    print("Time is up!")


t=input("\nEnter the Countdown time: ")
countdown_timer(int(t))
