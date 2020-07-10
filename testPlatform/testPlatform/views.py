'''
@Author: joker.zhang
@Date: 2020-07-02 18:52:30
@LastEditors: joker.zhang
@LastEditTime: 2020-07-09 14:06:28
@Description: For Automation
'''
from django.shortcuts import render_to_response


def home(request):
    context = {'welcome':'欢迎访问'}
    return render_to_response('home.html', context)
