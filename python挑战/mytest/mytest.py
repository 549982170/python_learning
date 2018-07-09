# encoding:utf-8
# usr/bin/python
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley',},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# rows_by_fname = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# print(rows_by_fname)
# print(rows_by_uid)
# rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
# print(rows_by_lfname)
#
# rows_by_fname = sorted(rows, key=lambda r: r['fname'])
# rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
#
# print (min(rows, key=itemgetter('uid')))
# print (max(rows, key=itemgetter('uid')))


def mysortedByKeyList(dict_list, dict_key, rev=False):
    """列表字典按字典里面的列表key来排序
    @param dict_list: list字典列表
    @param dict_key: list字典排序的key列表(dict_list可不存在该key)
    @param rev:bool 是否倒序,Flase为升序,True为降序"""
    dict_list.sort(key=lambda x: tuple(x.get(ca) for ca in dict_key), reverse=rev)
    return dict_list

dict_key = ["lname", "fname"]
print mysortedByKeyList(rows, dict_key)