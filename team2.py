#team 2
import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()	

#to take picture
tello.streamon()
frame_read= tello.get_frame_read()

#takeoff
tello.takeoff()

#TAKE PICTURE OF WALL AT D
#turn right 90
tello.rotate_clockwise(90)

#take a picture of D
cv2.imwrite("team2.png", frame_read.frame)

#turn right 90
tello.rotate_clockwise(90)

#FLY OVER POINT C AND ROTATE THE DRONE 360 DEGREES
#fly back
tello.move_back(40)

#rotate 360
tello.rotate_clockwise(360)

#fly forward
tello.move_forward(40)

#FLY OVER POINT B AND DO A FLIP
#move left
tello.move_left(40)

#do a flip
tello.flip("r")

#move right
tello.move_right(40)

#FLY OVER POINT A AND LAND THE DRONE
#fly forward
tello.move_forward(50)

#land
tello.land()