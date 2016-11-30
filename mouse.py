from evdev import UInput, ecodes as e
from datetime import datetime
import autopy
from Xlib import X, display
import pyautogui

def click():
    capabilities = {
        e.EV_REL : (e.REL_X, e.REL_Y), 
        e.EV_KEY : (e.BTN_LEFT, e.BTN_RIGHT),
    }
    
    with UInput(capabilities) as ui:
        ui.write(e.EV_KEY, e.BTN_LEFT, 1)
        ui.syn()

def shoot3(coords, screen, window):
    time1 = datetime.now()
    center = [p/2 for p in window]
    offset = [p-q for p, q in zip(coords, center)]
    #print "offset: " + str(offset)
    offset =  [int(p) for p in offset]
    
    (x, y) = autopy.mouse.get_pos()
    print (x, y)
    print offset
    #autopy.mouse.smooth_move(x+offset[0], y+offset[1])
    pyautogui.moveRel(offset[0], offset[1])
    autopy.mouse.click()
    time2 = datetime.now()
    print "shoot: " + str((time2 - time1).microseconds / 1000) + " ms"
      
def shoot(coords, screen, window):
    time1 = datetime.now()
    center = [p/2 for p in window]
    offset = [p-q for p, q in zip(coords, center)]
    #print "offset: " + str(offset)
    offset =  [int(p) for p in offset]
    #print offset
    
    capabilities = {
        e.EV_REL : (e.REL_X, e.REL_Y), 
        e.EV_KEY : (e.BTN_LEFT, e.BTN_RIGHT),
    }
    
    with UInput(capabilities) as ui:
        ui.write(e.EV_REL, e.REL_X, offset[0])
        ui.write(e.EV_REL, e.REL_Y, offset[1])
        ui.write(e.EV_KEY, e.BTN_LEFT, 1)
        ui.syn()
    
    time2 = datetime.now()
    print "shoot: " + str((time2 - time1).microseconds / 1000) + " ms"
#shoot([10, 10], [1600, 900], [640, 480])


time1 = datetime.now()
d = display.Display()
d.warp_pointer(300,300)
d.sync()
time2 = datetime.now()
print "shoot: " + str((time2 - time1).microseconds / 1000) + " ms"
