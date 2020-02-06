import xadmin
from .models import *
# Register your models here.
class CommentAdmin(object):
    list_display = ('user', 'comment_time', 'object_id')

xadmin.site.register(Comment, CommentAdmin)