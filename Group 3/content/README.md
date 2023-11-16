# <div align=center>duckietown_CD70</div>
#### <div align="center">" This repository is created for object recognition functionality of Duckiebot, </div>

***

### Create ROS Workspace and Package
- Create a ROS workspace

       $ mkdir -p ~/catkin_ws/src
       $ cd ~/catkin_ws/
       $ catkin_make
       $ source devel/setup.bash

- Run below commands to configure your ROS Package

       $ cd ~/catkin_ws
       $ catkin build
       $ source devel/setup.bash
       
        
### Train the dataset:
       $ git clone https://github.com/ultralytics/yolov5
       $ pip install -qr requirements.txt

       
      

     Train your own dataset using the following command.
     
       $ python train.py --img 416 --batch 16 --epochs 100 --data '<FILE>' --cfg ./models/new_yolov5s.yaml --weights '<WEIGHTS FILE>' --name yolov5s_results  --cache
    

### run the program
1. Object Detection
        
      - In shell 1:
     
       $ rosrun image_transport republish compressed in:=/[duckiebot_name]/camera_node/image raw out:=/[duckiebot_name]/camera_node/image/raw
       
      - In shell 2:
     
       $ roscd cd70/code/
       $ python publisher.py
       
      - In shell 3:
       
       $ dts start_gui_tools [duckiebotname]
       # rqt_image_view



***



