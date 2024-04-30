from typing import Any
from django.core.paginator import Paginator
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse
from django.views.generic import ListView, DetailView

from .models import articles, Category

# Create your views here.

# def home(request, page=1):
#     article_list = articles.objects.published()
#     paginator = Paginator(article_list, 3)
#     Articles = paginator.get_page(page)

#     context = {
#         "articles" : Articles,
#     }
#     return render(request, 'blog/home.html', context)

# rewriting the home class base view

class ArticleList(ListView):
    # model = articles
    # template_name = 'blog/home.html'
    # context_object_name = "articles"
    queryset = articles.objects.published()
    paginate_by = 3


# def detail(request, slug):
#     context = {
#         'article' : get_object_or_404(articles.objects.published(), slug=slug),
#         "category" : Category.objects.filter(status=True),
#     }
#     return render(request, "blog/detail.html", context)

# rewriting the detail class base view

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(articles.objects.published(), slug= slug)
            

# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()
#     paginator = Paginator(articles_list, 3)
#     Articles = paginator.get_page(page)

#     context = {
#         "category" : category,
#         "articles" : Articles,
#     }
#     return render(request, "blog/category.html", context)

# rewriting the category class base view

class CategoryList(ListView):
    paginate_by = 3
    template_name = 'blog/category_list.html'
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        global category
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context