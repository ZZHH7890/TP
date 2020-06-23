'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-06-23 17:20:07
@Description: For Automation
'''
from django.contrib import admin
from .models import TestCases

# Register your models here.
admin.site.register(TestCases)
