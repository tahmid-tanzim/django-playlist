from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/list.html", {"articles": articles})


def details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, "articles/details.html", {"article": article})