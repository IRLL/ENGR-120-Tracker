import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#load from the file
tmp = np.loadtxt("/home/bkallaher/runs/run.csv", delimiter=",")
[x,y,z] = np.split(tmp, 3, axis=0)
x = tmp[0,:]
y = tmp[1,:]
z = tmp[2,:]

tmp = np.loadtxt("/home/bkallaher/runs/base.csv", delimiter=",")
bx = tmp[0,:] + 0.05
by = tmp[1,:] + 0.1
bz = tmp[2,:] + 0.2

#plot the data
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, zs=z, color='b', marker='x', linewidth=5)
ax.plot(bx, by, zs=bz, marker='o', linewidth=5, color='r')
plt.draw()
plt.show(block=True)
