'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-07-20 14:53:36
@Description: For Automation
'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TestCaseInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='用例描述')
    url = models.CharField(max_length=100, verbose_name='请求地址')
    method = models.CharField(max_length=20, verbose_name='请求方法')
    email = models.EmailField(
        max_length=50, blank=True, null=True, verbose_name='登录邮箱')
    pw = models.CharField(max_length=20, blank=True,
                          null=True, verbose_name='登录密码')
    project = models.CharField(max_length=20, verbose_name='项目')
    iteration = models.CharField(max_length=20, verbose_name='迭代版本')
    su_env = models.TextField(max_length=200, blank=True,
                              null=True, verbose_name='前提条件设置')
    params = models.TextField(max_length=200, verbose_name='请求参数')
    ret = models.TextField(max_length=200, blank=True,
                           null=True, verbose_name='接口响应')
    checker = models.TextField(max_length=100, verbose_name='检验')
    next_step = models.TextField(max_length=100, blank=True,
                                 null=True, verbose_name='多业务数据')
    td_env = models.TextField(max_length=200, blank=True,
                              null=True, verbose_name='清理数据')
    owner = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='维护人员')
    created_time = models.DateTimeField(
        auto_now_add=True, verbose_name='创建时间')
    last_updated_time = models.DateTimeField(
        auto_now=True, verbose_name='最后维护时间')
    remark = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '用例描述'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
