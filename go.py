import rospy
from std_msgs.msg import Bool

rospy.init_node('henes_go_publisher', anonymous=True)
pub = rospy.Publisher('/start_command', Bool, queue_size=10)
rate = rospy.Rate(1)
val = Bool()

def publish_receive_product(): # diff
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