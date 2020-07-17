'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-07-17 19:43:09
@Description: For Automation
'''

import os
import pytest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from common.test_runner import OperateTestRunner
from common.log import get_logger
from .models import TestCases

# Create your views here.


def execute_action(request):
    if request.method == "POST":
        test_case_pk = request.POST["test_case_id"]
        test_case = TestCases.objects.get(id=test_case_pk)
    name = test_case.TC_name
    su = test_case.TC_set_up
    pa = test_case.TC_params
    cer = test_case.TC_checks
    ns = test_case.TC_next_step
    pro = test_case.TC_project
    ver = test_case.TC_version
    oer = test_case.owner
    re = test_case.TC_remark

    get_logger().info("用例编号为:%s", test_case_pk)
    get_logger().info("用例名称为:%s", name)
    get_logger().info("用例前提条件为:%s", su)
    get_logger().info("用例参数为:%s", pa)
    get_logger().info("用例检验为:%s", cer)
    get_logger().info("用例下一步为:%s", ns)
    get_logger().info("用例项目为:%s", pro)
    get_logger().info("用例版本为:%s", ver)
    get_logger().info("用例维护人为:%s", oer)
    get_logger().info("用例备注为:%s", re)
    os.environ.setdefault('test_case_id',test_case_pk)
    os.environ.setdefault('test_case_name',name)
    os.environ.setdefault('test_case_set_up',su)
    os.environ.setdefault('test_case_params',pa)
    os.environ.setdefault('test_case_checkers',cer)
    os.environ.setdefault('test_case_next_step',ns)
    os.environ.setdefault('test_case_project',pro)
    os.environ.setdefault('test_case_version',ver)
    os.environ.setdefault('test_case_owner',oer)
    os.environ.setdefault('test_case_remark',re)
    get_logger().info("pytest cmd:%s", OperateTestRunner.get_pytest_cmd())
    pytest.main(OperateTestRunner.get_pytest_cmd())

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
        get_logger().info("request.POST:%s", request.POST)
        test_case_pk = request.POST["test_case_id"]
        TestCases.objects.filter(id=test_case_pk).delete()
    return redirect('test_case_list')


def delete_all_action(request):
    if request.method == "POST":
        test_case_pks = request.POST.getlist('test_case_ids')
        get_logger().info("删除的用例编号为:%s", test_case_pks)
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
