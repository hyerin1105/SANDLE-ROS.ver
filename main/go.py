#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

def publish_receive_product():
    rospy.init_node('receive_product_publisher', anonymous=True)
    pub = rospy.Publisher('receive_product', Bool, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz (1 message per second)

    try:
        while not rospy.is_shutdown():
            msg = Bool()
            msg.data = True  # Change this value as needed
            pub.publish(msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        msg = Bool()
        msg.data = False
        pub.publish(msg)

if __name__ == '__main__':
    publish_receive_product()