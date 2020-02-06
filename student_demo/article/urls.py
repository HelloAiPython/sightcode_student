from django.urls import path
from . import views
urlpatterns = [
    #localhost:8000/article/
    path('', views.article_list, name='article_list'),
    #localhost:8000/article/1
    path('<int:article_id>', views.article_detail, name='article_detail'),
    path('type/<int:article_type_pk>', views.article_with_type, name='article_with_type'),
]