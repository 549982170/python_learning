# coding:utf-8
# !/user/bin/python
'''
Created on 2017年9月15日
@author: yizhiwu
接口测试函数
备注:GET请求参数放在body里面
'''
from mytest.util import myrequest

# 剧本预算(新增)
url = "/budget/api/save/script_budget"
playload = {
    "budget_id": 1,
    "budget_list": [
        {"budget_id": 1,
         "code": "S00010001",
         "budget_type": "筹划费用",
         "per_money": "2000",
         "unit": "集",
         "amount": "30",
         "total": "6000",
         "remark": "备注",
         "user_id": "1",
         },
        {
            "budget_id": 1,
            "code": "S00010001",
            "budget_type": "筹划费用",
            "per_money": "2000",
            "unit": "集",
            "amount": "30",
            "total": "6000",
            "remark": "备注",
            "user_id": "1",
        }
    ]
}

result = myrequest(url, playload, data_type="json")
print result

# 剧组人员预算(新增)
url = "/budget/api/save/department_budget"
playload = {
    "budget_id": 1,
    "budget_list": [
        {"budget_id": 1,
         "code": "S00010001",
         "department": "测试部门",
         "job": "职务测试",
         "member_amount": "30",
         "total_member_amount": "20",
         "per_money": "30.4",
         "unit": "单位",
         "time": "2.5",
         "total": "100.1",
         "department_total": "100.1",
         "remark": "备注",
         },
        {
            "budget_id": 1,
            "code": "S00010001",
            "department": "测试部门2",
            "job": "职务测试2",
            "member_amount": "30",
            "total_member_amount": "20",
            "per_money": "30.4",
            "unit": "单位2",
            "time": "2.5",
            "total": "100.1",
            "department_total": "100.1",
            "remark": "备注2",
        }
    ]
}

result = myrequest(url, playload, data_type="json")
print result

# 演员预算预算(新增)
url = "/budget/api/save/character_budget"
playload = {
    "budget_id": 1,
    "budget_list": [
        {"budget_id": 1,
         "code": "S00010001",
         "character_type": "演员类型",
         "member_amount": "10",
         "per_money": 800.00,
         "unit": "天",
         "time": "30.4",
         "unit": "单位",
         "total": "100",
         "remark": "备注",
         },
        {
            "budget_id": 1,
            "code": "S00010001",
            "character_type": "演员类型2",
            "member_amount": "10",
            "per_money": 800.00,
            "unit": "天",
            "time": "30.4",
            "unit": "单位2",
            "total": "100",
            "remark": "备注2",
        }
    ]
}

result = myrequest(url, playload, data_type="json")
print result

# 办公用品预算(新增)
url = "/budget/api/save/office_supplies_budget"
playload = {
    "budget_id": 1,
    "budget_list": [
        {"budget_id": 1,
         "code": "S00010001",
         "office_supplies_type": "办公类型",
         "department": "部门1",
         "description": "相关人员及内容",
         "per_money": 100.1,
         "unit": "单位",
         "time": "20",
         "amount": 100,
         "total": 100.0,
         "remark": "备注",
         },
        {"budget_id": 1,
         "code": "S00010001",
         "office_supplies_type": "办公类型2",
         "department": "部门2",
         "description": "相关人员及内容2",
         "per_money": 100.1,
         "unit": "单位2",
         "time": "20",
         "amount": 100,
         "total": 100.0,
         "remark": "备注",
         }
    ]
}

result = myrequest(url, playload, data_type="json")
print result

# 设备预算(新增)
url = "/budget/api/save/equipment_budget"
playload = {
    "budget_id": 1,
    "budget_list": [
        {"budget_id": 1,
         "code": "S00010001",
         "equipment_type": "设备类型",
         "department": "部门1",
         "project_type": "项目类型",
         "per_money": 10.5,
         "unit": "单位",
         "time": "20",
         "amount": 100,
         "total": 100.0,
         "remark": "备注",
         },
        {"budget_id": 1,
         "code": "S00010001",
         "equipment_type": "设备类型2",
         "department": "部门2",
         "project_type": "项目类型2",
         "per_money": 10.5,
         "unit": "单位2",
         "time": "20",
         "amount": 100,
         "total": 100.0,
         "remark": "备注2",
         }
    ]
}

result = myrequest(url, playload, data_type="json")
print result

# 设备预算(新增)
url = "/budget/api/save/place_budget"
playload = {
    "budget_id": 1,
    "budget_list": [
        {"budget_id": 1,
         "code": "S00010001",
         "place_type": "场地类型",
         "per_money": 10.5,
         "unit": "单位",
         "time": "20",
         "amount": 100,
         "total": 100.0,
         "remark": "备注",
         },
        {"budget_id": 1,
         "code": "S00010001",
         "place_type": "场地类型2",
         "per_money": 10.5,
         "unit": "单位2",
         "time": "20",
         "amount": 100,
         "total": 100.0,
         "remark": "备注2",
         }
    ]
}

result = myrequest(url, playload, data_type="json")
print result
