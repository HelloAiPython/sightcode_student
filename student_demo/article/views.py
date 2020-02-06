from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, Http404
from .models import Article, ArticleType
from comment.models import Comment
from comment.forms import CommentForm
# Create your views here.


def article_list(request):
    articles_all_list = Article.objects.all()
    paginator = Paginator(articles_all_list, 6)
    page_num = request.GET.get('page', 1)
    page_of_articles = paginator.get_page(page_num)
    current_page_num = page_of_articles.number
    page_range = list(range(max(current_page_num-2,1),current_page_num-1))+\
                 list(range(current_page_num, min(current_page_num+2, paginator.num_pages)+1))
    context = {}
    context['articles'] = page_of_articles.object_list
    context['page_of_articles'] = page_of_articles
    context['page_range'] = page_range
    context['article_types'] = ArticleType.objects.all()
    return render(request, "article_list.html", context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article_content_type = ContentType.objects.get_for_model(article)
    comments = Comment.objects.filter(content_type=article_content_type, object_id=article.pk)
    comment_form = CommentForm()
    context = {}
    context['article'] = article
    context['comments'] = comments
    context['comment_form'] = comment_form
    return render(request, "article_detail.html", context)

def article_with_type(request, article_type_pk):
    context = {}
    article_type = get_object_or_404(ArticleType, pk=article_type_pk)
    context['articles'] = Article.objects.filter(article_type=article_type)
    context['article_type'] = article_type
    context['article_types'] = ArticleType.objects.all()
    return render(request, 'articles_with_type.html', context)