from django.urls import path
from account.views import SignUp,Login,logout


urlpatterns = [
    path('signup',SignUp,name='signup'),
    path('login',Login,name='login')
    ]