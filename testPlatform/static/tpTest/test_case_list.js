/*
 * @Author: joker.zhang
 * @Date: 2020-07-15 11:06:43
 * @LastEditors: joker.zhang
 * @LastEditTime: 2020-07-15 19:59:48
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

function getValues() {
    var valArr = [];
    var ones = document.getElementsByName('item');
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
            contenType: 'application/json',
            // 不加这个，ajax会将结果后边加个[]，例如{ 'vals[]': [4, 6, 8] }
            traditional: true,
            //不加这个，会报服务器终止了一个在运行的程序
            async: false,
            data: {
                'vals': valArr
            },
            success: function () {
                alert("删除成功");
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