'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-07-07 17:47:19
@Description: For Automation
'''
# Register your models here.
from django.contrib import admin
from .models import TestCases


@admin.register(TestCases)
class TestCasesAdmin(admin.ModelAdmin):
    list_display = ['TC_name', 'TC_set_up', 'TC_params',
                    'TC_checks', 'TC_next_step', 'TC_version', 'owner', 'created_time', 'last_updated_time']
    list_filter = ['TC_version', 'owner']
    search_fields = ['TC_name']
    list_per_page = 10


# admin.site.register(TestCases,TestCasesAdmin)
