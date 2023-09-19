import rospy
from std_msgs.msg import Bool

rospy.init_node('mic_node', anonymous=True)
pub = rospy.Publisher('/mic', Bool, queue_size=10)
"""
rate = rospy.Rate(1)
val = Bool()
"""

def publish_button_press():
    while not rospy.is_shutdown():
        pub.publish(Bool(True))
        rospy.sleep(1.0)

if __name__ == '__main__':
    try:
        publish_button_press()
    except rospy.ROSInterruptException:
        pass


"""
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
"""