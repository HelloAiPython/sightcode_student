import xadmin
from .models import *
# Register your models here.
class ArticleAdmin(object):
    list_display = ('id', 'title', 'author', 'create_time',)
class ArticleTypeAdmin(object):
    list_display = ('id', 'type_name', )

xadmin.site.register(ArticleType, ArticleTypeAdmin)
xadmin.site.register(Article, ArticleAdmin)
