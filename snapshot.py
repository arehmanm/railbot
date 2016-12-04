#-- include('examples/showgrabbox.py')--#
import pyscreenshot as ImageGrab
import operator
from datetime import datetime
import gtk.gdk

def screenshot(rectpos, rectsize):
    w = gtk.gdk.get_default_root_window()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, rectsize[0], rectsize[1])
    pb = pb.get_from_drawable(w, w.get_colormap(), rectpos[0], rectpos[1], 0, 0, rectsize[0], rectsize[1])
    return pb.get_pixels_array()

def snapshot(screen, window, imp):
    diff = [(p-q)/2 for (p,q) in zip(window, imp)]
    pos = map(operator.sub, screen, window)
    pos = map(operator.add, pos, diff)
    screen = map(operator.sub, screen, diff)
    pos.extend(screen)
    #print pos
    return screenshot((pos[0], pos[1]), (imp[0], imp[1]))
    
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
