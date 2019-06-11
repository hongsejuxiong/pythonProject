#__author:  Administrator
#date:  2016/12/26
"""
li = [
    {'id': 1, 'name': 'root1', 'pid': 0},
    {'id': 2, 'name': 'root1', 'pid': 0},
    {'id': 3, 'name': 'root1', 'pid': 0},
    {'id': 4, 'name': 'root1', 'pid': 0},
]
# v = li
# v.append([999,000,])
# print(li)
for item in li:
    item.update({'children': []})

for row in li:
    if row['id'] == 3:
        row['children'].append(row)

for i in li:
    print(i,i['children'])

li[2]['name'] = "dfasdfasdfasdf"

for i in li:
    print(i,i['children'])
"""

comment_list = [
        {'id': 1, 'content': 'Python最牛逼', 'user': '搞基建', 'parent_id': None},
        {'id': 2, 'content': 'Java最牛逼', 'user': '搞基建', 'parent_id': None},
        {'id': 3, 'content': 'PHP最牛逼', 'user': '搞基建', 'parent_id': None},
        {'id': 4, 'content': '你最牛逼1232', 'user': '小比虎', 'parent_id': 1},
        {'id': 5, 'content': '老师最你比', 'user': '李欢', 'parent_id': 1},
        {'id': 6, 'content': '郭永昌是...', 'user': '郭永昌', 'parent_id': 4},
        {'id': 7, 'content': '哈哈我是流氓...', 'user': '崔月圆', 'parent_id': 2},
        {'id': 8, 'content': '我女朋友好漂亮...', 'user': '崔月圆', 'parent_id': 3},
        {'id': 9, 'content': '见到你女友，交定你朋友...', 'user': '搞基建', 'parent_id': 6},
        {'id': 10, 'content': '见到你女友，交定你朋友...', 'user': '鼻环', 'parent_id': None},
    ]

ret = []
comment_list_dict = {}

for row in comment_list:
        row.update({'children': []})
        comment_list_dict[row['id']] = row
"""
comment_list_dict
{
        1: {'id': 1, 'content': 'Python最牛逼', 'user': '搞基建', 'parent_id': None, 'children': []},
        1: {'id': 1, 'content': 'Python最牛逼', 'user': '搞基建', 'parent_id': None, 'children': []},
        1: {'id': 1, 'content': 'Python最牛逼', 'user': '搞基建', 'parent_id': None, 'children': []},
        1: {'id': 1, 'content': 'Python最牛逼', 'user': '搞基建', 'parent_id': None, 'children': []},
        1: {'id': 1, 'content': 'Python最牛逼', 'user': '搞基建', 'parent_id': None, 'children': []},
        1: {'id': 1, 'content': 'Python最牛逼', 'user': '搞基建', 'parent_id': None, 'children': []},
        10: {'id': 1, 'content': 'Python最牛逼', 'user': '搞基建', 'parent_id': None, 'children': []},
}
"""
for item in comment_list:
        parent_row = comment_list_dict.get(item['parent_id'])
        if not parent_row:
                ret.append(item)
        else:
                parent_row['children'].append(item)
print(ret)