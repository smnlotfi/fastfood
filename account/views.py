from django.shortcuts import render,redirect
from account.forms import SignUpForm,LoginForm
from account.models import MyUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.sessions.models import Session

import random

# Create your views here.



def SignUp(request):
    if request.user.is_authenticated:
        return redirect('/')
    Form=SignUpForm(request.POST or None)
    context = {
        'Form': Form,
    }
    if request.is_ajax():
        if request.POST:
            smscode=request.POST.get('smscode')
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            mobile = request.POST.get('mobile')
            if smscode != '':
                user = MyUser.objects.filter(mobile=mobile).first()
                code = user.sms_code
                if smscode == code:
                    user.is_active=True
                    user.save()
                    login(request, user)
                    response = {'msg': 'شما با موفقیت ثبت نام کردید!', 'ok': 'true'}
                else:
                    response = {'msg': 'کد وارد شده صحیح نمیباشد دوباره امتحان کنید', 'ok': 'false'}
            else:
                if password != repassword:
                    response = {'msg': 'رمز عبور شما تطابق ندارد دوباره امتحان کنید', 'ok': 'false'}
                else:
                    mobile = request.POST.get('mobile')
                    user = MyUser.objects.filter(mobile=mobile).first()
                    if user == None:
                        response = {'msg': 'not-code'}
                        password = request.POST.get('password')
                        user = MyUser.objects.create_user(mobile=mobile, password=password)
                        code = random.randint(1000, 9999)

                        # عملیات انجام ارسال کد به گوشی

                        code = str(code)
                        user.sms_code=code
                        user.save()

                    else:
                        response = {'msg': 'این شماره قبلا ثبت نام کرده است.', 'ok': 'false'}



        return JsonResponse(response)
    else:
        return render(request, 'signup.html', context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    Form=LoginForm(request.POST or None)
    context = {
        'Form': Form,
    }
    if request.is_ajax():
        if request.POST:
            smscode=request.POST.get('smscode')
            mobile = request.POST.get('mobile')
            user = MyUser.objects.filter(mobile=mobile).first()
            if user is None:
                response={'msg':'کاربری با این شماره موجود نیست اگر عضو نیستید ثبت نام کنید'}
            else:
                if smscode != '':
                    code = user.sms_code
                    print(code)
                    if smscode == code:
                        login(request, user)
                        response = {'msg': 'شما با موفقیت وارد شدید', 'ok': 'true'}
                    else:
                        response = {'msg': 'کد وارد شده صحیح نمیباشد دوباره امتحان کنید', 'ok': 'false'}
                else:
                    response = {'msg': 'not-code'}
                    user = MyUser.objects.filter(mobile=mobile).first()
                    code = random.randint(1000, 9999)

                    # عملیات انجام ارسال کد به گوشی

                    code = str(code)
                    user.sms_code = code
                    user.save()

        return JsonResponse(response)
    else:
        return render(request, 'login.html', context)


