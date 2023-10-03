import rospy
import os
import subprocess
from .forms import LoginForm
from .models import Customer
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from std_msgs.msg import Bool, String
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


########### ceo ###########
def wait(request):
    pub3 = rospy.Publisher('receive_product', Bool, queue_size=10)
    msg3 = Bool(data=True)
    pub3.publish(msg3)
    return render(request, 'wait.html')

def loading(request):
    return render(request, 'loading.html')

def map(request):
    rospy.init_node('ros_web_interface', anonymous=True)
    pub2 = rospy.Publisher('open_door', Bool, queue_size=10)
    msg2 = Bool(data=True)
    pub2.publish(msg2)
    return render(request, 'map.html')

def checking(request):
    pub4 = rospy.Publisher('microphone', Bool, queue_size=10)
    msg4 = Bool(data=True)
    pub4.publish(msg4)
    
    pub5 = rospy.Publisher('destination', String, queue_size=10)
    msg5 = String() #std::
    pub5.publish(msg5)
    return render(request, 'checking.html')

########### customer ###########
def main1(request):
    rospy.init_node('ros_web_interface', anonymous=True)
    pub2 = rospy.Publisher('start_command', Bool, queue_size=10)
    msg2 = Bool(data=True)
    pub2.publish(msg2)
    return render(request,'main1.html')

def goods(request):
    return render(request, 'goods.html')

def complete(request):
    rospy.init_node('ros_web_interface', anonymous=True)
    pub2 = rospy.Publisher('open_door', Bool, queue_size=10)
    msg2 = Bool(data=True)
    pub2.publish(msg2)
    return render(request, 'complete.html')

rospy.init_node('ros_web_interface', anonymous=True)
def end(request):
    pub2 = rospy.Publisher('open_door', Bool, queue_size=10)
    msg2 = Bool(data=False)
    pub2.publish(msg2)
    return render(request, 'end.html')
