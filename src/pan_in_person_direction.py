#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32, Int32MultiArray

# Create a global variable for the pan message to be published
pan_msg = Int32MultiArray()
# Create a list to store the last two pan angles
pan_angles_array = [0,0]

# Define global variables for the current and final pan angle
pan_angle = 0

# Define the callback function for the sound direction subscriber
def sound_direction_callback(msg):
    # Get the sound direction value from the received message
    mic_angle = msg.data

    # If the sound direction value is positive, adjust it for the inverted coordinate system
    if msg.data > 0:
        mic_angle = (180-msg.data)*-1
        # Cap the adjusted value at -60 degrees
        if mic_angle < -60:
            mic_angle = -60

    # If the sound direction value is negative, adjust it for the inverted coordinate system
    elif msg.data < 0:
        mic_angle = 180+msg.data
        # Cap the adjusted value at 60 degrees
        if mic_angle > 60:
            mic_angle = 60

    # Add the adjusted value to the list of last two pan angles
    pan_angles_array.pop(0)
    pan_angles_array.append(mic_angle)

    # Calculate the current pan angle by adding the last two pan angles
    pan_angle = pan_angles_array[1]+ pan_angles_array[0]
    # Cap the current pan angle at 60 degrees or -60 degrees
    if pan_angle > 60:
        pan_angle = 60
    if pan_angle < -60:
        pan_angle = -60

    # Set the data for the pan message to be published to the current pan angle
    pan_msg.data = [pan_angle]
    # Publish the pan message to the '/pan_angles' topic
    pub.publish(pan_msg)

    #print(mic_angle, pan_angle, pan_angles_array )

if __name__ == '__main__':
    # Initialize the ROS node with the name 'sound_direction_pan'
    rospy.init_node('sound_direction_pan')

    # Create a subscriber for the '/sound_direction' topic, which publishes Int32 messages
    sub = rospy.Subscriber('/sound_direction', Int32, sound_direction_callback)

    # Create a publisher for the '/pan_angles' topic, which publishes Int32MultiArray messages
    pub = rospy.Publisher('/pan_angles', Int32MultiArray, queue_size=10)

    # Start the ROS node main loop
    rospy.spin()
