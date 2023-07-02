from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import *


class FilterForm(forms.Form):
    prinadlezhnost = forms.ModelChoiceField(queryset=Znachenie.objects.all())



class AddUchastokForm(forms.ModelForm):
    class Meta:
        model = Uchastok
        fields = '__all__'

# RoadFormset = inlineformset_factory(Road, Uchastok, extra=1, fields=('number', 'subnumber', 'km', 'category'))