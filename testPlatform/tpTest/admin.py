'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-07-18 23:45:50
@Description: For Automation
'''
# Register your models here.
from django.contrib import admin
from .models import TestCaseInfo


@admin.register(TestCaseInfo)
class TestCaseInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'method',
                    'email', 'pw', 'project', 'params', 'checker', 'su_env', 'td_env', 'created_time', 'last_updated_time']
    list_filter = ['iteration', 'owner']
    search_fields = ['name']
    list_per_page = 10


# admin.site.register(TestCases,TestCasesAdmin)
