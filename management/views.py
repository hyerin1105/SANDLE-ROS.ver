import rospy
import os
import subprocess
from std_msgs.msg import Bool, String
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

rospy.init_node('ros_web_interface', anonymous=True)
# 회원가입
def signup(request):
    pub4 = rospy.Publisher('microphone', Bool, queue_size=10)
    msg4 = Bool(data=True)
    pub4.publish(msg4)

    pub5 = rospy.Publisher('destination', String, queue_size=10)
    msg5 = String() #std::
    pub5.publish(msg5)
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        pub = rospy.Publisher('open_door', Bool, queue_size=10)
        msg = Bool(data=True)
        pub.publish(msg)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        confirm = request.POST.get('confirm', None)

        err_data = {}
        if not (username and password and confirm):
            err_data['error'] = 'every'

        elif password != confirm:
            err_data['error'] = 'different'
        
        else:
            customer = User(
                username=username,
                password=make_password(password),
            )
            customer.save()
            return redirect('checking')
    return render(request, 'signup.html', err_data)

# 로그인
#rospy.init_node('ros_web_interface', anonymous=True)
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        err_data = {}
        if not (username and password):
            err_data['error'] = '모든 값을 입력해 주세요.'
        else:
            customer = User.objects.get(username=username)
            if check_password(password, customer.password):
                request.session['user'] = customer.id
                return redirect('goods')
            else:
                err_data['error'] = '비밀번호가 일치하지 않습니다.'
        return render(request, 'signup.html', err_data)

# 로그아웃
#@login_required 로그인 인증되어있을 때만 실행됨
def logout(request):
    auth.logout(request)
    return redirect('wait')