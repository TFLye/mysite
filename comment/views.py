from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from article.models import ArticlePost
from .forms import CommentForm
import http.client
import urllib
# 文章评论
def post_comment(request,article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    comments = article.comments.filter(active=True)
    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            # new_comment.user = request.user
            new_comment.save()
            return redirect("/article/details/"+str(article_id))
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")

# 通过qq号获取name
def get_qq_msg(request):
    # 1. 建立HTTP连接
    res = urllib.request.urlopen("https://api.toubiec.cn/qq?qq=2320456951&size=100")
    # print(res.read().decode("utf-8"))  # 自己解码
    return HttpResponse(res.read().decode("utf-8"))