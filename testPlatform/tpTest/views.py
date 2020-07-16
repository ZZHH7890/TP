'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-07-16 23:59:55
@Description: For Automation
'''

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from common.log import OperateLog
from .models import TestCases

# Create your views here.


def execute_action(request):

    return render(request, 'tpTest/add_test_case.html')




def add_form(request):
    return render(request, 'tpTest/add_test_case.html')


def add_action(request):
    if request.method == "POST":
        name = request.POST["TC_name"]
        su = request.POST["TC_set_up"]
        pa = request.POST["TC_params"]
        cer = request.POST["TC_checks"]
        ns = request.POST["TC_next_step"]
        pro = request.POST["TC_project"]
        ver = request.POST["TC_version"]
        oer = User.objects.get(id=request.POST["owner"])
        re = request.POST["TC_remark"]
        TestCases.objects.create(TC_name=name, TC_set_up=su, TC_params=pa, TC_checks=cer,
                                 TC_next_step=ns, TC_project=pro, TC_version=ver, owner=oer, TC_remark=re)
    return redirect('test_case_list')


def copy_form(request):
    if request.method == "POST":
        test_case_pk = request.POST["test_case_id"]
        test_case = TestCases.objects.get(id=test_case_pk)
    context = {}
    context['test_case'] = test_case
    return render(request, 'tpTest/copy_test_case.html', context)


def copy_action(request):
    if request.method == "POST":
        name = request.POST["TC_name"]
        su = request.POST["TC_set_up"]
        pa = request.POST["TC_params"]
        cer = request.POST["TC_checks"]
        ns = request.POST["TC_next_step"]
        pro = request.POST["TC_project"]
        ver = request.POST["TC_version"]
        oer = User.objects.get(id=request.POST["owner"])
        re = request.POST["TC_remark"]
        TestCases.objects.create(TC_name=name, TC_set_up=su, TC_params=pa, TC_checks=cer,
                                 TC_next_step=ns, TC_project=pro, TC_version=ver, owner=oer, TC_remark=re)
    return redirect('test_case_list')


def delete_action(request):
    if request.method == "POST":
        OperateLog.get_logger().info("request.POST:%s", request.POST)
        test_case_pk = request.POST["test_case_id"]
        TestCases.objects.filter(id=test_case_pk).delete()
    return redirect('test_case_list')


def delete_all_action(request):
    if request.method == "POST":
        test_case_pks = request.POST.getlist('test_case_ids')
        OperateLog.get_logger().info("test_case_pks:%s", test_case_pks)
        OperateLog.get_logger().info("test_case_pks type:%s", type(test_case_pks))
        for test_case_pk in test_case_pks:
            if test_case_pk != '':
                TestCases.objects.filter(id=test_case_pk).delete()
    return redirect('test_case_list')


def update_form(request):
    if request.method == "POST":
        test_case_pk = request.POST["test_case_id"]
        test_case = TestCases.objects.get(id=test_case_pk)
    context = {}
    context['test_case'] = test_case
    return render(request, 'tpTest/update_test_case.html', context)


def update_action(request):
    if request.method == "POST":
        test_case_pk = request.POST["test_case_id"]
        name = request.POST["TC_name"]
        su = request.POST["TC_set_up"]
        pa = request.POST["TC_params"]
        cer = request.POST["TC_checks"]
        ns = request.POST["TC_next_step"]
        pro = request.POST["TC_project"]
        ver = request.POST["TC_version"]
        oer = User.objects.get(id=request.POST["owner"])
        re = request.POST["TC_remark"]
        TestCases.objects.filter(id=test_case_pk).update(TC_name=name, TC_set_up=su, TC_params=pa, TC_checks=cer,
                                                         TC_next_step=ns, TC_project=pro, TC_version=ver, owner=oer, TC_remark=re)
        return redirect('test_case_detail', test_case_pk=test_case_pk)


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
