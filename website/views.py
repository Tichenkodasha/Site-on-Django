from django.shortcuts import render
from django.http import HttpResponse


# Это библиотека для почтового сервера. Она устарела поэтому нужно заменить на Authlib.
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def home(request):
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')

