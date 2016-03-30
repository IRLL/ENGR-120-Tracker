#!/usr/bin/env python

"""
Author: Brandon Kallaher (brandon.kallaher@wsu.edu)
Description:
    Reads a csv compares it to a baseline and generates an image for processing
    It then loads the image and determines number of blue pixels in the image
"""

import numpy as np # for matrix operations and data structures
import matplotlib.pyplot as plt #For plotting of runs
import math #Fos cos and sin
import tf.transformations as transform #For quaternion to euler transform
import cv2 #For image processing
import os #used for environ and mkdir
from shutil import rmtree as rmdir #Need this function in order to delete tmp dir without deleting tmp files

#Define the path to load the run file and base
dirbase=os.environ['HOME'] + "/runs/"
fname = "run.csv"
baseline_file = "base.csv"

def rotate(x, y, z, theta):
    #Do X Rotation
    x_rot = np.dot([[1,0,0],
                    [0, math.cos(theta[0]), -math.sin(theta[0])],
                    [0, math.sin(theta[0]), math.cos(theta[0])]], [x,y,z])

    #Do Y Rotation
    y_rot = np.dot([[math.cos(theta[1]), 0, math.sin(theta[1])],
                    [0,1,0],
                    [-math.sin(theta[1]), 0, math.cos(theta[1])]], x_rot)

    #Do Z Rotation
    z_rot = np.dot([[math.cos(theta[2]), -math.sin(theta[2]), 0],
                    [math.sin(theta[2]), math.cos(theta[2]), 0],
                    [0, 0, 1]], y_rot)
    return z_rot

def parse_run(basedir, fname, baseline):

    #load from the file
    tmp = np.genfromtxt(basedir + fname, skip_footer=4, delimiter=",")
    #[x,y,z] = np.split(tmp, 4, axis=0)
    x = tmp[0,:]
    y = tmp[1,:]
    z = tmp[2,:]
    tmp = np.genfromtxt(basedir + fname, skip_header=3, delimiter=",", usecols=(0))
    quat = np.transpose(tmp)
    theta0 = transform.euler_from_quaternion(quat)
    print "theta0", theta0

    tmp = np.loadtxt(baseline, delimiter=",")
    bx = tmp[0,:]
    by = tmp[1,:]
    bz = tmp[2,:]
    tmp = np.genfromtxt(baseline, skip_header=3, delimiter=",", usecols=(0))
    quat = np.transpose(tmp)
    theta1 = transform.euler_from_quaternion(quat)
    print "theta1", theta1
    print "theta:", np.subtract(theta0, theta1)

    [xr, yr, zr] = rotate(x,y,z,np.subtract(theta0, theta1))

    #plot the data
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(x, y, color='b', linewidth=5)
    ax.plot(bx, by, linewidth=5, color='r')
    #ax.plot(xr, yr, color='g')
    #ax.set_xlabel('x')
    #ax.set_ylabel('y')
    plt.margins(0.05, 0.1)
    plt.draw()
    #plt.show(block=False)
    if not os.path.exists(basedir + "tmp"):
        os.mkdir(basedir + "tmp")

    fig.savefig(basedir + "tmp/out.png", transparent=True, bbox_inches='tight')

    #Load the new image for image processing
    img = cv2.imread(basedir + "tmp/out.png")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_b = np.array([110,50,50])
    high_b = np.array([130,255,255])

    mask = cv2.inRange(hsv, low_b, high_b)

    res = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow('image', img)
    # cv2.imshow('HSV', hsv)
    # cv2.imshow('mask', mask)
    # cv2.imshow('res', res)

    b,g,r = cv2.split(res)

    return cv2.countNonZero(b) # get count of all pixels with at least 1 blue value

    #cv2.destroyAllWindows()


if __name__ == '__main__':
    print parse_run(dirbase, fname, dirbase + baseline_file)

    rmdir(dirbase + "tmp", ignore_errors=True)
