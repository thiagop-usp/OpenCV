import cv2
import numpy as np
import matplotlib as plt

#reads both the full image and the template thats going to be looked for
#0 means grayscale
frnds = cv2.imread('friends.jpg', 0)
tmpt = cv2.imread('chandler.jpg', 0)

#finding resolutions
imgh, imgw = frnds.shape
tmph, tmpw = tmpt.shape

cv2.imshow('friends', frnds)
cv2.imshow('chandler', tmpt)

#matches the full image with the template
match = cv2.matchTemplate(frnds, tmpt, 3);
minv, maxv, minl, maxl = cv2.minMaxLoc(match)

#finding edges of the match
top_left = maxl
bottom_right = (maxl[0] + tmpw, maxl[1] + tmph)

#drawing rectangle on the match to see if it's right (255 = white, 2 = thickness)
cv2.rectangle(frnds, top_left, bottom_right, 255, 2)

#showing result
cv2.imshow('matching', frnds)
key = cv2.waitKey(0)
#waits for ESC key to be pressed to leave
if key == 27:
    cv2.destroyAllWindows()
