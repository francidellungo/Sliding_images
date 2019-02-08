""" import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pylab
from matplotlib.backend_bases import NavigationToolbar2



 def press(event, i):
    if event.key == right_button:
        i = i+1
    elif event.key == left_button:
        i = i-1

#fig = plt.figure()

toolbar_elements = fig.canvas.toolbar.children()
left_button = toolbar_elements[6]
right_button = toolbar_elements[8] 

pylab.ion()

img1 = pylab.imread('nike.png')
img2 = pylab.imread('pepsi2.png')
img3 = pylab.imread('img_000101.png')
img4 = pylab.imread('Marlboro.png')
img5 = pylab.imread('pepsi.png')
img6 = pylab.imread('sport.png')
img7 = pylab.imread('starbucks.png')

images = list()
images.append(img1)
images.append(img2)
images.append(img3)
images.append(img4)
images.append(img5)
images.append(img6)
images.append(img7) 

for img in images:
    pylab.imshow(img)
    pylab.show()
    pylab.waitforbuttonpress()"""




import numpy as np
#import matplotlib.pyplot as plt
import pylab

# define your x and y arrays to be plotted
#t = np.linspace(start=0, stop=2*np.pi, num=100)
#y1 = np.cos(t)
#y2 = np.sin(t)
#y3 = np.tan(t)
#plots = [(t,y1), (t,y2), (t,y3)]

img1 = pylab.imread('nike.png')
img2 = pylab.imread('pepsi2.png')
img3 = pylab.imread('img_000101.png')
img4 = pylab.imread('Marlboro.png')
img5 = pylab.imread('pepsi.png')
img6 = pylab.imread('sport.png')
img7 = pylab.imread('starbucks.png')

images = list()
images.append(img1)
images.append(img2)
images.append(img3)
images.append(img4)
images.append(img5)
images.append(img6)
images.append(img7)

#pylab.imshow(img1)
#pylab.show()
#pylab.draw()
# now the real code :) 
curr_pos = 0

def key_event(e):
    global curr_pos

    if e.key == "right":
        curr_pos = curr_pos + 1
    elif e.key == "left":
        curr_pos = curr_pos - 1
    else:
        return
    curr_pos = curr_pos % len(images)

    """ax.cla()
    ax.plot(plots[curr_pos][0], plots[curr_pos][1])
    fig.canvas.draw()"""

    pylab.cla()
    pylab.imshow(images[curr_pos])
    pylab.draw()


fig = pylab.figure()
#fig.axes('off')
#fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', key_event)
fig.show()
#ax = fig.add_subplot(111)
#ax.plot(t,y1)

pylab.show()