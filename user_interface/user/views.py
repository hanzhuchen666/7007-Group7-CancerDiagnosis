from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import hashlib
from .models import User


# Create your views here.
def login(request):
    if request.method == 'GET':
        if 'uid' in request.session and 'username' in request.session:
            #     return HttpResponse('您已登录')
            return render(request, 'user/login.html')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            return HttpResponse('用户名或密码不能为空')
        try:
            user = User.objects.get(username=username)
        except:
            HttpResponse('用户名或密码错误！')
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != user.password:
            HttpResponse('用户名或密码错误！')
        # 保持登录状态
        request.session['username'] = user.username
        request.session['uid'] = user.id
        # return HttpResponse('登录成功')
        return HttpResponseRedirect('/upload_image/index')


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_2 = request.POST['password_2']
        if not username or not password:
            return HttpResponse('用户和密码不能为空')
        if password != password_2:
            return HttpResponse('两次密码不一致')
        # return HttpResponseRedirect('user/register.html')
        # 对输入密码计算hash值
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        User.objects.create(username=username,
                            password=password_2)
        # return HttpResponse('registered successfully')
        return render(request,'user/login.html',locals())


def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
    if 'username' in request.session:
        del request.session['username']
    # return HttpResponse('用户退出成功')
    return render(request, 'user/login.html')
