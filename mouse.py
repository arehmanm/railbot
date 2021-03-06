from evdev import UInput, ecodes as e
from datetime import datetime
import autopy
from Xlib import X, display
import uinput
import time
import math

device = uinput.Device([
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        uinput.REL_X,
        uinput.REL_Y,
        ])

def click():
    capabilities = {
        e.EV_REL : (e.REL_X, e.REL_Y), 
        e.EV_KEY : (e.BTN_LEFT, e.BTN_RIGHT),
    }
    
    with UInput(capabilities) as ui:
        ui.write(e.EV_KEY, e.BTN_LEFT, 1)
        ui.syn()

def click2():
    device = uinput.Device([
            uinput.BTN_LEFT,
            uinput.BTN_RIGHT,
            uinput.REL_X,
            uinput.REL_Y,
            ])
    time.sleep(0.01)
    device.emit(uinput.BTN_LEFT, 1)

def shoot1(coords, screen, window, sens=1.0):
    time1 = datetime.now()
    center = [p/2 for p in window]
    print window
    offset = [p-q for p, q in zip(coords, center)]
    #print "offset: " + str(offset)
    offset =  [int(p) for p in offset]
    #print "offset: " + str(offset)
    
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

def shoot2(coords, screen, window, sens=1.0):
    global device
    center = [p/2 for p in window]
    offset = [p-q for p, q in zip(coords, center)]
    offset =  [int(p*sens) for p in offset]
    #print "offset: " + str(offset)
    
    device.emit(uinput.REL_X, offset[0])
    device.emit(uinput.REL_Y, offset[1])
    device.emit_click(uinput.BTN_LEFT, 0)
    device.emit_click(uinput.BTN_LEFT, 1)

def shoot(coords, screen, window, sens=1.0):
    shoot2(coords, screen, window, sens)

def move2(coords, screen, window, sens=1.0):
    print "moving to " + str(coords)
    global device
    center = [q - p/2 for (q, p) in zip(screen, window)]
    offset = [p-q for p, q in zip(coords, center)]
    dist = math.sqrt(offset[0]*offset[0] + offset[1]*offset[1])
    print dist
    sens = 1.0 - sens*dist / 250.0
    print sens
    offset =  [int(p*sens) for p in offset]
    #print "offset: " + str(offset)

    device.emit(uinput.REL_X, offset[0])
    device.emit(uinput.REL_Y, offset[1])

def move(coords, screen, window, imp, sens=1.0):
    print "moving to " + str(coords)
    global device
    center = [p/2 for p in imp]
    offset = [p-q for p, q in zip(coords, center)]
    offset =  [int(p) for p in offset]
    #print "offset: " + str(offset)

    device.emit(uinput.REL_X, offset[0])
    device.emit(uinput.REL_Y, offset[1])

