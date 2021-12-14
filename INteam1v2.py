#team 1
from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()	

#to take picture
tello.streamon()
frame_read= tello.get_frame_read()

#takeoff
tello.takeoff()

#TAKE PICTURE OF WALL AT B
def task1():
	#turn left 90
	tello.rotate_counter_clockwise(90)

	#take a picture of B
	cv2.imwrite("team1.png", frame_read.frame)

	#turn right 90
	tello.rotate_clockwise(90)

#FLY OVER POINT A AND ROTATE THE DRONE 360 DEGREES
def task2():
	#fly forward
	tello.move_forward(40)

	#rotate 360
	tello.rotate_clockwise(360)

	#move back
	tello.move_back(40)

#FLY OVER POINT D AND DO A FLIP
def task3():
	#move right
	tello.move_right(90)

	#do a flip
	tello.flip("r")

	#move back
	tello.move_left(40)

#FLY OVER POINT C AND LAND THE DRONE
def task4():
	#fly forward
	tello.move_back(50)

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