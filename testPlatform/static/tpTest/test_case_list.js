/*
 * @Author: joker.zhang
 * @Date: 2020-07-15 11:06:43
 * @LastEditors: joker.zhang
 * @LastEditTime: 2020-07-20 19:32:54
 * @Description: For Automation
 */

// https://www.cnblogs.com/xiximayou/p/11792875.html
function selectAll() {
    var select_all_box = document.getElementById("select_all");       //全选/反选的选择框id
    var check_boxs = document.getElementsByName("check_box");    //单选框check_box
    var num = check_boxs.length;
    if (select_all_box.checked) {
        for (var index = 0; index < num; index++) {
            check_boxs[index].checked = true;
        }
    } else {
        for (var index = 0; index < num; index++) {
            check_boxs[index].checked = false;
        }
    }
}

function selectOne() {
    var one = document.getElementsByName("check_box");
    one.checked = true;
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


// https://www.cnblogs.com/xiximayou/p/11792875.html
function getDeleteValues() {
    var valArr = [];
    var ones = document.getElementsByName('check_box');
    for (var i = 0; i < ones.length; i++) {
        if (ones[i].checked == true) {
            valArr[i] = ones[i].value
        }
    }
    if (valArr.length != 0) {
        // var vals = valArr.join(',');
        // alert(valArr);
        $.ajax({
            // 地址一定要正确
            url: "delete_all_action/",
            // 全部大写
            type: 'POST',
            dateType:'JSON',
            // contentType: 'application/json',
            // 不加这个，ajax会将结果后边加个[]，例如{ 'vals[]': [4, 6, 8] }
            traditional: true,
            //不加这个，会报服务器终止了一个在运行的程序
            async: false,
            data: {
                'test_case_ids': valArr
            },
            // https://blog.csdn.net/qq_43054982/article/details/85269403
            headers: { "X-CSRFtoken": getCookie("csrftoken") },
            success: function () {
                alert("删除成功");
                window.location.reload(true);
            },
            error: function () {
                alert("删除失败");
            }
        })
    }
    else {
        var error_m = "请选择数据";
        alert(error_m);
    }
}

function getExecuteValues() {
    var valArr = [];
    var ones = document.getElementsByName('check_box');
    for (var i = 0; i < ones.length; i++) {
        if (ones[i].checked == true) {
            valArr[i] = ones[i].value
        }
    }
    if (valArr.length != 0) {
        // var vals = valArr.join(',');
        // alert(valArr);
        $.ajax({
            // 地址一定要正确
            url: "execute_all_action/",
            // 全部大写
            type: 'POST',
            dateType:'JSON',
            // contentType: 'application/json',
            // 不加这个，ajax会将结果后边加个[]，例如{ 'vals[]': [4, 6, 8] }
            traditional: true,
            //不加这个，会报服务器终止了一个在运行的程序
            async: false,
            data: {
                'test_case_ids': valArr
            },
            // https://blog.csdn.net/qq_43054982/article/details/85269403
            headers: { "X-CSRFtoken": getCookie("csrftoken") },
            success: function () {
                alert("执行成功");
                window.location.reload(true);
            },
            error: function () {
                alert("执行失败");
            }
        })
    }
    else {
        var error_m = "请选择数据";
        alert(error_m);
    }
}