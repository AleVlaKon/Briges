from django import forms
from django.forms import ModelForm, CheckboxInput, CheckboxSelectMultiple
from django.forms.models import inlineformset_factory
from django.forms import formset_factory
from .models import *


class FilterForm(forms.Form):
    prinadlezhnost = forms.ModelChoiceField(queryset=Znachenie.objects.all(), widget=CheckboxSelectMultiple)



class AddUchastokForm(forms.ModelForm):
    class Meta:
        model = Uchastok
        fields = '__all__'

#RoadFormset = inlineformset_factory(Road, Uchastok, extra=1)
UchastokFormSet = formset_factory(AddUchastokForm, extra=3)


class AddRoadForm(forms.ModelForm):
    class Meta:
        model = Road
        fields = '__all__'

RoadFormSet = formset_factory(AddRoadForm, extra=3)






