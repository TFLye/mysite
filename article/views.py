from django.shortcuts import render
from django.core.paginator import Paginator
from comment.models import Comment
# 导入 HttpResponse 模块
from django.http import HttpResponse
# 导入数据模型ArticlePost
from .models import ArticlePost
import markdown


def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    for article in articles:
        article.body = markdown.markdown(article.body, extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
        ])
    # 需要传递给模板（templates）的对象
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    # render函数：载入模板，并返回context对象
    return render(request, 'article/blog.html', {'articles': articles})


# 视图函数
def article_details(request, article_id):
    article = ArticlePost.objects.get(pk=article_id)
    comments = Comment.objects.filter(article=article_id)
    article.totalviews += 1
    article.save(update_fields = ['totalviews'])
    md = markdown.Markdown(extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ])
    article.body = md.convert(article.body);
    context = {'article': article,'toc':md.toc,'comments': comments}
    return render(request, 'article/details.html', context)
# Create your views here.
