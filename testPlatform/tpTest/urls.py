'''
@Author: joker.zhang
@Date: 2020-06-23 14:30:15
@LastEditors: joker.zhang
@LastEditTime: 2020-07-13 14:29:48
@Description: For Automation
'''

from django.urls import path
from . import views

urlpatterns = [
    path('test_case_list/', views.test_case_list, name='test_case_list'),
    path('<int:test_case_pk>', views.test_case_detail, name='test_case_detail'),
    path('add_test_case/', views.add_form, name='add_form'),
    path('add_test_case/add_action/', views.add_action, name='add_action'),
    path('test_case_list/update_form/', views.update_form, name='update_form'),
    path('test_case_list/update_form/update_action/', views.update_action, name='update_action'),
    path('test_case_list/delete_action/', views.delete_action, name='delete_action'),
]
