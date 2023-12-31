from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .models import *


# Create your views here.
def road_index(request):
    """Главная страница"""
    return render(request, 'roads/index.html')

class MainListObject(ListView):
    '''Главная страница с перечнем объектов'''
    model=NameObject
    template_name = 'roads/index.html'

    def get_queryset(self):
        return NameObject.objects.filter(in_archive=False)



class ArchiveListObject(ListView):
    '''Главная страница с перечнем объектов'''
    model=NameObject
    template_name = 'roads/index.html'

    def get_queryset(self):
        return NameObject.objects.filter(in_archive=True)



class RoadListObject(ListView):
    model = Road
    template_name = 'roads/list_roads.html'
    context_object_name = 'roads'

    def get_queryset(self):
        return Road.objects.filter(etap_proekta__object_name__id=self.kwargs['obj_id'])





class RoadIndex(ListView):
    '''Список всех дорог'''
    model = Road
    form_class = FilterForm
    template_name = 'roads/list_roads.html'
    context_object_name = 'roads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilterForm()
        return context


class RoadIndexFilter(ListView):
    '''Список отфильтрованных дорог дорог'''
    model = Road
    form_class = FilterForm
    template_name = 'roads/list_roads.html'
    context_object_name = 'roads'


    def get_queryset(self):
        queryset = Road.objects.filter(number__znachenie__in=self.request.GET.getlist('prinadlezhnost'))
        return queryset
    

    def get_context_data(self, **kwargs):
        print(self.request.GET.getlist('prinadlezhnost'))
        context = super(RoadIndexFilter, self).get_context_data(**kwargs)
        context['form'] = FilterForm()
        return context


class InputRoad(CreateView):
    form_class = AddRoadForm
    template_name = 'roads/add_road.html'
    success_url = reverse_lazy('input_road')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['pokr_form'] = PokrFormset(self.request.POST)
        else:
            context['pokr_form'] = PokrFormset()
        return context


    def form_valid(self, form):
        context = self.get_context_data()
        uchastok = context['pokr_form']
        # pokrytie = context['pokr_form']
        self.object = form.save()
        if uchastok.is_valid():
            uchastok.instance = self.object
            uchastok.save()


# class AddUchastok(CreateView):
#     '''Страница ввода участка и покрытия на участке'''
#     form_class = AddUchastokForm
#     template_name = 'roads/add_uchastok.html'
#     # success_url = reverse_lazy('listroads')
    

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.POST:
#             context['pokr_form'] = PokrFormSet(self.request.POST)
#         else:
#             context['pokr_form'] = PokrFormSet()
#         return context
    


#     def form_valid(self, form):
#         context = self.get_context_data()
#         uchastok = context['pokr_form']
#         # pokrytie = context['pokr_form']
#         self.object = form.save()
#         if uchastok.is_valid():
#             uchastok.instance = self.object
#             uchastok.save()

#         # if pokrytie.is_valid():
#         #     pokrytie.instance = self.object
#         #     pokrytie.save()    
#         return super().form_valid(form)

    
def road(request, road_id):
    if int(road_id) > 1000:
        return redirect('input_brige')

    return HttpResponse(f"<h1>Описание моста {road_id}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не ннейдени</h1>')





