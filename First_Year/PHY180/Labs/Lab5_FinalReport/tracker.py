import cv2
import numpy as np
import time
from matplotlib import pyplot as plt
import atexit
from scipy import signal

def nothing(val):
    pass

def exit_handler():

    x_pos_arr = np.asarray(ball_x)
    time_arr = np.asarray(ball_t)
    np.savetxt("MassTest_" + name + "_pos.csv", x_pos_arr, delimiter=",")
    np.savetxt("MassTest_" + name + "_time.csv", time_arr, delimiter=",")
    # np.savetxt("first_200_x_pos_pixels.csv", x_pos_arr, delimiter=",")
    # np.savetxt("first_200_times.csv", time_arr, delimiter=",")
    #print(sum(ball_x)/len(ball_x))
    #print(sum(ball_y)/len(ball_y))
    #print(len(ball_r))

    plt.plot(ball_t, ball_x)
    plt.show()
 
def initialize_trackbars():
    global hh, hl, sh, sl, vh, vl, wnd

    cv2.namedWindow("Colorbars") 
    
    hh='Hue High'
    hl='Hue Low'
    sh='Saturation High'
    sl='Saturation Low'
    vh='Value High'
    vl='Value Low'

    wnd = 'Colorbars'

    cv2.createTrackbar(hl, wnd,0,179,nothing)
    cv2.createTrackbar(hh, wnd,0,179,nothing)
    cv2.createTrackbar(sl, wnd,0,255,nothing)
    cv2.createTrackbar(sh, wnd,0,255,nothing)
    cv2.createTrackbar(vl, wnd,0,255,nothing)
    cv2.createTrackbar(vh, wnd,0,255,nothing)

def initialize():
    global cap, origin_px, meter_per_px, name
    #cap = cv2.VideoCapture(2)
    cap = cv2.VideoCapture("videos\MassTest_508.97g.mp4")
    name = "194.2cm"
    #initialize_trackbars()
    atexit.register(exit_handler)


def find_ball(frame, show_trackbars = False):
    frame = cv2.GaussianBlur(frame, (7, 7), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hul, huh, sal, sah, val, vah = 0, 9, 205, 255, 56, 255

    hul, huh, sal, sah, val, vah = 23, 40, 126, 255, 127, 255 #rob vals

    if show_trackbars:
        hul=cv2.getTrackbarPos(hl, wnd)
        huh=cv2.getTrackbarPos(hh, wnd)
        sal=cv2.getTrackbarPos(sl, wnd)
        sah=cv2.getTrackbarPos(sh, wnd)
        val=cv2.getTrackbarPos(vl, wnd)
        vah=cv2.getTrackbarPos(vh, wnd)

    HSVLOW = np.array([hul, sal, val])
    HSVHIGH = np.array([huh, sah, vah])
    thresh = cv2.inRange(hsv, HSVLOW, HSVHIGH)
    floodfill = thresh.copy()
    h, w = thresh.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(floodfill, mask, (0,0), 255)
    floodfill_inv = cv2.bitwise_not(floodfill)
    thresh_filled = thresh | floodfill_inv    
    edged = cv2.Canny(thresh_filled, 30, 200)
    all_contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    filtered_contours = []

    for contour in all_contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        if abs(max(w, h)/min(w, h)) < 1.5:
            if area > 100:
                filtered_contours.append(contour) 
                break

    if len(filtered_contours) < 1:
        return -1, -1, -1, thresh_filled

    ball_contour = filtered_contours[0]
    center, radius = cv2.minEnclosingCircle(ball_contour)
    
    return int(center[0]), int(center[1]), int(radius), thresh_filled
    
def main():
    global ball_t, ball_x, ball_r, ball_y
    ball_t, ball_x, ball_r, ball_y = [], [], [], []

    i = 0
    while(i < 1): # i < number_of_frams
        i += 1
        print(i)
        ret,frame = cap.read()
        time_stamp = cap.get(cv2.CAP_PROP_POS_MSEC)/1000
        x_px, y_px, radius, thresh = find_ball(frame, show_trackbars = False)

        if x_px > -1:
            # x_relative_to_origin = x_px - origin_px
            # y_relative_to_origin = y_px - origin_py
            # x_relative_m = x_relative_to_origin*meter_per_px
            # y_relative_m = y_relative_to_origin*meter_per_px
            ball_t.append(time_stamp)
            ball_x.append(y_px)
            #ball_r.append(radius)
            #ball_y.append(y_px)
            cv2.circle(frame, (x_px, y_px), radius, (0, 255, 0), 2)
            cv2.circle(frame, (x_px, y_px), 2, (255, 0, 0), 2)
        
        cv2.imshow("contours", frame)
        cv2.imshow("thresh", thresh)
        if(cv2.waitKey(5) & 0xFF == ord("q")):
            break
        # Winow view of trackers
    
    cap.release()
    cv2.destroyAllWindows()

ball_radius_px = 35
ball_radius_m = 0.06477
meter_per_px = ball_radius_m/ball_radius_px

meter_per_px = 0.8128 / 1920
origin_px = 66


if __name__ == "__main__":
    initialize()
    main()