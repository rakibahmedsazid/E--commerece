
from django.urls import path

from appstore import views


urlpatterns = [
    path('',views.home,name="home"),
    path('mens',views.mens,name="mens"),
    path('females',views.females,name="females"),
    path('toy',views.toy,name="toy"),
    path('chaild',views. chaild,name="chaild"),
    path('signup',views.signupPage,name="signup"),
    path('login',views.loginPage,name="login"),
    path('logout',views.logoutPage,name="logout"),
    path('details/<str:id>',views.details,name="details"),
    
]
