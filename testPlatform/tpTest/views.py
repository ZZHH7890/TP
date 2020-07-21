'''
@Author: joker.zhang
@Date: 2020-06-23 10:50:40
@LastEditors: joker.zhang
@LastEditTime: 2020-07-21 08:54:11
@Description: For Automation
'''

import os
import pytest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from common.com_test_runner import OperateTestRunner
from common.com_log import get_logger
from .models import TestCaseInfo

# Create your views here.


def execute_all_action(request):
    if request.method == "POST":
        test_case_pk = request.POST.getlist('test_case_ids')
    # 数组设置不了环境变量，转换为字符串
    test_case_pks = ','.join(test_case_pk)
    #os.environ.setdefault('test_case_id', test_case_pks)
    os.environ['test_case_id'] = test_case_pks
    pytest.main(OperateTestRunner.get_pytest_cmd())
    return render(request, 'tpTest/add_test_case.html')


def execute_action(request):
    if request.method == "POST":
        test_case_pk = request.POST["test_case_id"]
        #test_case = TestCaseInfo.objects.get(id=test_case_pk)

    #os.environ.setdefault('test_case_id', test_case_pk)
    os.environ['test_case_id'] = test_case_pk
    get_logger().info("pytest cmd:%s", OperateTestRunner.get_pytest_cmd())
    pytest.main(OperateTestRunner.get_pytest_cmd())

    return render(request, 'tpTest/add_test_case.html')


def add_form(request):
    return render(request, 'tpTest/add_test_case.html')


def add_action(request):
    if request.method == "POST":
        vname = request.POST["tname"]
        vurl = request.POST["turl"]
        vmethod = request.POST["tmethod"]
        vemail = request.POST["temail"]
        vpw = request.POST["tpw"]
        vproject = request.POST["tproject"]
        viteration = request.POST["titeration"]
        vsu_env = request.POST["tsu_env"]
        vparams = request.POST["tparams"]
        vchecker = request.POST["tchecker"]
        vtd_env = request.POST["ttd_env"]
        vowner = User.objects.get(id=request.POST["towner"])
        vremark = request.POST["tremark"]
        TestCaseInfo.objects.create(name=vname, url=vurl, method=vmethod, email=vemail,
                                    pw=vpw, project=vproject, iteration=viteration, su_env=vsu_env, params=vparams, checker=vchecker, td_env=vtd_env, owner=vowner, remark=vremark)
    return redirect('test_case_list')


def copy_form(request):
    if request.method == "POST":
        test_case_pk = request.POST["test_case_id"]
        test_case = TestCaseInfo.objects.get(id=test_case_pk)
    context = {}
    context['test_case'] = test_case
    return render(request, 'tpTest/copy_test_case.html', context)


def copy_action(request):
    if request.method == "POST":
        vname = request.POST["tname"]
        vurl = request.POST["turl"]
        vmethod = request.POST["tmethod"]
        vemail = request.POST["temail"]
        vpw = request.POST["tpw"]
        vproject = request.POST["tproject"]
        viteration = request.POST["titeration"]
        vsu_env = request.POST["tsu_env"]
        vparams = request.POST["tparams"]
        vchecker = request.POST["tchecker"]
        vtd_env = request.POST["ttd_env"]
        vowner = User.objects.get(id=request.POST["towner"])
        vremark = request.POST["tremark"]
        TestCaseInfo.objects.create(name=vname, url=vurl, method=vmethod, email=vemail,
                                    pw=vpw, project=vproject, iteration=viteration, su_env=vsu_env, params=vparams, checker=vchecker, td_env=vtd_env, owner=vowner, remark=vremark)
    return redirect('test_case_list')


def delete_action(request):
    if request.method == "POST":
        get_logger().info("request.POST:%s", request.POST)
        test_case_pk = request.POST["test_case_id"]
        TestCaseInfo.objects.filter(id=test_case_pk).delete()
    return redirect('test_case_list')


def delete_all_action(request):
    if request.method == "POST":
        test_case_pks = request.POST.getlist('test_case_ids')
        get_logger().info("删除的用例编号为:%s", test_case_pks)
        for test_case_pk in test_case_pks:
            if test_case_pk != '':
                TestCaseInfo.objects.filter(id=test_case_pk).delete()
    return redirect('test_case_list')


def update_form(request):
    if request.method == "POST":
        test_case_pk = request.POST["test_case_id"]
        test_case = TestCaseInfo.objects.get(id=test_case_pk)
    context = {}
    context['test_case'] = test_case
    return render(request, 'tpTest/update_test_case.html', context)


def update_action(request):
    if request.method == "POST":
        test_case_pk = request.POST["test_case_id"]
        vname = request.POST["tname"]
        vurl = request.POST["turl"]
        vmethod = request.POST["tmethod"]
        vemail = request.POST["temail"]
        vpw = request.POST["tpw"]
        vproject = request.POST["tproject"]
        viteration = request.POST["titeration"]
        vsu_env = request.POST["tsu_env"]
        vparams = request.POST["tparams"]
        vchecker = request.POST["tchecker"]
        vtd_env = request.POST["ttd_env"]
        vowner = User.objects.get(id=request.POST["towner"])
        vremark = request.POST["tremark"]
        TestCaseInfo.objects.filter(id=test_case_pk).update(name=vname, url=vurl, method=vmethod, email=vemail,
                                                            pw=vpw, project=vproject, iteration=viteration, su_env=vsu_env, params=vparams, checker=vchecker, td_env=vtd_env, owner=vowner, remark=vremark)
        return redirect('test_case_detail', test_case_pk=test_case_pk)


def test_case_list(request):
    test_case_all_list = TestCaseInfo.objects.all()
    paginator = Paginator(test_case_all_list, 5)
    page_num = request.GET.get('page', 1)
    page_of_test_cases = paginator.get_page(page_num)
    context = {}
    context['page_of_test_cases'] = page_of_test_cases
    return render(request, 'tpTest/test_case_list.html', context)


def test_case_detail(request, test_case_pk):
    context = {}
    context['test_case'] = get_object_or_404(TestCaseInfo, pk=test_case_pk)
    return render(request, 'tpTest/test_case_detail.html', context)
