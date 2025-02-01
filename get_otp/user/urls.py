
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('verify_otp',views.verify_otp,name="verify_otp")
]
