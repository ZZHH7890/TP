'''
@Author: joker.zhang
@Date: 2020-06-23 14:30:15
@LastEditors: joker.zhang
@LastEditTime: 2020-07-10 17:47:30
@Description: For Automation
'''

from django.urls import path
from . import views

urlpatterns = [
    path('test_case_list/', views.test_case_list, name='test_case_list'),
    path('<int:test_case_pk>', views.test_case_detail, name='test_case_detail'),
    path('add_test_case_from/', views.add_test_case_form, name='add_test_case_form')
]
