#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

rospy.init_node('open_door_node', anonymous=True)
pub = rospy.Publisher('/open_door', Bool, queue_size=10)
rate = rospy.Rate(1)
val = Bool()

def pulish_button_press():
    msg = "Button Pressed"
    rospy.loginfo(msg)
    pub.publish(msg)

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            pub.publish(val)
            rate.sleep()
    except rospy.ROSInitException:
        pass