#!/usr/bin/env python
#import rospy
from geometry_msgs.msg import Pose
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#globals for use in callback
locx = np.array([0]) #list of x positions
locy = np.array([0]) #list of y positions
locz = np.array([0]) #list of z positions

#setup the plotting
plt.ion()
fig = plt.figure()

def add_to_path(data):
    locs.append([data.position.x, data.position.y, data.position.z])
    locx = np.append(locx, np.array([data.position.x]))
    locy = np.append(locy, np.array([data.position.y]))
    locz = np.append(locz, np.array([data.position.z]))


#loc_sub = rospy.Subscriber('/robot/location', Pose)

#Plotting of the data
for i in range(0,10):
    fig.add_subplot(111, projection='3d').plot(locx, locy, locz, marker='x')
    plt.draw()
    locx = np.append(locx, np.array([np.random.rand(1)]))
    locy = np.append(locy, np.array([np.random.rand(1)]))
    locz = np.append(locz, np.array([np.random.rand(1)]))
    plt.show()


#rospy.spin()

#Save the data on exit
dat = np.asarray([locx, locy, locz])
np.savetxt("/home/bkallaher/runs/run.csv", dat, delimiter=",")
