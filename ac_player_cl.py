#!/usr/bin/python

# Play the Animal Crossing: New Leaf soundtrack in your command
# line according to the date, weather, and time of day!

import datetime
import os
import requests
import subprocess
import time

# Add your OpenWeatherMap API key here!
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q=NewYork&APPID='
WEATHER_API_KEY = ''

class AcPlayer:
    def __init__(self):
        self.song = ''
        self.time = None
        self.weather = ''
        # Paths for songs depending on weather
        self.clear_path = os.getcwd() + '/assets/songs/time/clear/'
        self.rainy_path = os.getcwd() + '/assets/songs/time/rainy/'
        self.snowy_path = os.getcwd() + '/assets/songs/time/snowy/'
        self.get_weather()

    def display_info(self):
        print('It is currently {} o\'clock and {}.'.format(self.time, self.weather))

    def get_weather(self):
        response = requests.get(WEATHER_URL + WEATHER_API_KEY).json()
        self.weather = response['weather'][0]['main']

    def play(self):
        playing = subprocess.call(['mplayer', self.song, '/dev/null'], stdout=subprocess.PIPE)

    def update(self):
        time = datetime.datetime.now().hour

        if time != self.time:
            self.time = time
            if self.weather == 'Rain':
                self.song = self.rainy_path + str(self.time) + '.mp3'
            elif self.weather == 'Snow':
                self.song = self.snowy_path + str(self.time) + '.mp3'
            else:
                self.song = self.clear_path + str(self.time) + '.mp3'
            self.display_info()

def main():
    print('ANIMAL CROSSING: NEW LEAF PLAYER')
    print( '****** command line edition!')
    player = AcPlayer()

    while 1:
        player.update()
        player.play()

if __name__ == '__main__':
    main()
