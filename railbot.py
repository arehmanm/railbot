import pyxhook
import calc
import snapshot
import numpy
import mouse
from datetime import datetime
import operator
import constants
import time
import os
import sys
#change this to your log file's path

low = constants.low_blue
high = constants.high_blue

def algo1():
    time1 = datetime.now()
    img = snapshot.snapshot(constants.screen, constants.window, constants.imp)
    print "snapshot: " + str((datetime.now() - time1).microseconds / 1000.0) + " ms"
    time1 = datetime.now()
    retval = calc.getCenter(numpy.array(img), low, high)
    if retval:
        (center, rectpos, rectsize) = retval
        center = map(operator.add, center, constants.diff)
    else:
        return
    print "getCenter: " + str((datetime.now() - time1).microseconds / 1000.0) + " ms"
    time1 = datetime.now()
    #print center
    if center:
        mouse.shoot(center, constants.screen, constants.window)
    time2 = datetime.now()
    print "shoot: " + str((datetime.now() - time1).microseconds / 1000.0) + " ms"

def algo2():
    global sensitivity
    frame1 = 0
    frame2 = 0
    time1 = datetime.now()
    img1 = snapshot.snapshot(constants.screen, constants.window, constants.imp)
    diff = (datetime.now() - time1).microseconds
    frame1 = frame1 + diff/2.0
    print "snapshot: " + str(diff / 1000.0) + " ms"
    time1 = datetime.now()
    retval = calc.getCenter(numpy.array(img1), low, high)
    diff = (datetime.now() - time1).microseconds
    frame1 = frame1 + diff
    print "getCenter: " + str(diff / 1000.0) + " ms"
    time1 = datetime.now()
    if retval:
        (center1, rectpos, rectsize) = retval
        center1 = map(operator.add, center1, constants.diff)
        rectpos = map(operator.add, rectpos, constants.diff)
        rectpos = map(operator.sub, rectpos, constants.window)
        rectpos = map(operator.add, rectpos, constants.screen)
    else:
        return
    #img2 = snapshot.snapshot(constants.screen, constants.window, constants.imp)
    img2 = snapshot.screenshot(rectpos, rectsize)
    diff = (datetime.now() - time1).microseconds
    frame2 = frame2 + diff
    print "snapshot: " + str(diff / 1000.0) + " ms"
    time1 = datetime.now()
    retval = calc.getCenter(numpy.array(img2), low, high)
    if retval:
        (center2, rectpos2, rectsize2) = retval
    else:
        return
    diff = (datetime.now() - time1).microseconds
    frame2 = frame2 + diff
    print "getCenter: " + str(diff / 1000.0) + " ms"
    time1 = datetime.now()
    if center2:
        center2 = map(operator.add, center2, rectpos)
        center2 = map(operator.add, center2, constants.window)
        center2 = map(operator.sub, center2, constants.screen)
    #print center

    multiplier = (frame2 + 25000.0) / frame1
    print "Using multiplier: " + str(multiplier)
    if center1 and center2:
        offset = [q-p for (p, q) in zip(center1, center2)]
        new_center = (multiplier*offset[0]+center2[0], multiplier*offset[1]+center2[1])
        mouse.shoot(new_center, constants.screen, constants.window, sensitivity)
    print "shoot: " + str((datetime.now() - time1).microseconds / 1000.0) + " ms"

def get_diff(rectpos, rectsize, center1):
    frame = 0
    time1 = datetime.now()
    img2 = snapshot.screenshot(rectpos, rectsize)
    diff = (datetime.now() - time1).microseconds
    frame = frame + diff
    print "snapshot: " + str(diff / 1000.0) + " ms"
    time1 = datetime.now()
    retval = calc.getCenter(numpy.array(img2), low, high)
    if retval:
        (center2, rectpos2, rectsize2) = retval
    else:
        return

    diff = (datetime.now() - time1).microseconds
    frame = frame + diff
    print "getCenter: " + str(diff / 1000.0) + " ms"
    time1 = datetime.now()
    if center2:
        center2 = map(operator.add, center2, rectpos)
        center2 = map(operator.add, center2, constants.window)
        center2 = map(operator.sub, center2, constants.screen)
    #print center

    if center1 and center2:
        offset = [q-p for (p, q) in zip(center1, center2)]
        rectpos2 = [p+q for (p,q) in zip(rectpos, offset)]
        return (rectpos2, center2, frame)
    else:
        return (0, 0, 0)

def algo3():
    global sensitivity
    frame1 = 0
    frame2 = 0
    time1 = datetime.now()
    img1 = snapshot.snapshot(constants.screen, constants.window, constants.imp)
    diff = (datetime.now() - time1).microseconds
    frame1 = frame1 + diff/2.0
    print "snapshot: " + str(diff / 1000.0) + " ms"
    time1 = datetime.now()
    retval = calc.getCenter(numpy.array(img1), low, high)
    diff = (datetime.now() - time1).microseconds
    frame1 = frame1 + diff
    print "getCenter: " + str(diff / 1000.0) + " ms"
    time1 = datetime.now()
    if retval:
        (center1, rectpos, rectsize) = retval
        center1 = map(operator.add, center1, constants.diff)
        rectpos = map(operator.add, rectpos, constants.diff)
        rectpos = map(operator.sub, rectpos, constants.window)
        rectpos = map(operator.add, rectpos, constants.screen)
    else:
        return
    #img2 = snapshot.snapshot(constants.screen, constants.window, constants.imp)

    x = []
    y = []
    t = []
    totaltime = frame1
    for i in range(7):
        (rectpos, center2, time2) = get_diff(rectpos, rectsize, center1)
        totaltime = totaltime + time2
        x.append(center2[0])
        y.append(center2[1])
        t.append(totaltime)
        center1 = center2

    print x, y, t
    z = numpy.polyfit(t, x, 2)
    f = numpy.poly1d(z)
    v = numpy.polyfit(t, y, 2)
    g = numpy.poly1d(v)

    totaltime = totaltime+25000
    new_center = (int(f(totaltime)), int(g(totaltime)))
    print totaltime
    print new_center
    mouse.shoot(new_center, constants.screen, constants.window, sensitivity)
    #print "shoot: " + str((datetime.now() - time1).microseconds / 1000.0) + " ms"

sensitivity = 0.9
algo = algo1

#this function is called everytime a key is pressed.
def OnKeyPress(event):
    global low, high
    global sensitivity
    global algo
    if event.Key == "Shift_L":
        print ""
        time1 = datetime.now()
        os.system("xinput set-prop " + mouseid + " \"Device Enabled\" 0")
        print "disable mouse: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
        time1 = datetime.now()
        #algo1()
        algo()
        #mouse.click()
        time2 = datetime.now()
        time3 = time2 - time1
        print "total: " + str(time3.microseconds / 1000.0) + " ms"
        for i in range(4):
            time.sleep(0.025)
            img = snapshot.snapshot(constants.screen, constants.window, constants.imp)
            #calc.getCenter(numpy.array(img), low, high)
        #time.sleep(0.1)
        time1 = datetime.now()
        os.system("xinput set-prop " + mouseid + " \"Device Enabled\" 1")
        print "enable mouse: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    elif event.Key == "apostrophe":
        sensitivity += 0.05
        print "\nsensitivity: " + str(sensitivity)
    elif event.Key == "semicolon":
        sensitivity -= 0.05
        print "\nsensitivity: " + str(sensitivity)
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

mouseid = sys.argv[1]
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
