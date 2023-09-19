import rospy
from std_msgs.msg import String

rospy.init_node('destination_node', anonymous=True)
pub = rospy.Publisher('/destination', String, queue_size=10)
rate = rospy.Rate(1)
val = String()

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