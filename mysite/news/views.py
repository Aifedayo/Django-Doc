from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_year=year)
    context = {'year': year, 'article_list': a_list}
