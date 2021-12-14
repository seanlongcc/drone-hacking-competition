#team 2
from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()	

#to take picture
tello.streamon()
frame_read= tello.get_frame_read()

#takeoff
tello.takeoff()

#TAKE PICTURE OF WALL AT D
def task1():
	#turn right 90
	tello.rotate_clockwise(90)

	#take a picture of D
	cv2.imwrite("team2.png", frame_read.frame)

	#turn right 90
	tello.rotate_clockwise(90)

#FLY OVER POINT C AND ROTATE THE DRONE 360 DEGREES
def task2():
	#fly back
	tello.move_back(40)

	#rotate 360
	tello.rotate_clockwise(360)

	#fly forward
	tello.move_forward(40)

#FLY OVER POINT B AND DO A FLIP
def task3():
	#move left
	tello.move_left(40)

	#do a flip
	tello.flip("r")

	#move right
	tello.move_right(40)

#FLY OVER POINT A AND LAND THE DRONE
def task4():
	#fly forward
	tello.move_forward(50)

	#land
	tello.land()
	
while True:
    key = input()
    if key == "0": # ESC
        break
    elif key == '1':
        task1()
    elif key == '2':
    	task2()
    elif key == '3':
    	task3()
    elif key == '4':
    	task4()

#land
tello.land()