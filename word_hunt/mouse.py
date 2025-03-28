from Quartz.CoreGraphics import CGEventCreateMouseEvent, CGEventPost
from Quartz.CoreGraphics import kCGEventLeftMouseDown, kCGEventLeftMouseDragged, kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft, kCGHIDEventTap
import time

def mouse_event(type, pos):
    x, y = pos
    event = CGEventCreateMouseEvent(None, type, (x, y), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, event)

def drag_path(path):
    if not path:
        return

    def scale(x): return x / 2  # Retina fix

    # Start drag
    start = path[0]
    mouse_event(kCGEventLeftMouseDown, (scale(start.xc), scale(start.yc)))
    time.sleep(0.01)

    for tile in path[1:]:
        mouse_event(kCGEventLeftMouseDragged, (scale(tile.xc), scale(tile.yc)))
        time.sleep(0.02)
        # time.sleep(1)

    # End drag
    mouse_event(kCGEventLeftMouseUp, (scale(path[-1].xc), scale(path[-1].yc)))
    time.sleep(0.05)
