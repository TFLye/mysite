from django.db import models
from article.models import ArticlePost
# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(ArticlePost,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80,default='tfl',null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]
