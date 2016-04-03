# ENGR-120-Tracker
Uses the Optitrack system to track the Engineering 120 robots around the track

How to use
==========
1. Launch the Optitrack system normally and enable VRPN broadcasting
    -Name the rigid body as robot
2. Source devel/setup.bash
3. roslaunch optitrack.Launch
    -This will launch the VRPN module and the logger
4. run the run_to_file.py program for each run through the track.
    -This will generate a CSV upon SIGINT in the directory structures
    -The tree is composed of branches based on month and then dates
    -Files will be saved in the format run_"Name"_"Hour":"Minute":"Second".csv
