from django.shortcuts import render
from django.http import HttpResponse


def index(request, ):
    some_str = ''
    return render(request, 'index.html', {
        'some_str': some_str
    })


def acricles(request):
    return  HttpResponse("This is 'acricle'")


def archive(request):
    return HttpResponse("Hello, you are in archive")


def user(request):
    return render(request, 'user.html')


def article(request, article_number):
    return render(request, 'Article.html', {
        'article_number': article_number
    })


def aa(request, article_number=""):
    return HttpResponse("this is an article`s archive")


def slug(request, article_number, slug_text=""):
    return render(request, 'slug.html', {
        'slug_text': slug_text,
    })


def u_number(request, users_number):
    return HttpResponse(f"number: {users_number}")


def regex(request, text):
    return HttpResponse(f"it is regex: {text}")