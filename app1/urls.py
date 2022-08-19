from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('index',views.index,name='index'),
    path('all',views.index1,name='index'),
    path('about.html',views.about,name='about'),
    path('post.html/<int:i>',views.post,name='post')
]