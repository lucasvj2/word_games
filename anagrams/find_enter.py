import cv2
import numpy as np
import pyautogui
from common.tile import Tile

def capture_screen():
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def find_enter_button(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_purple = np.array([122, 42, 170])
    upper_purple = np.array([128, 52, 195])
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if 4.5 < w / h < 5.5:
            return (x, y, w, h)
    
    return (-1, -1, -1, -1)

def get_enter():
    image = capture_screen()
    x, y, w, h = find_enter_button(image)
    if x == -1 and y == -1 and w == -1 and h == -1:
        return None
    return Tile(" ", x, y, w, h)


