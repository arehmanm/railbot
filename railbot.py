import pyxhook
import calc
import snapshot
import numpy
import mouse
from datetime import datetime
import operator
#change this to your log file's path

screen = [1600, 900]
window = [640, 480]
imp = [400, 300]
diff = [(p-q)/2 for (p,q) in zip(window, imp)]

def algo1():
    time1 = datetime.now()
    img = snapshot.snapshot(screen, window, imp)
    print "snapshot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    center = calc.getCenter(numpy.array(img))
    if center:
        center = map(operator.add, center, diff)
    print "getCenter: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    #print center
    if center:
        mouse.shoot(center, screen, window)
    time2 = datetime.now()
    print "shoot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"

def algo2():
    global multiplier
    time1 = datetime.now()
    img1 = snapshot.snapshot(screen, window, imp)
    print "snapshot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    center1 = calc.getCenter(numpy.array(img1))
    print "getCenter: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    if center1:
        center1 = map(operator.add, center1, diff)
    img2 = snapshot.snapshot(screen, window, imp)
    print "snapshot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    center2 = calc.getCenter(numpy.array(img2))
    print "getCenter: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()
    if center2:
        center2 = map(operator.add, center2, diff)
    #print center
    if center1 and center2:
        offset = [q-p for (p, q) in zip(center1, center2)]
        new_center = [multiplier*p+q for (p, q) in zip(offset, center2)]
        mouse.shoot(new_center, screen, window)
    print "shoot: " + str((datetime.now() - time1).microseconds / 1000) + " ms"
    time1 = datetime.now()

multiplier = 4
algo = algo1

#this function is called everytime a key is pressed.
def OnKeyPress(event):
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
    elif event.Key == "P_Add":
        multiplier += 1
        print "\nmutiplier: " + str(multiplier)
    elif event.Key == "P_Subtract":
        multiplier -= 1
        print "\nmutiplier: " + str(multiplier)
    elif event.Key == "P_End":
        algo = algo1
        print "\n**** Setting algo1 ****"
    elif event.Key == "P_Down":
        algo = algo2
        print "\n**** Setting algo2 ****"

    
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
