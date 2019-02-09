import numpy as np
import pylab

# Get images and inizialize list images

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

#Start real code
curr_pos = 0
fig = pylab.figure()
ax = fig.add_subplot(111)
ax.axis('off')
pylab.imshow(images[0])

def key_event(e):
    global curr_pos

    #If right button pressed -> go to next image
    if e.key == "right":
        curr_pos = curr_pos + 1
    #If left button pressed -> go to previous image
    elif e.key == "left":
        curr_pos = curr_pos - 1
    else:
        return
    curr_pos = curr_pos % len(images)

    pylab.cla()
    pylab.axis('off')
    pylab.imshow(images[curr_pos])
    pylab.draw()



#fig.axes('off')
#fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', key_event)
fig.show()
#ax = fig.add_subplot(111)
#ax.plot(t,y1)

pylab.show()