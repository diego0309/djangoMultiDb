from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts, PostCassandra
from .forms import PostForm
from datetime import datetime
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster
# Create your views here.


def index(request):

    postsMysql = Posts.objects.using('ejemplo').all()
    postsMongo = Posts.objects.using('mongo').all()
    postsSqlite = Posts.objects.all()
    postsCassandra = PostCassandra.objects.all()

    context = {
        'title': 'Posts obtenidos desde mysql',
        'title2': 'Posts obtenidos desde sqlite',
        'title3': 'Posts obtenidos desde mongoDB',
        'title4': 'Posts obtenidos desde cassandra',
        'postsMysql': postsMysql,
        'postsSqlite': postsSqlite,
        'postsMongo': postsMongo,
        'postsCassandra': postsCassandra
    }

    return render(request, 'posts/index.html', context)


def detailsSqLite(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)


def detailsMySql(request, id):
    post = Posts.objects.using('ejemplo').get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)


def detailsMongo(request, id):
    post = Posts.objects.using('mongo').get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)

def detailsCassandra(request, id):
    post = PostCassandra.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)


def nuevo(request):

    if request.method == "POST":

        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_At = datetime.now()
            if request.POST['bd'] == 'mongo':
                post.save(using='mongo')
                context = {
                    'post': post
                }
                return redirect(detailsMongo, id=post.id)
            if request.POST['bd'] == 'mysql':
                post.save(using='ejemplo')
                context = {
                    'post': post
                }
                return redirect(detailsMySql, id=post.id)
            if request.POST['bd'] == 'sqlite':
                post.save()
                context = {
                    'post': post
                }
                return redirect(detailsSqLite, id=post.id)
            if request.POST['bd'] == 'cassandra':
                cluster = Cluster(['127.0.0.1'])
                session = cluster.connect()
                session.set_keyspace('db')
                insert = PostCassandra(id = PostCassandra.objects.all().count()+1, title= request.POST['title'], body=request.POST['body'])
                insert.save()
                cluster.shutdown()
                context = {
                    'post': request.POST.get('id', 1)
                }
                return redirect(detailsCassandra, id=PostCassandra.objects.all().count())

    else:
        form = PostForm()

    context = {
        'title': 'Nuevo post',
        'form': form
    }
    return render(request, 'posts/nuevo.html', context)


def deleteSqlite(request, id=None):
    object = Posts.objects.get(id=id)
    object.delete()
    return redirect(index)


def deleteMysql(request, id=None):
    object = Posts.objects.using('ejemplo').get(id=id)
    object.delete()
    return redirect(index)


def deleteMongo(request, id=None):
    object = Posts.objects.using('mongo').get(id=id)
    object.delete()
    return redirect(index)

def deleteCassandra(request, id=None):
    object = PostCassandra.objects.get(id=id)
    object.delete()
    return redirect(index)