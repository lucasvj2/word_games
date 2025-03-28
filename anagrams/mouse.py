from Quartz.CoreGraphics import CGEventCreateMouseEvent, CGEventPost
from Quartz.CoreGraphics import kCGEventLeftMouseDown, kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft, kCGHIDEventTap
import time

def mouse_event(type, pos):
    x, y = pos
    event = CGEventCreateMouseEvent(None, type, (x, y), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, event)

def scale(x):  # Retina fix
    return x / 2

def click_path(path):
    if not path:
        return

    for tile in path:
        pos = (scale(tile.xc), scale(tile.yc))
        mouse_event(kCGEventLeftMouseDown, pos)
        time.sleep(0.02)
        mouse_event(kCGEventLeftMouseUp, pos)
        time.sleep(0.05)
