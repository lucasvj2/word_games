import cv2
import numpy as np

def show_hsv_values(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel = hsv[y, x]
            print(f"HSV at ({x},{y}): {pixel}")  # pixel is [H, S, V]

    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", mouse_callback)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread("./test_images/anagrams.png")  # or use your capture_screen()
show_hsv_values(image)