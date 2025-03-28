import cv2
import numpy as np
import pyautogui
import torch
from common.model import LetterCNN
from common.tile import Tile
import os

def capture_screen():
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def find_grid_region(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([18, 50, 220])
    upper_green = np.array([19, 80, 250])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    squares = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if 0.9 < w / h < 1.1 and w > 50 and w < 100: #could be different size
            squares.append((x, y, w, h))

    if len(squares) < 6:
        print("Could not find all squares")
        return []
    
    if len(squares) > 6:
        print("Found more than 6 squares, returning first 6")
        
    return squares[:6]

def ocr_cell(cell_img, model, classes):
    # Preprocess image to match model input (grayscale + resize)
    cell = cv2.cvtColor(cell_img, cv2.COLOR_BGR2GRAY)
    _, cell = cv2.threshold(cell, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cell1 = cv2.resize(cell, (64, 64))
    cell1 = cell1.astype(np.float32) / 255.0
    tensor = torch.tensor(cell1).unsqueeze(0).unsqueeze(0) 

    model.eval()
    with torch.no_grad():
        output = model(tensor)
        pred = torch.argmax(output, dim=1).item()
        letter = classes[pred]

    return letter


def get_grid():
    model = LetterCNN()
    model.load_state_dict(torch.load("common/model.pth", map_location=torch.device('cpu')))
    model.eval()
    classes = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    
    image = capture_screen()
    squares = find_grid_region(image)
    if len(squares) == 0:
        return None

    squares.sort() #sort by x val

    grid = []
    for idx, (x, y, w, h) in enumerate(squares):
        x = x + 15
        y = y + 15
        w = w - 26
        h = h - 26
        cell_img = image[y:y+h, x:x+w]
        letter = ocr_cell(cell_img, model, classes)
        grid.append(Tile(letter, x, y, w, h))
        print(letter)

    return grid

