"""
#Get data
file_object = open('fixationStream.txt', 'r')

# Create data
#x = np.random.randn(10000)
#y = np.random.randn(10000)
x = [1,2,3,4,5,6]
y = [1,2,3,4,5,7]
#trasparency = []
XY = (x,y)
# Create heatmap
heatmap, xedges, yedges = np.histogram2d(x, y, bins=(64,64))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
 
# Plot heatmap
plt.clf()
plt.title('Pythonspot.com heatmap example')
#plt.ylabel('y')
#plt.xlabel('x')

#for interpolation see: https://matplotlib.org/gallery/images_contours_and_fields/interpolation_methods.html
plt.imshow(XY)

plt.show()
"""

""" import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

uniform = np.random.randn(10,10)
print(uniform[0])
sb.heatmap(uniform, vmin=-1, vmax=1, center=0)
plt.show() """

import matplotlib.pyplot as plt
from matplotlib.path import Path
import csv
import math

verts = []
xFix_start = None
yFix_start = None

with open('fixStream.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[0] == 'FS':
            xFix_start = row[1]
            yFix_start = row[2]
        elif row[0] == 'FE' and xFix_start is not None: #Per terminare la fixation deve essere iniziata
            xFix_end = row[1]
            yFix_end = row[2]
            #TODO gestire caso FS o FE Nan,Nan,-
            #if not math.isnan(xFix_start)
            x = (float(xFix_start)+ float(xFix_end))/2
            y = (float(yFix_start)+ float(yFix_end))/2
            verts.append((x,y))

#print(verts)
               


"""    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')"""


""" verts = [
    (0.1, 0.),  # P0
    (0.2, 1.), # P1
    (1., 0.8), # P2
    (0.9, 0.1), # P3
    (0.7, 0.4), # P4
    ]
"""

codes = list()
for i in verts:
    codes.append(Path.MOVETO,)

"""codes = [
         Path.MOVETO,
         Path.MOVETO,
         Path.MOVETO,
         Path.MOVETO,
         ]
         """

path = Path(verts, codes)

fig = plt.figure()
ax = fig.add_subplot(111)
xs, ys = zip(*verts)

ax.plot(xs, ys, 'o-', lw=1, color='green', ms=20)


for i in range(0, len(verts)):
    ax.annotate(i, xy = verts[i], verticalalignment='center', horizontalalignment='center' )

#ax.annotate("33", xy=verts[0], ha="center")

ax.axis('off')
ax.set_aspect('equal')
ax.autoscale_view()

#ax.set_xlim(-0.1, 1.1)
#ax.set_ylim(-0.1, 1.1)
plt.show()
