from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return HttpResponse('<h1>Тут будет таблица мостов</h1>')


def input_brige_form(request):
    return HttpResponse('<h1>Тут будет форма мостов</h1>')

def brige(request, brige_id):
    if int(brige_id) > 1000:
        return redirect('input_brige')

    return HttpResponse(f"<h1>Описание моста {brige_id}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не ннейдени</h1>')