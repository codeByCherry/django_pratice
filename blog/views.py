from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticle


# Create your views here.
def index(request):
    blogArticles = BlogArticle.objects.all()
    context = dict(
        blogArticles=blogArticles,
    )
    return render(request, 'blog/index.html', context=context)
