from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse

from .models import articles, Category

# Create your views here.

def home(request, page=1):
    article_list = articles.objects.published()
    paginator = Paginator(article_list, 3)
    Articles = paginator.get_page(page)

    context = {
        "articles" : Articles,
    }
    return render(request, 'blog/home.html', context)

def detail(request, slug):
    context = {
        'article' : get_object_or_404(articles.objects.published(), slug=slug),
        "category" : Category.objects.filter(status=True),
    }
    return render(request, "blog/detail.html", context)

def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 3)
    Articles = paginator.get_page(page)


    context = {
        "category" : category,
        "articles" : Articles,

    }
    return render(request, "blog/category.html", context)
