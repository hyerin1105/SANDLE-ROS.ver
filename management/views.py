import rospy
import os
import subprocess
from std_msgs.msg import Bool
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required  # 데코레이터 함수 생성

from django.contrib.auth.hashers import make_password, check_password


# 회원가입
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
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
        
"""
def signup(request):
    rospy.init_node('ros_web_interface', anonymous=True)
    pub = rospy.Publisher('button_open', Bool, queue_size=10)
    msg = Bool(data=True)
    pub.publish(msg)
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')
"""

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

    """
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        customer = auth.authenticate(request, password=password)
        
        # 해당 user 객체가 존재한다면
        if customer is not None:
            # 로그인한다
            auth.login(request, customer)
            return redirect('goods')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')
    """

# 로그아웃
#@login_required 로그인 인증되어있을 때만 실행됨
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    auth.logout(request)
    return redirect('wait')