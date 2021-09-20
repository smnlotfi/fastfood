from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import MyUser
from django.contrib.auth import authenticate,login,logout


class SignUpForm(UserCreationForm):
    mobile=forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'شماره موبایل خود را وارد نمایید','class':'form-control'}),
        label='شماره موبایل'
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'رمز عبور خود را وارد نمایید', 'class': 'form-control'}),
        label='رمز عبور'
    )
    repassword = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'رمز عبور خود را دوباره وارد نمایید', 'class': 'form-control'}),
        label='تکرار رمز عبور'
    )
    smscode = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'کد ارسال شده به گوشیتان را وارد نمایید', 'class': 'form-control hidden','id':'sms-code'}),
        label='کد تایید',
        required=False,
        empty_value=True
    )

    class Meta:
        model=MyUser
        fields=['mobile','name','password','repassword']

class LoginForm(forms.Form):
    mobile=forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'شماره موبایل خود را وارد نمایید','class':'form-control'}),
        label='شماره موبایل'
    )
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'placeholder': 'رمز عبور خود را وارد نمایید', 'class': 'form-control'}),
    #     label='رمز عبور'
    # )
    # repassword = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'placeholder': 'رمز عبور خود را دوباره وارد نمایید', 'class': 'form-control'}),
    #     label='تکرار رمز عبور'
    # )
    smscode = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'کد ارسال شده به گوشیتان را وارد نمایید', 'class': 'form-control hidden','id':'sms-code'}),
        label='کد تایید',
        required=False,
        empty_value=True
    )
