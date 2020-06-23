'''
@Author: joker.zhang
@Date: 2020-06-23 14:30:15
@LastEditors: joker.zhang
@LastEditTime: 2020-06-23 14:59:20
@Description: For Automation
'''

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
]

