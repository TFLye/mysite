# 引入path
from django.urls import path,include
from article import views
# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('',views.article_list, name='article_list'),
    # path('list/', views.article_list, name='article_list'),
    path('details/<int:article_id>', views.article_details, name='article_details'),
]