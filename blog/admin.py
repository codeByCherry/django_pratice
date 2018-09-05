from django.contrib import admin
from .models import BlogArticle


class BlogArticleAdmin(admin.ModelAdmin):
    # 管理页显示 col 的类别
    list_display = ('title', 'author', 'publish',)
    # 右侧过滤器，比如按时间过滤
    list_filter = ('publish', 'author',)
    # 搜索范围
    search_fields = ('title', 'body',)

    ordering = ['publish', 'author', ]

# Register your models here.
admin.site.register(BlogArticle, BlogArticleAdmin)
