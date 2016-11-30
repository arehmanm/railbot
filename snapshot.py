#-- include('examples/showgrabbox.py')--#
import pyscreenshot as ImageGrab
import operator
from datetime import datetime
import cv2
import numpy
import gtk.gdk

def snapshot(screen, window, imp):
    diff = [(p-q)/2 for (p,q) in zip(window, imp)]
    pos = map(operator.sub, screen, window)
    pos = map(operator.add, pos, diff)
    screen = map(operator.sub, screen, diff)
    pos.extend(screen)
    #print pos

    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, imp[0], imp[1])
    pb = pb.get_from_drawable(w, w.get_colormap(), pos[0], pos[1], 0, 0, imp[0], imp[1])
    return pb.get_pixels_array()
    
def snapshot2(screen, window):
    time1 = datetime.now()
    pos = map(operator.sub, screen, window)
    pos.extend(screen)
    # part of the screen
    img=ImageGrab.grab(bbox=pos) # X1,Y1,X2,Y2
    time2 = datetime.now()
    print "snapshot: " + str((time2 - time1).microseconds / 1000) + " ms"
    return img
#-#
'''
img = snapshot((1600, 900), (5, 5))
img = numpy.asarray(img)
print img
cv2.imshow("Image", img)
cv2.waitKey()
#'''
