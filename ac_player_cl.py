#!/usr/bin/python

# Play the Animal Crossing: New Leaf soundtrack in your command
# line according to the date, weather, and time of day!

import sched
import subprocess
import time 

class AcPlayer:
    def __init__(self,time):
        self.song = ''
        self.time = datetime.datetime.now().hour
        # Paths for songs depending on weather
        self.clear_path = os.getcwd() + '/assets/songs/time/clear/'
        self.rainy_path = os.getcwd() + '/assets/songs/time/rainy/'
        self.snowy_path = os.getcwd() + '/assets/songs/time/snowy/'

    def display_info(self):
        print('It is currently {} o\'clock'.format(self.time))

    def play(self):
        subprocess.call('mplayer', self.song)

    def update(self):
        self.time = datetime.datetime.now().hour
        self.song = self.clear_path + self.time + '.mp3'
        
def main():
    print('ANIMAL CROSSING: NEW LEAF PLAYER')
    print( '****** command line edition!')
    scheduler = sched.scheduler(time.time, time.sleep)


if __name__ == '__main__':
    main()
