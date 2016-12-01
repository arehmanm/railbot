import pyxhook
import calc
import snapshot
import numpy
import mouse
from datetime import datetime
import operator
import constants
import time
#change this to your log file's path

low = constants.low_blue
high = constants.high_blue

def algo1():
    time1 = datetime.now()
    img = snapshot.snapshot(constants.screen, constants.window, constants.imp)
    print "snapshot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    center = calc.getCenter(numpy.array(img), low, high)
    if center:
        center = map(operator.add, center, constants.diff)
    print "getCenter: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    #print center
    if center:
        mouse.shoot(center, constants.screen, constants.window)
    time2 = datetime.now()
    print "shoot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"

def algo2():
    global multiplier
    time1 = datetime.now()
    img1 = snapshot.snapshot(constants.screen, constants.window, constants.imp)
    print "snapshot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    center1 = calc.getCenter(numpy.array(img1), low, high)
    print "getCenter: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    if center1:
        center1 = map(operator.add, center1, constants.diff)
    img2 = snapshot.snapshot(constants.screen, constants.window, constants.imp)
    print "snapshot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    center2 = calc.getCenter(numpy.array(img2), low, high)
    print "getCenter: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    if center2:
        center2 = map(operator.add, center2, constants.diff)
    #print center
    if center1 and center2:
        offset = [q-p for (p, q) in zip(center1, center2)]
        new_center = (multiplier*offset[0]+center2[0], offset[1]+center2[1])
        mouse.shoot(new_center, constants.screen, constants.window)
    print "shoot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()

multiplier = 4
algo = algo1

#this function is called everytime a key is pressed.
def OnKeyPress(event):
    global low, high
    global multiplier
    global algo
    if event.Key == "Shift_L":
        print ""
        time1 = datetime.now()
        #algo1()
        algo()
        #mouse.click()
        time2 = datetime.now()
        time3 = time2 - time1
        print "total: " + str(time3.microseconds / 1000) + " ms"
        time.sleep(0.1)
        img = snapshot.snapshot(constants.screen, constants.window, constants.imp)
        center = calc.getCenter(numpy.array(img), low, high)
    elif event.Key == "apostrophe":
        multiplier += 1
        print "\nmutiplier: " + str(multiplier)
    elif event.Key == "semicolon":
        multiplier -= 1
        print "\nmutiplier: " + str(multiplier)
    elif event.Key == "bracketleft":
        algo = algo1
        print "\n**** Setting algo1 ****"
    elif event.Key == "bracketright":
        algo = algo2
        print "\n**** Setting algo2 ****"
    elif event.Key == "minus":
        print "\n**** Now targetting BLUE team ****"
        low = constants.low_blue
        high = constants.high_blue
    elif event.Key == "equal":
        print "\n**** Now targetting RED team ****"
        low = constants.low_red
        high = constants.high_red
    
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
