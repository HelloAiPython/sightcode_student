from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class ArticleType(models.Model):
    type_name = models.CharField(verbose_name='分类', max_length=30)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
    def __str__(self):
        return self.type_name

class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=30)
    article_type = models.ForeignKey(ArticleType, verbose_name='选择类别', on_delete=models.CASCADE, blank=True, null=True)
    content = RichTextUploadingField(verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    #last_updated_time = models.DateTimeField(verbose_name='最近更新', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        ordering = ['-create_time']
        verbose_name = '题目'
        verbose_name_plural = '题目'
    def __str__(self):
        return self.title