#!/usr/bin/env python

"""
Author: Brandon Kallaher (brandon.kallaher@wsu.edu)
Description:
    Subscribes to /robot/location and saves the data to a csv file
"""

import rospy
from geometry_msgs.msg import Pose
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import time

name = raw_input("Enter a name for the run: ")
print name
t = time.localtime()

#Define the path to save the run files
dirbase=os.environ['HOME'] + "/runs/{0}/{1}/".format(t.tm_mon, t.tm_mday)
fname = "run_{0}_{1}:{2}.csv".format(name, t.tm_hour, t.tm_min)

#globals for use in callback
locx = np.array([0, 1, 2, 3, 4]) #list of x positions
locy = np.array([0, 2, 3, 4, 5]) #list of y positions
locz = np.array([0, 3, 4, 5, 6]) #list of z positions
quat = np.array([5, 3, 9 ,2])

#setup the plotting
# plt.ion()
# fig = plt.figure()

def shutdown_callback():
    #Save the data on exit
    qx = np.pad([quat[0],0], (0,locx.size-2), mode='constant', constant_values=0)
    qy = np.pad([quat[1],0], (0,locx.size-2), mode='constant', constant_values=0)
    qz = np.pad([quat[2],0], (0,locx.size-2), mode='constant', constant_values=0)
    qw = np.pad([quat[3],0], (0,locx.size-2), mode='constant', constant_values=0)

    dat = np.vstack([locx, locy, locz, qx, qy, qz, qw])
    if not os.path.exists(dirbase):
        os.makedirs(dirbase)
    np.savetxt(dirbase + fname, dat, delimiter=",")

def add_to_path(data):
    locs.append([data.position.x, data.position.y, data.position.z])
    locx = np.append(locx, np.array([data.position.x]))
    locy = np.append(locy, np.array([data.position.y]))
    locz = np.append(locz, np.array([data.position.z]))

    if quat.size:
        quat[0] = data.orientation.x
        quat[1] = data.orientation.y
        quat[2] = data.orientation.z
        quat[3] = data.orientation.w


#init node and subscriber
rospy.init_node('dataSaver')
loc_sub = rospy.Subscriber('/robot/location', Pose)

rospy.on_shutdown(shutdown_callback)

#Plotting of the data
'''for i in range(0,10):
    fig.add_subplot(111, projection='3d').plot(locx, locy, locz, marker='x')
    plt.draw()
    locx = np.append(locx, np.array([np.random.rand(1)]))
    locy = np.append(locy, np.array([np.random.rand(1)]))
    locz = np.append(locz, np.array([np.random.rand(1)]))
    plt.show()
'''

rospy.spin()
