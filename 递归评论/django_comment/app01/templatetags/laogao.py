#__author:  Administrator
#date:  2016/12/26
from django import template
from django.utils.safestring import mark_safe
register = template.Library()

def diGui(children_list):
    html = ""
    for cv in children_list:
        b = '<div class="comment-box"><span>'
        b += cv['content'] + "</span>"
        b += diGui(cv['children'])
        b += "</div>"
        html += b
    return html

@register.simple_tag
def create_tree(comment_list):
    html = '<div class="comment-list">'
    for v in comment_list:
        a = '<div class="comment-box"><span>'
        a += v['content'] + "</span>"
        a += diGui(v['children'])
        a += "</div>"
        html += a

    return mark_safe(html)

"""
 function diGui(children_list){
                var html = "";
                $.each(children_list,function (ck,cv) {
                       var b = '<div class="comment-box"><span>';
                       b+= cv.content + "</span>";
                       b += diGui(cv.children);
                       b += "</div>";
                       html += b;
                 });
                return html;
            }


            function create_tree(data,$this) {
                 var html = '<div class="comment-list">';
                 $.each(data,function (k,v) {
                    var a = '<div class="comment-box"><span>';
                     a+= v.content + "</span>";
                     // 创建自评论
                     a += diGui(v.children);
                     a+= "</div>";
                     html += a;
                 });

                 html += "</div>";
                $this.after(html);
        }
    """
