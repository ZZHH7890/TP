'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-06-23 11:40:32
@Description: For Automation
'''
from django.db import models

# Create your models here.

class TestCases(models.Model):
    TC_name = models.CharField(max_length=500)
    TC_set_up = models.TextField()
    TC_params= models.TextField()
    TC_checks= models.TextField()
    TC_next_step= models.CharField(max_length=200)
    TC_version = models.CharField(max_length=100)
