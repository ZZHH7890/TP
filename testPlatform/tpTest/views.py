'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-07-06 17:27:24
@Description: For Automation
'''
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import TestCases

# Create your views here.


def test_case_list(request):
    test_case_all_list = TestCases.objects.all()
    paginator = Paginator(test_case_all_list, 5)
    page_num = request.GET.get('page', 1)
    page_of_test_cases = paginator.get_page(page_num)
    context = {}
    context['page_of_test_cases'] = page_of_test_cases
    return render(request, 'tpTest/test_case_list.html', context)


def test_case_detail(request, test_case_pk):
    context = {}
    context['test_case'] = get_object_or_404(TestCases, pk=test_case_pk)
    return render(request, 'tpTest/test_case_detail.html', context)
