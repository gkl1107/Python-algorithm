

from numpy import linspace, pi, sin, cos
from pylab import plot, subplot, cm, imshow, xlabel, ylabel, \
    title, grid, axis, show, savefig, gcf, figure, close, tight_layout

from scipy.misc.pilutil import imread


x = linspace(0, 2*pi, 101)

s = sin(x)

c = cos(x)

img = imread('dc_metro.JPG', flatten = True)   # flatten creates a 2-D array from a JPEG

close('all')

# start by create a 2-by-2 plot grid and plot the 1st one
subplot(2, 2, 1)
plot(x, s, 'b-', x, c, 'r*')
axis('tight')

# move on to the 2nd plot
subplot(2, 2, 2)
plot(x, s)
grid()
xlabel('this is x')
ylabel('this is s')
title(' x vs s')
axis('tight')

# move on the 3rd plot

subplot(2,2,3)
imshow(img, extent=[-10, 10, -10, 10], cmap = cm.winter)

tight_layout()

show()

savefig(my_plot.png)
