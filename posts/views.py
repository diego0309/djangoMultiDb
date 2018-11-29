from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.


def index(request):

    postsMysql = Posts.objects.using('ejemplo').all()[:10]
    postsMongo = Posts.objects.using('mongo').all()[:10]
    postsSqlite = Posts.objects.all()[:10]

    context = {
        'title': 'Posts obtenidos desde mysql',
        'title2': 'Posts obtenidos desde sqlite',
        'title3': 'Posts obtenidos desde mongoDB',
        'postsMysql': postsMysql,
        'postsSqlite': postsSqlite,
        'postsMongo': postsMongo
    }

    return render(request, 'posts/index.html', context)


def details(request, id):
    post = Posts.objects.using('ejemplo').get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)


def nuevo(request):
    context = {
        'title': 'Nuevo post'
    }
    return render(request, 'posts/nuevo.html', context)
