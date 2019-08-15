/**
    Plays song when it's time to wake up. Input required hour and minute from user and keeps the loop running until its time for alaram.
    It requires path to any song or music file in computer system in order to play music.
**/

import time
import os

not_executed = 1

try:
	hour = int(input("At what hour? "))
	minute = int (input("At what minute? "))
except ValueError:
	print ("It's not an integer")
while(not_executed):
	dt = list(time.localtime())
	dthour = dt[3]
	dtminute = dt[4]
	if dthour == hour and dtminute == minute:
		print ("Wake UP! It's",hour,":",minute)
		os.startfile("C:\\Users\\XYZ\\Music\\Songs\\Ed Sheeran - Shape of You.mp3")
		not_executed = 0
        
