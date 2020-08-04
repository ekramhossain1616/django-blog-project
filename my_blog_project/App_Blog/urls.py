from django.urls import path,include
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('',views.BlogList.as_view(), name = 'blog_list'),
    path('create/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<str:slug>',views.blog_details, name='blog_details'),
    path('liked/<pk>/',views.liked,name='liked'),
    path('unliked/<pk>/',views.unliked,name='unliked'),
    path('my_blogs/',views.MyBlogs.as_view(),name='my_blogs'),
    path('edit_blog/<pk>/',views.UpdateBlog.as_view(),name='edit_blog'),

]
