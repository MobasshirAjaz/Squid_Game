#INITIAL SETUP
#----------------------------------------------------------------
import time
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import os
folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
intro = graphic[0];
kill = graphic[1];
winner = graphic[2];
TIMER_MAX = 60
TIMER = TIMER_MAX
maxMove = 6500000
#sets the minimum confidence threshold for the detection
cv2.imshow('CookieCutter', cv2.resize(intro, (0, 0), fx=1, fy=1))
cv2.waitKey(1)
while True:
    cv2.imshow('CookieCutter', cv2.resize(intro, (0, 0), fx=1, fy=1))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------
folderPath = 'img'
mylist = os.listdir(folderPath)
graphic1 = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
mlsa = graphic1[0];
sqr_img = graphic1[1];
#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
gameOver = False
NotWon =True
#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
#while not gameOver:
#      continue
#win = False
cam = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
win = True
while True:
# Get image frame
    success, img = cam.read()
# Find the hand and its landmarks
    #frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(img) # with draw
#hands = detector.findHands(img, draw=False) # without draw
    img = np.fliplr(img)
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)

            # Find Distance between two Landmarks. Could be same hand or different hands
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
    # Display
    cv2.imshow("Camera", img)
    cv2.imshow("Shape", sqr_img)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
if not win:
    for i in range(10):
        cv2.imshow('CookieCutter', cv2.resize(kill, (0, 0), fx=1, fy=1))
    while True:
       if cv2.waitKey(10) & 0xFF == ord('q'):
            break
else:
   cv2.imshow('Squid Game', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
   cv2.waitKey(125)
   while True:
        cv2.imshow('Squid Game', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
        #cv2.imshow('shit',cv2.resize(graphic[3], (0, 0), fx = 0.5, fy = 0.5))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()