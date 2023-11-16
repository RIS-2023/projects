cmake_minimum_required(VERSION 2.8.3)
project(duckiebot_package)

find_package(catkin REQUIRED COMPONENTS
  rospy
  duckietown_msgs # Every duckietown packages should use this.
  cv_bridge
  tf
  std_msgs
)


catkin_package(
  CATKIN_DEPENDS
  message_runtime
  std_msgs
)

# add python scripts
catkin_install_python(PROGRAMS
  Duckiebot_script.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
