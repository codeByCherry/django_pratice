from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:blogArticle_id>/", views.blogArticle_content, name="blogArticle_content"),

]

