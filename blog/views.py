from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import BlogArticle


# Create your views here.
def index(request):
    blogArticles = BlogArticle.objects.all()
    context = dict(
        blogArticles=blogArticles,
    )
    return render(request, 'blog/index.html', context=context)


def blogArticle_content(request, blogArticle_id):
    blogArticle = get_object_or_404(BlogArticle, id=blogArticle_id)
    context = dict(
        blogArticle=blogArticle,
    )
    return render(request, 'blog/content.html', context=context)
