from django.urls import path
from .views import home
from .views import detail, category

app_name = 'Blog'
urlpatterns = [
    path('home/', home, name='Home'),
    path('home/page/<int:page>', home, name='Home'),
    path('detail/<slug:slug>', detail, name = 'Detail'),
    path('category/<slug:slug>', category, name = 'category'),
    path('category/<slug:slug>/page/<int:page>', category, name = 'category'),
]
