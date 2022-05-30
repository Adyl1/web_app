from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('<h1>about<h1/>')


def index2(request):
    return HttpResponse('<h1>this is index2<h1/>')

def index3(request):
    return HttpResponse('<h1>this is index3<h1/>')

def index4(request):
    return HttpResponse('<h1>this is index4<h1/>')

def index5(request):
    return HttpResponse('<h1>this is index5<h1/>')






