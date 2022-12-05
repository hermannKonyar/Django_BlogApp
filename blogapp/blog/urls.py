from django.urls import path
from . import views


urlpatterns = [
    path("", views.index,name='home'),
    path("main", views.index),
    path("blogs", views.blogs,name='blogs'),
    path("blogs/<int:id>", views.blog_details,name='blog_details'),
    path("tarifler",views.foods,name='foods')

]
