from django.urls import path
from app1.views import *

app_name='nani'
urlpatterns=[
    path('app1_fun/',app1_fun,name='app1_fun'),
]