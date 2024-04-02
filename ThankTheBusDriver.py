import cv2
import numpy
import win32api
import time
import pyautogui
from PIL import ImageGrab, Image, ImageFilter

def find_pattern(target, threshold=0.95, show=False):
        targ_points = []

        cv_targ = cv2.imread(target)
        _, targ_w, targ_h = cv_targ.shape[::-1]

        sc_w = win32api.GetSystemMetrics(0)
        sc_h = win32api.GetSystemMetrics(1)
        # Grabs a screenshot from your main screen.
        im = ImageGrab.grab((0,0, sc_w, sc_h))
        # Converts the image into an edge detected one.
        im = im.convert("L")
        im = im.filter(ImageFilter.FIND_EDGES)
        cv_im = numpy.array(im)
        cv_im = cv2.cvtColor(cv_im, cv2.COLOR_RGB2BGR)

        res = cv2.matchTemplate(cv_im, cv_targ, cv2.TM_CCOEFF_NORMED)
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            if show:
                cv2.rectangle(cv_im, pt, (pt[0] + targ_w, pt[1] + targ_h), (0,255,0), 2)
            print('Found {img} at ({}x, {}y)'.format(pt[0], pt[1], img=target))
            targ_points.append(pt)

        if show:
            cv2.imshow('Result', cv_im)
            cv2.waitKey()

        return targ_points

# Has to be based on windows resolution. Not just game resolution.
if (win32api.GetSystemMetrics(0) == 1920 and win32api.GetSystemMetrics(1) == 1080):
    target = "target1080p.bmp"
else:
    # Goes to 1440.
    target = "target.bmp"

#Pyautogui has a failsafe, but that only affects if it's touching the mouse, which it isn't.
pyautogui.FAILSAFE = False

#Only works for letters a-z and numbers. Won't work with prntscrn, ctrl, tab, etc.
keybind = input("Enter emote keybind: ")

while True:
    # Function returns a list of coordinates, if the len is greater than 0, it found a target.
    if len(find_pattern(target)) > 0:
        # Emote keybind.
        pyautogui.press(keybind)
        time.sleep(5)