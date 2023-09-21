import rospy
import os
import subprocess
from .forms import LoginForm
from .models import Customer
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from std_msgs.msg import Bool
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


########### ceo ###########
def wait(request):
    pub3 = rospy.Publisher('henes_come', Bool, queue_size=10)
    msg3 = Bool(data=True)
    pub3.publish(msg3)
    return render(request, 'wait.html')

def loading(request):
    return render(request, 'loading.html')

def checking(request):
    rospy.init_node('ros_web_interface', anonymous=True)
    pub2 = rospy.Publisher('open_door', Bool, queue_size=10)
    msg2 = Bool(data=True)
    pub2.publish(msg2)
    return render(request, 'checking.html')

########### customer ###########
def main1(request):
    rospy.init_node('ros_web_interface', anonymous=True)
    pub2 = rospy.Publisher('henes_go', Bool, queue_size=10)
    msg2 = Bool(data=True)
    pub2.publish(msg2)
    return render(request,'main1.html')

#@login_required(login_url='managment/login/')
def goods(request):
    return render(request, 'goods.html')

def complete(request):
    rospy.init_node('ros_web_interface', anonymous=True)
    pub = rospy.Publisher('open_door', Bool, queue_size=10)
    msg = Bool(data=True)
    pub.publish(msg)
    return render(request, 'complete.html')

rospy.init_node('ros_web_interface', anonymous=True)
def end(request):
    pub = rospy.Publisher('open_door', Bool, queue_size=10)
    msg = Bool(data=True)
    pub.publish(msg)
    return render(request, 'end.html')