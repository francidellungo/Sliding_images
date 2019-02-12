from PIL import Image

def get_width_pixels(filepath):
    width, height = Image.open(filepath).size
    return width

def get_height_pixels(filepath):
    w, height = Image.open(filepath).size
    return height

import matplotlib.pyplot as plt
xs = [1,2,3,4]
ys = [1,4,9,16]
#plt.plot(xs, ys, 'ro')
s = [30, 50, 80, 100]

plt.plot(xs,ys, linewidth=2)
plt.scatter(xs, ys, s=s)
xy = []
for i in range(len(xs)):
    xy.append((xs[i], ys[i]))
#plt.annotate('2', xy= xy)
plt.show()
