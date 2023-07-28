from django import forms
from django.forms import ModelForm, CheckboxInput, CheckboxSelectMultiple
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django.forms import formset_factory
from .models import *



class FilterForm(forms.Form):
    prinadlezhnost = forms.ModelChoiceField(queryset=Znachenie.objects.all(), widget=CheckboxSelectMultiple)


class AddRoadForm(forms.ModelForm):
    '''Форма ввода дороги'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['km'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['owner'].widget.attrs['class'] = 'form-control'
        self.fields['znachenie'].widget.attrs['class'] = 'form-select'
        self.fields['osevaya_nagruzka'].widget.attrs['class'] = 'form-control'
        self.fields['start_uchastka'].widget.attrs['class'] = 'form-control'
        self.fields['end_uchastka'].widget.attrs['class'] = 'form-control'
        self.fields['end_uchastka'].widget.attrs['class'] = 'form-control'
        self.fields['full_lenght'].widget.attrs['class'] = 'form-control'
        self.fields['etap_proekta'].widget.attrs['class'] = 'form-select'


    class Meta:
        model = Road
        fields = ['number', 
                  'name',
                  'km',
                  'category' ,
                  'owner' ,
                  'znachenie',
                  'osevaya_nagruzka',
                  'start_uchastka',
                  'end_uchastka',
                  'full_lenght',
                  'etap_proekta',
                  ]


RoadFormset = inlineformset_factory(Road, PokrytieUchastka, extra=2, fields='__all__')

