from djitellopy import Tello
import cv2, math, time
import threading

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    #In reality you want to display frames in a seperate thread. Otherwise
    #they will freeze while the drone moves.
    #if doesnt work, remove **********************************************
    def getImage():
        img = frame_read.frame
        cv2.imshow("drone", img)

    getImageThread = threading.Thread(target = getImage, daemon = True)
    getImageThread.start()
    getImage()
    #*********************************************************************
    '''
    img = frame_read.frame
    cv2.imshow("drone", img)
    '''

    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.rotate_counter_clockwise(90)
    elif key == ord('d'):
        tello.rotate_clockwise(90)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('t'):
        cv2.imwrite("dronecomp.png", frame_read.frame)
    elif key == ord('f'):
        tello.flip("r")    
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('v'):
        tello.move_down(30)

tello.land()
