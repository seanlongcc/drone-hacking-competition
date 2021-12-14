#team 1
import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()	

#to take picture
tello.streamon()
frame_read= tello.get_frame_read()

#takeoff
tello.takeoff()

#TAKE PICTURE OF WALL AT B
#turn left 90
tello.rotate_counter_clockwise(90)

#take a picture of B
cv2.imwrite("team1.png", frame_read.frame)

#turn right 90
tello.rotate_clockwise(90)

#FLY OVER POINT A AND ROTATE THE DRONE 360 DEGREES
#fly forward
tello.move_forward(40)

#rotate 360
tello.rotate_clockwise(360)

#move back
tello.move_back(40)

#FLY OVER POINT D AND DO A FLIP
#fly right
tello.move_right(40)

#do a flip
tello.flip("r")

#fly left
tello.move_left(40)

#FLY OVER POINT C AND LAND THE DRONE
#fly back
tello.move_back(40)

#land
tello.land()