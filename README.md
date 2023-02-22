# mic_pan
This package uses [ReSpeaker Mic Array v2.0](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/) and gets the direction of the voice and pans the robot head in that direction.

## Installation
### 1. ReSpeaker Mic Array v2.0 ros package installation
Install the package according to the instructions provideo on: https://index.ros.org/p/respeaker_ros/#melodic

### 2. mic_pan installtion
 To install this, you need to go into your workspace using\
```cd your_ws/src/```\
clone the repo\
```git clone https://github.com/UsamaArshad16/mic_pan.git```\
Build this package\
```cd ..```\
```catkin_make```\
```source devel/setup.bash```\
Note: keep the workspaces for both packages seperate. because fisrt package uses catkin_build and second package uses catkin_make.

## Run the demo
```roslaunch rehab_bringup rehab_bringup.launch```\
```rosrun rosserial_python serial_node.py tcp 11411```\
```rosrun mic_pan pan_in_person_direction.py```
