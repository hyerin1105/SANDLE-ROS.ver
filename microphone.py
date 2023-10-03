import rospy
from std_msgs.msg import Bool

def microphone_active_publisher():
    rospy.init_node('microphone_active_publisher', anonymous=True)
    pub_microphone = rospy.Publisher('/microphone', Bool, queue_size=10)
    pub_open_door = rospy.Publisher('/open_door', Bool, queue_size=10)
    rate = rospy.Rate(1)  # 1Hz로 publish할 예정

    microphone_active = True  # 초기 상태 (마이크로폰 비활성화)

    while not rospy.is_shutdown():
        # 여기에서 필요한 조건에 따라 microphone_active 변수를 업데이트
        # 예를 들어, 특정 조건을 만족하면 microphone_active = True로 설정
        # 여기에서 조건을 검사하고 open_door를 제어합니다.
        if not microphone_active:
            pub_open_door.publish(Bool(data=True))
        else:
            pub_open_door.publish(Bool(data=False))

        # microphone_active 값을 Bool 메시지로 publish
        pub_microphone.publish(microphone_active)

        rate.sleep()

if __name__ == '__main__':
    try:
        microphone_active_publisher()
    except rospy.ROSInterruptException:
        pass

	


"""
import rospy
from std_msgs.msg import Bool

def microphone_active_publisher():
    rospy.init_node('microphone_active_publisher', anonymous=True)
    pub = rospy.Publisher('/microphone', Bool, queue_size=10)
    rate = rospy.Rate(1)  # 1Hz로 publish할 예정

    microphone_active = True  # 초기 상태 (마이크로폰 비활성화)

    while not rospy.is_shutdown():
        # 여기에서 필요한 조건에 따라 microphone_active 변수를 업데이트
        # 예를 들어, 특정 조건을 만족하면 microphone_active = True로 설정

        # microphone_active 값을 Bool 메시지로 publish
        pub.publish(microphone_active)

        rate.sleep()

if __name__ == '__main__':
    try:
        microphone_active_publisher()
    except rospy.ROSInterruptException:
        pass
"""