from django.urls import path
from .views import ArticleList, ArticleDetail, CategoryList


app_name = 'Blog'
urlpatterns = [
    # path('home/', home, name='Home'),
    # path('home/page/<int:page>', home, name='Home'),
    path('home/', ArticleList.as_view(), name='Home'),
    path('home/page/<int:page>', ArticleList.as_view(), name='Home'),
    path('detail/<slug:slug>', ArticleDetail.as_view(), name = 'Detail'),
    path('category/<slug:slug>', CategoryList.as_view(), name = 'category'),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name = 'category'),
]
