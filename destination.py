import rospy
from std_msgs.msg import String

pub = rospy.Publisher('/destination', String, queue_size=10)
rospy.init_node('destination', anonymous=True)
rate = rospy.Rate(1)
val = String()

def func():
    destination_value = ""  # Initialize destination_value
    if (destination_value == "0"):
        val.data = "Main_University"  # Set the data attribute of val
    elif (destination_value == "1"):
        val.data = "Medical_Sciences_Gwans"
    elif (destination_value == "2"):
        val.data = "International_Center"
    elif (destination_value == "3"):
        val.data = "Naturel_Science_Gwan"
    elif (destination_value == "5"):
        val.data = "Idesign"
    elif (destination_value == "6"):
        val.data = "Humanities_Social_Science_Gwan"
    elif (destination_value == "7"):
        val.data = "Educational_Sciences_Gwan"
    elif (destination_value == "9"):
        val.data = "Gong_Hak_Gwan"
    elif (destination_value == "A"):
        val.data = "Antire_preneur_Gwan"
    elif (destination_value == "B"):
        val.data = "San_Hak_Hyeop_Ryeok_Gwan"
    elif (destination_value == "BI"):
        val.data = "BRIX_Gwan"
    elif (destination_value == "C"):
        val.data = "Regional_Innovation_Gwan"
    elif (destination_value == "GV"):
        val.data = "Global_Village"
    elif (destination_value == "H"):
        val.data = "Hak_Ye_Gwans"
    elif (destination_value == "L"):
        val.data = "Library"
    elif (destination_value == "M"):
        val.data = "Multi_Media_Gwans"
    elif (destination_value == "ML"):
        val.data = "Media_Laps"
    elif (destination_value == "RC"):
        val.data = "Hyang_111"
    elif (destination_value == "RC2"):
        val.data = "Hyang_222"
    elif (destination_value == "RC3"):
        val.data = "Hyang_333"
    elif (destination_value == "T"):
        val.data = "Han_maru"
    elif (destination_value == "U"):
        val.data = "Unitophia_Gwan"
    else:
        val.data = "I don't know what you're talking about"

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            func()
            rospy.loginfo(val)
            pub.publish(val)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
