from django.urls import path,include
from register import views

urlpatterns = [
    path('home',views.home_register,name='home_register'),
     path('register',views.sup_register,name='sup_register'),
    # path('register_response',views.sup_response,name='sup_response')
 ]
 