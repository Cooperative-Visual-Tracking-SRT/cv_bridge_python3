# cv_bridge python 3
This is a sample code of using python3 and cv_bridge in ROS. The node will publish the image from `cv2.VideoCaputre(0)` 
to topic. 

## Prerequisite
- ubuntu 18.04
- python 3.6 (include pip, opencv, numpy, yaml and so on)
- python 2.7 (include pip)
- ros-melodic-desktop-full

## Installation
Install some dependency library. 
```
sudo apt-get install python-catkin-tools python3-dev python3-catkin-pkg-modules ros-melodic-cv-bridge
python2 -m pip install catkin-tools
python3 -m pip install rospkg
```
Note: `catkin-tools` only supports `python 2.7`, and `rospkg` supports `python 3`. 
When you use `catkin-tools` in `python 3`, the python interpreter will automatically find the library in `python2`. This
may encounter some problems when you use IDE such as pycharm. But if you can import `rospy` in terminal, you have 
installed successfully. You can test in terminal by using the following commands:
```
$ python3
>> import rospy
>> import rospkg 
```

Create a catkin workspace.
```
mkdir catkin_ws
cd catkin_ws
mkdir src
catkin_make
```
Put this package into `src`.
```
cd src
git clone 
chmod +x cv_bridge_python3/scripts/publisher.py
```
Put `cv_bridge` source code into `src`.
```
git clone https://github.com/ros-perception/vision_opencv.git src/vision_opencv
cp -r src/vision_opencv .
rm -r src
``` 
Check the path of `python 3` executable file (default in `/usr/bin/python3`),
`python 3.6` include directory (default in `/usr/include/python3.6m`),
`python 3.6` library path (default in `/usr/lib/x86_64-linux-gnu/libpython3.6m.so` for `x86_64` or 
`/usr/lib/aarch64-linux-gnu/libpython3.6m.so` for `arm_64`)

Compile the project, Use `python 3` as `cmake` python interpreter. 
```
cd ..
catkin_make --cmake-args -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so
```

Now you can test the `publisher.py`. Open a terminal and input
```
roscore
```
Open another terminal and run the publisher node
```
cd catkin_ws
source devel/setup.bash
rosrun cv_bridge_python3 publisher.py
```
Open another terminal, use `rviz` to visualize the image.
