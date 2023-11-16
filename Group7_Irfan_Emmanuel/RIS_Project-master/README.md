## RIS_Project
This repository is created for lane and object detection functionality of a Duckiebot called robotLA. robotLA reads the camera view of a duckiebot and detects the lines as well as obstacles (ducks) in front of it.


# About the Project

#### Module Name: S23_CO-548-A_RIS Project
#### Instructor: Prof. Amr Alanwar Abdelhafez
#### Contributors: Emmanuel Muuo Mutuku & Irfan Karmali

# I. Introduction to ROS

### A. Installation of ROS Noetic
1.Take a look at the ROS Wiki page to follow <a href="http://wiki.ros.org/noetic/Installation/Ubuntu">instructions to ROS Noetic installation</a>.

### B. Creation of ROS Workspace and Package
1. Create a ROS workspace

       $ mkdir -p ~/catkin_ws/src
       $ cd ~/catkin_ws/
       $ catkin_make
       $ source devel/setup.bash

2. Get into your ROS workspace

       $ cd ~/catkin_ws/src
       
3. Copy a ROS Package

       $ git clone https://github.com/ldw200012/duckietown_yolov5.git

4. Run below commands to configure your ROS Package

       $ cd ~/catkin_ws
       $ catkin_make
       $ source devel/setup.bash (This command must be run on every shell you are using for ROS from now on)
       
# II. DATASET CREATION 

### A. Custom the program 

1. Prepare a dataset 

      i. Data preparation from duckiebot camera (You can skip this step if you already have your own images).
       
       $ rosrun image_transport republish compressed in:=/[duckiebot_name]/camera_node/image raw out:=/[duckiebot_name]/camera_node/image/raw
       $ cd [folder_directory_to_save_images]
       $ rosrun image_view image_saver image:=/[duckiebot_name]/camera_node/image/raw _save_all_image:=false _filename_format:=foo.jpg __name:=image_saver
       
      Now you can save image to the directory whenever you call the below command
       
       $ rosservice call /image_saver/save      
     
      ii. Data Annotation

      - Follow the instructions in Roboflow https://blog.roboflow.com/vott/
      
      iii. Dataset Creation
       
      - Follow the instructions in Roboflow https://www.youtube.com/watch?v=MdF6x6ZmLAY until 15:40.
      
        From now on, you need to remember the "<b>link</b>" provided by Roboflow. (Choose 'Terminal' among 'Jupyter/Terminal/Raw URL')
        <br>
        <br>

### B. How to run the program
1. Lane and Object Detection
        
      - In shell 1:
     
       $ rosrun image_transport republish compressed in:=/[duckiebot_name]/camera_node/image raw out:=/[duckiebot_name]/camera_node/image/raw
       
      - In shell 2:
     
       $ cd ./onject_detection/script/
       $ python3 lane_object_detection.py
       
      - In shell 3:
       
       $ dts start_gui_tools [duckiebotname]
       # rqt_image_view
       

