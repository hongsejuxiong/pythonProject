from django.shortcuts import render,HttpResponse
from app01 import models

def index(request):
    return render(request, 'index.html')


def comment(request):
    news_id = request.GET.get('news_id')
    # models.xxx.filter(news_id=news_id).values(...)
    comment_list = [
        {'id': 1, 'content': 'Python最牛逼', 'user': '搞基建', 'parent_id': None},
        {'id': 2, 'content': 'Java最牛逼', 'user': '搞基建', 'parent_id': None},
        {'id': 3, 'content': 'PHP最牛逼', 'user': '搞基建', 'parent_id': None},
        {'id': 4, 'content': '你最牛逼', 'user': '小比虎', 'parent_id': 1},
        {'id': 5, 'content': '老师最你比', 'user': '李欢', 'parent_id': 1},
        {'id': 6, 'content': '郭永昌是...', 'user': '郭永昌', 'parent_id': 4},
        {'id': 7, 'content': '哈哈我是流氓...', 'user': '崔月圆', 'parent_id': 2},
        {'id': 8, 'content': '我女朋友好漂亮...', 'user': '崔月圆', 'parent_id': 3},
        {'id': 9, 'content': '见到你女友，交定你朋友...', 'user': '搞基建', 'parent_id': 8},
        {'id': 10, 'content': '见到你女友，交定你朋友...', 'user': '鼻环', 'parent_id': None},
        {'id': 11, 'content': '我是大胖...', 'user': 'xiaopang', 'parent_id': 6},
    ]
    comment_tree = []
    comment_list_dict = {}

    for row in comment_list:
        row.update({'children': []})
        comment_list_dict[row['id']] = row
    for item in comment_list:
        parent_row = comment_list_dict.get(item['parent_id'])
        if not parent_row:
            comment_tree.append(item)
        else:
            parent_row['children'].append(item)

    # import json
    # return HttpResponse(json.dumps(comment_tree))
    return render(request, 'comment.html', {'comment_tree': comment_tree})



