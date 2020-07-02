'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-07-01 17:09:57
@Description: For Automation
'''
from django.db import models

# Create your models here.


class TestCases(models.Model):
    TC_name = models.CharField(max_length=500, verbose_name='用例概述')
    TC_set_up = models.TextField(verbose_name='用例前置')
    TC_params = models.TextField(verbose_name='接口参数')
    TC_checks = models.TextField(verbose_name='检验')
    TC_next_step = models.CharField(
        max_length=200, null=True, blank=True, default='无', verbose_name='下一步参数')
    TC_version = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='用例版本')

    class Meta:
        verbose_name = '用例概述'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.TC_name
