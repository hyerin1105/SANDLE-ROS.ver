import rospy
import os
import subprocess
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from std_msgs.msg import Bool

# Create your views here.
def main(request):
    return render(request, 'main.html')
    
rospy.init_node('ros_web_interface', anonymous=True)
def goods(request):
    pub = rospy.Publisher('button_press', Bool, queue_size=10)
    msg = Bool(data=True)
    pub.publish(msg)
    return render(request, 'goods.html')
    #msg = Bool(data="Button Pressed")
    #pub.publish(msg)
    #response_data = {'message': 'ROS message sent successfully'}
    #return JsonResponse(response_data)

def complete(request):
    return render(request, 'complete.html')

rospy.init_node('ros_web_interface', anonymous=True)
def end(request):
    pub2 = rospy.Publisher('button_press2', Bool, queue_size=10)
    msg2 = Bool(data=True)
    pub2.publish(msg2)
    return render(request, 'end.html')