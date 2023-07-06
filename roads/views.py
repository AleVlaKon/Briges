from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import *
from .models import *


# Create your views here.
def road_index(request):
    """Главная страница"""
    return render(request, 'roads/index.html')

# def road_index(request):
#     """Выводит таблицу дорог"""
#     roads = Uchastok.objects.all()
#     return render(request, 'roads/list_roads.html', {'roads': roads})

class RoadIndex(ListView):
    '''Список всех дорог'''
    model = Uchastok
    form_class = FilterForm
    template_name = 'roads/list_roads.html'
    context_object_name = 'roads'

    def get_context_data(self, **kwargs):
        context = super(RoadIndex, self).get_context_data(**kwargs)
        context['form'] = FilterForm()
        return context


class RoadIndexFilter(ListView):
    '''Список отфильтрованных дорог дорог'''
    model = Uchastok
    form_class = FilterForm
    template_name = 'roads/list_roads.html'
    context_object_name = 'roads'


    def get_queryset(self):
        # queryset = Uchastok.objects.filter(number__znachenie__in=self.request.GET.get('a'))
        queryset = Uchastok.objects.filter(number__znachenie__in=self.request.GET.getlist('prinadlezhnost'))
        return queryset
    

    def get_context_data(self, **kwargs):
        print(self.request.GET.getlist('prinadlezhnost'))
        context = super(RoadIndexFilter, self).get_context_data(**kwargs)
        context['form'] = FilterForm()
        return context




def input_road_form(request):
    if request.method == 'GET':
        form = AddUchastokForm(request.GET)
        print(request.GET)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddUchastokForm()

    return render(request, 'roads/add_road.html', {'form': form})

def road(request, road_id):
    if int(road_id) > 1000:
        return redirect('input_brige')

    return HttpResponse(f"<h1>Описание моста {road_id}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не ннейдени</h1>')