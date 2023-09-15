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
    pub2 = rospy.Publisher('button_go', Bool, queue_size=10)
    msg2 = Bool(data=True)
    pub2.publish(msg2)
    return render(request, 'wait.html')

def loading(request):
    return render(request, 'loading.html')

def checking(request):
    return render(request, 'checking.html')

########### customer ###########
def main1(request):
    rospy.init_node('ros_web_interface', anonymous=True)

    pub = rospy.Publisher('button_open', Bool, queue_size=10)
    msg = Bool(data=True)
    pub.publish(msg)
    
    pub2 = rospy.Publisher('button_go', Bool, queue_size=10)
    msg2 = Bool(data=True)
    pub2.publish(msg2)
    return render(request,'main1.html')

@login_required(login_url='managment/login/')
def goods(request):
    return render(request, 'goods.html')
"""
def goods(request, customer_id): #views.py의 pk변수명과 urls.py의 변수명은 같아야 함
    customer = get_object_or_404(Customer, pk=customer_id) #모델과 pk를 customer_id라고 부를거야
    customer_form = LoginForm()
    return render(request,'goods.html', {'customer' : customer}) #값을 보낼거임
"""
rospy.init_node('ros_web_interface', anonymous=True)
def complete(request):
    rospy.init_node('ros_web_interface', anonymous=True)

    pub = rospy.Publisher('button_open', Bool, queue_size=10)
    msg = Bool(data=True)
    pub.publish(msg)
    return render(request, 'complete.html')

rospy.init_node('ros_web_interface', anonymous=True)
def end(request):
    pub = rospy.Publisher('button_open', Bool, queue_size=10)
    msg = Bool(data=True)
    pub.publish(msg)
    return render(request, 'end.html')