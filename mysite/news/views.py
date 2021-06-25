from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    article_list = Article.objects.filter(pub_year=year)
    context = {'year': year, 'article_list': article_list}
    return render(request, 'news/year_archive.html', context)
