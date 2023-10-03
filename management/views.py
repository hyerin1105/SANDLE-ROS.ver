import rospy
import os
import subprocess
from std_msgs.msg import Bool, String
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

rospy.init_node('ros_web_interface', anonymous=True)

# Initialize the destination publisher and val variable
pub5 = rospy.Publisher('destination', String, queue_size=10)
val = String()

def func(destination_value):
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

# 회원가입
def signup(request):    
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        pub = rospy.Publisher('open_door', Bool, queue_size=10)
        msg = Bool(data=False)
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
            
            func(username)
            pub5.publish(val)
            return redirect('checking')
    return render(request, 'signup.html', err_data)

# 로그인
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
def logout(request):
    auth.logout(request)
    return redirect('wait')
