from django.urls import path,include
from .views import great,getname,users,greet_to_users

urlpatterns=[
    path('message',great),
    path('getname',getname),
    path('users',users),
    path('user_message/<str:name>',greet_to_users),
]