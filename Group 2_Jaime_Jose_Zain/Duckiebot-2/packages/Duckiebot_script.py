import rospy
from std_msgs.msg import Float32
from duckietown_msgs.msg import Twist2DStamped
from sensor_msgs.msg import Range

# Constants
MIN_SAFE_DISTANCE = 0.10  #  10 cm
SAFE_DISTANCE = 0.20  # 20 cm
BACKWARD_SPEED = -0.5  # Adjust the backward speed as needed

class TOFController:
    def __init__(self):
        # Initialize ROS node
        rospy.init_node('tof_controller')

        # Subscribe to the TOF sensor topic
        rospy.Subscriber('thor/front_center_tof_driver_node/range', Range, self.tof_callback)

        # Create a publisher to control the Duckiebot's velocity
        self.velocity_pub = rospy.Publisher('thor/joy_mapper_node/car_cmd', Twist2DStamped, queue_size=1)

        # Initialize the flag to indicate if an obstacle is too close
        self.obstacle_detected = False

    def tof_callback(self, data):
        # Check if an obstacle is too close
        if data.range < SAFE_DISTANCE:
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def run(self):
        # Run the controller loop
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            rospy.loginfo(self.obstacle_detected)
            if self.obstacle_detected:
                # Move backwards until the safe distance is achieved
                self.move_backwards()
            else:
                # Stop the backward movement
                self.stop_movement()

            rate.sleep()

    def move_backwards(self):
        # Create a Twist message with backward speed
        velocity_msg = Twist2DStamped()
        velocity_msg.v = BACKWARD_SPEED
        velocity_msg.omega = 0
        velocity_msg.header.stamp = rospy.Time.now()

        # Publish the message to move the Duckiebot
        self.velocity_pub.publish(velocity_msg)

    def stop_movement(self):
        # Create a Twist message with zero speed to stop the Duckiebot
        velocity_msg = Twist2DStamped()
        velocity_msg.v = 0
        velocity_msg.omega = 0
        velocity_msg.header.stamp = rospy.Time.now()

        # Publish the message to stop the movement
        self.velocity_pub.publish(velocity_msg)


if __name__ == '__main__':
    try:
        # Create a TOFController object and run it
        tof_controller = TOFController()
        tof_controller.run()
    except rospy.ROSInterruptException:
        pass
