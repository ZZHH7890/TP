'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-07-02 10:44:11
@Description: For Automation
'''
from django.shortcuts import render, get_object_or_404
from .models import TestCases

# Create your views here.


def test_case_list(request):
    context = {}
    context['test_cases'] = TestCases.objects.all()
    return render(request, 'tpTest/test_case_list.html', context)


def test_case_detail(request, test_case_pk):
    context = {}
    context['test_case'] = get_object_or_404(TestCases, pk=test_case_pk)
    return render(request, 'tpTest/test_case_detail.html', context)
